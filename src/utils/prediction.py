import pandas as pd
import numpy as np
from tqdm import tqdm
import yaml
from joblib import load


def get_col_configs(config_f):
    with open(config_f) as fh:
        config_dict = yaml.safe_load(fh)

    # print(config_dict)
    return config_dict


def test_parsing(dataframe, config_dict):
    dataframe["hgvs"] = (
        dataframe["all_mappings"].str.split(";", expand=True)[0].str.split(":", expand=True)[5]
    )
    dataframe["consequence"] = dataframe["so"]

    # Drop variant info columns so we can perform one-hot encoding
    var = dataframe[config_dict["display_cols"].keys()]
    var.columns = list(config_dict["display_cols"].values())
    dataframe = dataframe.drop(config_dict["detail_cols"], axis=1)
    dataframe = dataframe.replace([".", "-"], np.nan)

    for key in tqdm(dataframe.columns):
        try:
            dataframe[key] = dataframe[key].astype("float64").copy()
        except:
            dataframe[key] = dataframe[key].copy()

    # Perform one-hot encoding
    dataframe = pd.get_dummies(dataframe, prefix_sep="_")
    dataframe[config_dict["allele_freq_columns"]] = dataframe[
        config_dict["allele_freq_columns"]
    ].fillna(0)

    for key in tqdm(config_dict["median_scores"].keys()):
        if key in dataframe.columns:
            dataframe[key] = (
                dataframe[key].fillna(config_dict["median_scores"][key]).astype("float64")
            )

    df2 = pd.DataFrame()
    for key in tqdm(config_dict["filtered_cols"]):
        if key in dataframe.columns:
            df2[key] = dataframe[key].copy()
        else:
            df2[key] = 0

    del dataframe

    df2 = df2.drop(config_dict["detail_cols"], axis=1)

    return df2, var


def load_model():
    with open("./model/MLP.joblib", "rb") as f:
        clf = load(f)
    return clf


def predict(uploaded_file):
    # Load the config file as dictionary
    config_f = "./configs/app_cols.yaml"
    config_dict = get_col_configs(config_f)
    clf = load_model()
    df = pd.read_csv(
        uploaded_file,
        comment="#",
        usecols=config_dict["raw_cols"],
        low_memory=False,
    )
    df, var = test_parsing(df, config_dict)
    y_score = clf.predict_proba(df)
    pred = pd.DataFrame(y_score, columns=["Ditto_Benign_score", "Ditto score"])
    overall = pd.concat([var, pred[["Ditto score"]]], axis=1)
    overall["Ditto score"] = overall["Ditto score"].round(2)
    del df, var, pred, clf, config_f, config_dict
    return overall
