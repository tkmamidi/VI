import csv


def parse_data(file_path):
    parsed_data = {}
    table_header = []
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        table_header = next(csv_reader)
        cols_to_display = list(range(1, 8)) + [11, 12, 23]  # Select columns
        for row in csv_reader:
            selected_data = [row[i] for i in cols_to_display]
            selected_header = [table_header[i] for i in cols_to_display]
            parsed_line = {selected_header[i]: selected_data[i] for i in range(len(selected_data))}
            parsed_data[",".join(row)] = parsed_line
    return parsed_data, table_header
