import pandas as pd

csv_file_path = "home/HOME.csv"

def import_csv_file(csv):
    csv_file = pd.read_csv(csv, delimiter=';')
    return csv_file

