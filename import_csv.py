import csv

with open("home/HOME.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")

    for row in csv_reader:
        print(row)

