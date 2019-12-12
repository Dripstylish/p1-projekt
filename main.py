import calculate_price as cp
import math_methods as mm

# import csv file
csv_file = cp.import_csv_file()

# create subsets for each property type
variables = ["Alder", "Grundareal", "Boligareal", "Liggetid"]
subset = csv_file.loc[:, ["EjdType", "Kontantpris", "Alder", "Grundareal", "Boligareal", "Liggetid"]]

# Delimiting variable scopes
subset = subset.loc[subset["Alder"] >= -10]
subset = subset.loc[subset["Alder"] < 300]
subset = subset.loc[subset["Boligareal"] >= 0]
subset = subset.loc[subset["Boligareal"] < 5000]
subset = subset.loc[subset["Grundareal"] >= 0]
subset = subset.loc[subset["Grundareal"] < 300000]
subset = subset.loc[subset["Liggetid"] >= 0]
subset = subset.loc[subset["Liggetid"] < 2000]

subset_ejer = subset.loc[subset["EjdType"] == "Ejerlejlighed"]
subset_ejer = subset_ejer.dropna()
subset_ejer = subset_ejer.drop("EjdType", axis=1)
subset_ejer = subset_ejer.loc[subset_ejer["Grundareal"] < 200]

subset_ejer_uden_grundareal = subset_ejer.drop("Grundareal", axis=1)
variables_uden = ["Alder", "Boligareal", "Liggetid"]

subset_ejer_train, subset_ejer_test = cp.create_test_train(subset_ejer)

subset_rakke = subset.loc[subset["EjdType"] == "Raekkehus"]
subset_rakke = subset_rakke.dropna()
subset_rakke = subset_rakke.drop("EjdType", axis=1)
subset_rakke = subset_rakke.loc[subset_rakke["Grundareal"] < 1000]

subset_rakke_train, subset_rakke_test = cp.create_test_train(subset_rakke)

subset_villa1 = subset.loc[subset["EjdType"] == "Villa, 1 fam."]
subset_villa1 = subset_villa1.dropna()
subset_villa1 = subset_villa1.drop("EjdType", axis=1)

subset_villa1_train, subset_villa1_test = cp.create_test_train(subset_villa1)

# for lille datasæt; 538 rækker
subset_villa2 = subset.loc[subset["EjdType"] == "Villa, 2 fam."]
subset_villa2 = subset_villa2.dropna()
subset_villa2 = subset_villa2.drop("EjdType", axis=1)

subset_villa2_train, subset_villa2_test = cp.create_test_train(subset_villa2)

# find slopes
slopes_ejer = mm.standardised_slopes(subset_ejer_train, variables)
slopes_rakke = mm.standardised_slopes(subset_rakke_train, variables)
slopes_villa1 = mm.standardised_slopes(subset_villa1_train, variables)
slopes_villa2 = mm.standardised_slopes(subset_villa2_train, variables)

# find residual
constants_ejer, a_dataframes_ejer = mm.residual(subset_ejer_train, slopes_ejer)
constants_rakke, a_dataframes_rakke = mm.residual(subset_rakke_train, slopes_rakke)
constants_villa1, a_dataframes_villa1 = mm.residual(subset_villa1_train, slopes_villa1)
constants_villa2, a_dataframes_villa2 = mm.residual(subset_villa2_train, slopes_villa2)

# create scatterplots
cp.create_scatterplots(subset_ejer_train, constants_ejer, "Ejerlejlighed")
cp.create_scatterplots(subset_rakke_train, constants_rakke, "Rækkehus")
cp.create_scatterplots(subset_villa1_train, constants_villa1, "Villa1")
cp.create_scatterplots(subset_villa2_train, constants_villa2, "Villa2")

# test
print("Ejerlejlighed")
difference_ejer, difference_ejer_percent = cp.test(subset_ejer_test, constants_ejer)
print("Rækkehus")
difference_rakke, difference_rakke_percent = cp.test(subset_rakke_test, constants_rakke)
print("Villa1")
difference_villa1, difference_villa1_percent = cp.test(subset_villa1_test, constants_villa1)
print("Villa2")
difference_villa2, difference_villa2_percent = cp.test(subset_villa2_test, constants_villa2)

difference_list = difference_ejer + difference_rakke + difference_villa1 + difference_villa2
difference_list_percent = difference_ejer_percent + difference_rakke_percent + difference_villa1_percent + difference_villa2_percent

print("\nI alt")
mean = mm.mean(difference_list)
mean_percent = mm.mean(difference_list_percent)
print("Gennemsnitlig forskel: {} kr.".format(round(mean)))
print("Procentvis Gennemsnitlig forskel: {}%".format(round(mean_percent)))