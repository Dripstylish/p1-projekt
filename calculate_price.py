import pandas as pd
import math_methods as mm

csv_file_path = "home/HOME.csv"

def import_csv_file(csv = csv_file_path):
    csv_file = pd.read_csv(csv, delimiter=';')
    return csv_file