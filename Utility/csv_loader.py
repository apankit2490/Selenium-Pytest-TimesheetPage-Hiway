import csv

def get_csv_data(csv_path):
    rows = []
    csv_data = open(csv_path, "rt")
    content = csv.reader(csv_data)
    next(content, None)
    for row in content:
        rows.append(row)
    return rows
