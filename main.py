import calculate_price as cp
import math_methods as mm

# import csv file
csv_file = cp.import_csv_file()

# create subsets for each property type
variables = ["Alder", "Grundareal", "Boligareal", "Liggetid"]
subset = csv_file.loc[:, ["EjdType", "Kontantpris", "Alder", "Grundareal", "Boligareal", "Liggetid"]]

subset_ejer = subset.loc[subset["EjdType"] == "Ejerlejlighed"]
subset_ejer = subset_ejer.dropna()
subset_ejer = subset_ejer.drop("EjdType", axis=1)
subset_ejer_uden_grundareal = subset_ejer.drop("Grundareal", axis=1)
variables_uden = ["Alder", "Boligareal", "Liggetid"]

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
slopes_ejer_uden = mm.standardised_slopes(subset_ejer_uden_grundareal, variables_uden)

# find residual
constants_ejer, a_dataframes_ejer = mm.residual(subset_ejer, slopes_ejer)
constants_rakke, a_dataframes_rakke = mm.residual(subset_rakke, slopes_rakke)
constants_villa1, a_dataframes_villa1 = mm.residual(subset_villa1, slopes_villa1)
constants_villa2, a_dataframes_villa2 = mm.residual(subset_villa2, slopes_villa2)
constants_ejer_uden, a_dataframes_ejer_uden = mm.residual(subset_ejer_uden_grundareal, slopes_ejer_uden)

#property_nr = 1
#alder = 2.0
#liggetid = 3.0
#grundareal = 40.0
#boligareal = 65.0

while True:
    print("Boligtyper:\n1: Ejerlejlighed\n2: Rækkehus\n3. Villa1\n4. Villa2")
    property_nr = int(input("Indtast tallet for din boligtype: "))

    # Define property
    if property_nr == 1:
        property_type = "Ejerlejlighed"
        constants = constants_ejer
        a_dataframes = a_dataframes_ejer
    elif property_nr == 2:
        property_type = "Rækkehus"
        constants_ejer_uden = constants_rakke
        a_dataframes = a_dataframes_rakke
    elif property_nr == 3:
        property_type = "Villa1"
        constants = constants_villa1
        a_dataframes = a_dataframes_villa1
    else:
        property_type = "Villa2"
        constants = constants_villa2
        a_dataframes = a_dataframes_villa2

    alder = float(input("Indtast din boligs alder: "))
    liggetid = float(input("Indtast liggetiden for din bolig: "))
    grundareal = float(input("Indtast grundarealet for din bolig: "))
    boligareal = float(input("Indtast boligarealet for din bolig: "))

    variables = {"Alder": alder, "Liggetid": liggetid, "Grundareal": grundareal, "Boligareal": boligareal}

    # Print status
    print("\nBoligtype: {}\nAlder: {}\nLiggetid: {}\nGrundareal: {}\nBoligareal: {}".format(property_type, alder,
                                                                                          liggetid, grundareal,
                                                                                          boligareal))

    # Calculate price
    kontantpris = (constants["a_1_max"] * variables[constants["a_1"]] + constants["b_1"]) + (constants["a_2_max"] * variables[constants["a_2"]] + constants["b_2"]) + (constants["a_3_max"] * variables[constants["a_3"]] + constants["b_3"]) + (constants["a_4_max"] * variables[constants["a_4"]] + constants["b_4"])
    print("Optimale Kontantpris: {} kr.".format(kontantpris))
    break