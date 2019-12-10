import calculate_price as cp
import math_methods as mm

# df.loc[df["Boligtype"] == "Ejerlejlighed"]

# import csv file
csv_file = cp.import_csv_file()

# create subsets for each property type
variables = ["Alder", "Grundareal", "Boligareal", "Liggetid"]
subset = csv_file.loc[:, ["EjdType", "Kontantpris", "Alder", "Grundareal", "Boligareal", "Liggetid"]]

subset_ejer = subset.loc[subset["EjdType"] == "Ejerlejlighed"]
subset_ejer = subset_ejer.dropna()
subset_ejer = subset_ejer.drop("EjdType", axis=1)
subset_ejer_uden_grundareal = subset_ejer.drop("Grundareal", axis=1)

subset_rakke = subset.loc[subset["EjdType"] == "Raekkehus"]
subset_rakke = subset_rakke.dropna()
subset_rakke = subset_rakke.drop("EjdType", axis=1)

subset_villa1 = subset.loc[subset["EjdType"] == "Villa, 1 fam."]
subset_villa1 = subset_villa1.dropna()
subset_villa1 = subset_villa1.drop("EjdType", axis=1)

subset_villa2 = subset.loc[subset["EjdType"] == "Villa, 2 fam."]
subset_villa2 = subset_villa2.dropna()
subset_villa2 = subset_villa2.drop("EjdType", axis=1)

# find slopes
slopes_ejer = mm.standardised_slopes(subset_ejer, variables)
slopes_rakke = mm.standardised_slopes(subset_rakke, variables)
slopes_villa1 = mm.standardised_slopes(subset_villa1, variables)
slopes_villa2 = mm.standardised_slopes(subset_villa2, variables)
slopes_ejer_uden = mm.standardised_slopes(subset_ejer_uden_grundareal, variables)

# find residual
constants_ejer, a_dataframes_ejer = mm.residual(subset_ejer, slopes_ejer)
constants_rakke, a_dataframes_rakke = mm.residual(subset_rakke, slopes_rakke)
constants_villa1, a_dataframes_villa1 = mm.residual(subset_villa1, slopes_villa1)
constants_villa2, a_dataframes_villa2 = mm.residual(subset_villa2, slopes_villa2)
constants_ejer_uden, a_dataframes_ejer_uden = mm.residual(subset_ejer_uden_grundareal, slopes_ejer_uden)

def boligtype_define(boligtype_tal):
    if boligtype_tal == 1:
        boligtype = "Ejerlejlighed"
    elif boligtype_tal == 2:
        boligtype = "Rækkehus"
    elif boligtype_tal == 3:
        boligtype = "Villa1"
    else:
        boligtype = "Villa2"

    return boligtype

while True:
    print("""1: Ejerlejlighed
    2: Rækkehus
    3. Villa1
    4. Villa2""")
    property_nr = input("Indtast tallet for din boligtype: ")
    boligtype = boligtype_define(property_nr)

    alder = float(input("Indtast din boligs alder: "))
    liggetid = float(input("Indtast liggetiden for din bolig: "))
    grundareal = float(input("Indtast grundarealet for din bolig: "))
    boligareal = float(input("Indtast boligarealet for din bolig: "))



    break