import pandas as pd
import matplotlib.pyplot as plt
import math_methods as mm

csv_file_path = "home/HOME.csv"

def import_csv_file(csv = csv_file_path):
    csv_file = pd.read_csv(csv, delimiter=';')
    return csv_file

def create_test_train(dataframe):
    amount = int(len(dataframe)/4)
    subset_train = dataframe.head(int(len(dataframe) - amount))
    subset_test = dataframe.tail(amount)
    return subset_train, subset_test

def create_scatterplot_price(list1, list2, save_file):
    print("Starting scatterplot", save_file)
    plt.title(save_file)
    plt.xlabel("Residual")
    plt.ylabel("Kontantpris")
    plt.plot(list1, list2, "ro")
    plt.savefig("{}.pdf".format(save_file))
    print("Scatterplot complete")

def create_scatterplots(dataframe, constants, name):
    print("Creating scatterplots for", name)
    list1 = dataframe.loc[:, "Kontantpris"].values
    for i in range(1, 4):
        list2 = constants["dataframe_y{}".format(i)].values
        create_scatterplot_price(list2, list1, "{}_y{}".format(name, i))

#property_nr = 1
#alder = 2.0
#liggetid = 3.0
#grundareal = 40.0
#boligareal = 65.0

"""
while True:
    print("Boligtyper:\n1: Ejerlejlighed\n2: Rækkehus\n3: Villa1\n4: Villa2")
    property_nr = int(input("Indtast tallet for din boligtype: "))

    # Define property
    if property_nr == 1:
        property_type = "Ejerlejlighed"
        constants = constants_ejer
        a_dataframes = a_dataframes_ejer
    elif property_nr == 2:
        property_type = "Rækkehus"
        constants = constants_rakke
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
    print("\nOptimale Kontantpris: {} kr.".format(kontantpris))

    option = input("\nType a to retry, type q to quit: ")
    if option == "a":
        pass
    elif option == "q":
"""