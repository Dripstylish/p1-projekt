import pandas as pd
import matplotlib.pyplot as plt
import math_methods as mm

csv_file_path = "home/HOME.csv"

def import_csv_file(csv = csv_file_path):
    csv_file = pd.read_csv(csv, delimiter=';')
    return csv_file

def create_test_train(dataframe):
    amount = int(len(dataframe)/6)
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
    plt.clf()
    print("Scatterplot complete")

def create_scatterplot_residual_progression(list, save_file):
    print("Starting scatterplot", save_file)
    turns = [1, 2, 3]
    plt.title(save_file)
    plt.xlabel("Niveau")
    plt.ylabel("Residual")
    plt.plot(turns, list, "ro")
    plt.savefig("{}.pdf".format(save_file))
    plt.clf()
    print("Scatterplot complete")

    """
    plt.title("Average CG for small- and large-eared elves")
    plt.xlabel("Ear Length")
    plt.ylabel("GC Percentage")
    plt.plot(plot_dict_small["earlength"], plot_dict_small["GC percentage"], "ro")
    plt.plot(plot_dict_large["earlength"], plot_dict_large["GC percentage"], "b*")
    plt.legend(["Small Ears", "Large Ears"], loc=4)
    plt.savefig("GC_vs_earsize.pdf")
    """

def create_scatterplots(dataframe, constants, name):
    print("Creating scatterplots for", name)
    list1 = dataframe.loc[:, "Kontantpris"].values
    mean_residuals = []
    for i in range(1, 4):
        list2 = constants["dataframe_y{}".format(i)].values
        create_scatterplot_price(list2, list1, "{}_y{}".format(name, i))
        mean_residuals.append(mm.mean(list2)[0])
    create_scatterplot_residual_progression(mean_residuals, "{}_Residualer".format(name))

def test(dataframe, constants):
    resultat = []
    difference_list = []
    difference_list_percent = []
    for row in dataframe.iterrows():
        variables = {"Alder": row[1]["Alder"], "Liggetid": row[1]["Liggetid"], "Grundareal": row[1]["Grundareal"], "Boligareal": row[1]["Boligareal"]}
        kontantpris = (constants["a_1_max"] * variables[constants["a_1"]] + constants["b_1"]) + (
                constants["a_2_max"] * variables[constants["a_2"]] + constants["b_2"]) + (
                constants["a_3_max"] * variables[constants["a_3"]] + constants["b_3"]) + (
                constants["a_4_max"] * variables[constants["a_4"]] + constants["b_4"])
        #print("\nRigtige Kontantpris: {} kr.".format(row[1]["Kontantpris"]))
        #print("Gættede Kontantpris: {} kr.".format(kontantpris))
        difference = row[1]["Kontantpris"] - kontantpris
        difference_percent = abs(kontantpris / (row[1]["Kontantpris"] / 100))
        #print("Forskel: {} kr.".format(difference))
        difference_list.append(difference)
        difference_list_percent.append(difference_percent)
        if difference == 0:
            resultat.append(True)
        else:
            resultat.append(False)
    #print("{}/{} Korrekt".format(procent_resultat.count(True), len(dataframe)))
    percent = resultat.count(True) / len(dataframe)
    #print("{}% Korrekt".format(percent))
    mean = mm.mean(difference_list)
    mean_percent = mm.mean(difference_list_percent)
    print("Gennemsnitlig forskel: {} kr.".format(round(mean)))
    print("Procentvis Gennemsnitlig forskel: {}%".format(round(mean_percent)))
    return difference_list, difference_list_percent

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