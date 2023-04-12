def parse_data(df):
    parsed_data = {}
    table_header = df.columns.tolist()

    cols_to_display = list(range(len(table_header)))

    for i, row in df.iterrows():
        selected_data = [str(row[j]) for j in cols_to_display]
        parsed_line = {table_header[j]: selected_data[j] for j in range(len(selected_data))}
        parsed_data[i] = parsed_line
    return parsed_data, table_header
