import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

import math_methods as mm

#print({'x': range(1,101), 'y': np.random.randn(100)*15+range(1,101)})
#df=pd.DataFrame({'x': range(1,101), 'y': np.random.randn(100)*15+range(1,101)})
#print(df)

csv_file_path = "home/HOME.csv"

def create_headline(text, newline):
    symbol = "-"
    amount = 5
    symbols = symbol*amount
    if newline == 0:
        print(symbols + " " + text + " " + symbols)
    elif newline == 1:
        print("\n" + symbols + " " + text + " " + symbols)
    elif newline == 2:
        print(symbols + " " + text + " " + symbols + "\n")
    else:
        print("\n" + symbols + " " + text + " " + symbols + "\n")


def import_csv_file():
    create_headline("Importing CSV file", 0)
    with open(csv_file_path, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        create_headline("Creating CSV dictionary", 0)
        row_count = 0
        labels = True
        for row in csv_reader:
            if labels:
                csv_dict = {}
                for label in row:
                    csv_dict[label] = []
                labels = False
            else:
                for key in row.keys():
                    list = csv_dict[key]
                    list.append(row[key])
                    csv_dict[key] = list
                row_count = row_count + 1
                """
                if row_count > 10:
                    break
                """

        create_headline("Dictionary complete. Processed {} rows".format(row_count), 0)
        check_if_dirty(csv_dict)
        dataset = clean_dataset(csv_dict)
        print(pd.DataFrame(dataset))
        return dataset

def check_if_dirty(dataset):
    dirty_instances = 0
    create_headline("Checking for dirty data", 3)
    for dataset_key in dataset.keys():
        full_list_count = Counter(dataset[dataset_key])
        for count_key in full_list_count.keys():
            if count_key == "NA":
                print(dataset_key + ": {} NA instances".format(full_list_count[count_key]))
                dirty_instances = dirty_instances + full_list_count[count_key]
    create_headline("Found {} dirty variable instances".format(dirty_instances), 1)

"""
Postnr: int
Salgsdato: dato
EjdType: str
Boligtilstand: str
Kontantpris: float
Boligareal: float
Kaelderareal: float
Grundareal: float
Opfoerelsesaar: int? str? (år)
AntalPlan: int
NytKokken: ??
"""
def clean_dataset(dataset):
    create_headline("Cleaning data", 1)
    data_cleaned = 0
    # TODO: correct datatypes
    list_to_int = ["Postnr"]
    for key in dataset.keys():
        if key == "Postnr":
            [float(i) for i in dataset[key]]

    # TODO: correct data (handle NA occurences)
    create_headline("Cleaning complete. Cleaned {} variables".format(data_cleaned), 2)
    return dataset

def count_occurences(dataset):
    create_headline("Counting occurences in lists in dataset", 1)
    for key in dataset.keys():
        print(key + ": ", Counter(dataset[key]))
    create_headline("Counting complete", 0)

def scatterplot_liggetid_pris(dataset):
    data = dict((n, dataset[n]) for n in ("Liggetid", "Kontantpris"))
    dataframe = pd.DataFrame(data)
    print(dataframe)
    mm.scatterplot_two_variable("Liggetid", "Kontantpris", dataframe)

def calculate_optimal_price():
    # TODO: calculate price
    return

def calculate_property_value():
    # TODO: calculate property value
    return

dataset = import_csv_file()
#scatterplot_liggetid_pris(dataset)