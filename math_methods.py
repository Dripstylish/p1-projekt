import math
import pandas as pd

def slope(dataframe1, dataframe2):
    """
    Finds the slope between two dataframes.
    :param dataframe1: variable x
    :param dataframe2: variable y
    :return: slope as float
    """
    power = dataframe1.pow(2)
    mul = dataframe1.mul(dataframe2)
    n = len(dataframe1)

    return float((n * mul.sum() - dataframe1.sum() * dataframe2.sum()) / (n * power.sum() - (dataframe1.sum()**2)))

def mean(list):
    """
    Finds the mean value of a list.
    :param list: a list of slopes or intersections
    :return: mean value as float
    """
    return sum(list) / len(list)

def standard_deviation(list):
    """
    Finds the standard deviation of a list.
    :param list: a list of slopes or intersections
    :return: standard deviation as float
    """
    values = []
    for item in list:
        values.append(abs(item - mean(list)))

    return math.sqrt(sum(values)/len(list)), -math.sqrt(sum(values)/len(list))

def standardisation(dataframe):
    """
    Standardises the values from a dataframe.
    :param dataframe: a dataframe of slopes or intersections
    :return: standardised values in a dataframe
    """
    std_dev, _ = standard_deviation(dataframe.values)
    dataframe_sub = dataframe.sub(mean(dataframe.values))
    dataframe_div = dataframe_sub.div(std_dev)
    return dataframe_div

def find_max(dataframe):
    """
    Finds the maximum value of a dataframe.
    :param dataframe: a dataframe of slopes
    :return: maximum value as float and the belonging variable as string
    """
    abs = dataframe.abs()
    locate = dataframe.loc[abs.idxmax(), "Hældninger"]
    a_max_variable = locate.index[0]
    a_max = dataframe.at[a_max_variable, "Hældninger"]
    return a_max, a_max_variable

def intersection(dataframe1, dataframe2):
    """
    Finds the intersection between two dataframes.
    :param dataframe1: variable x
    :param dataframe2: variable y
    :return: intersection as float
    """
    power = dataframe1.pow(2)
    mul = dataframe1.mul(dataframe2)
    n = len(dataframe1)
    return float(((dataframe2.sum() * power.sum()) - (dataframe1.sum()) * mul.sum())/((n * power.sum()) - (dataframe1.sum()**2)))

"""
Input: Dictionary med hældninger

residual(dataframe, hældningsdict, niveau): # niveau starter fra 1

  name_a = "a_" + str(niveau)
  name_a_max = "a_" + str(niveau) + "_max"
  name_b = "b_" + str(niveau)

  bolig_konstanter = {}
  a_lister = {}

  variabler = []
  for key in hældningsdict.keys():
    variabler.append(key)

  a_max, a_max_variabel = find_max(hældningsdict)
  variabler.remove(a_max_variabel)

  b = standardiseret_skæring(dataframe, variabler, a_max_variabel)

  bolig_konstanter[name_a] = a_max_variabel
  bolig_konstanter[name_a_max] = a_max
  bolig_konstanter[name_b] = b

  linje_liste = []
  for element in dataframe[a_max_variabel]:
    linje_liste.append(a_max * element + b)

  a_lister[name_a] = linje_liste

  y_2_liste = []
  loop_level = 0
  for element in dataframe["y"]:
    y_2_liste.append(element - linje_liste[loop_level])
    loop_level += 1

  dataframe2 = y_2_liste, dataframe.loc[variabler]
  hældninger2 = standardiseret_hældninger(dataframe2)
  niveau2 = niveau + 1

  if len(variabler) >= 1:
    bolig_konstanter2, a_lister2 = residual(dataframe2, hældninger2, niveau2)
    bolig_konstanter.update(bolig_konstanter2)
    a_lister.update(a_lister2)

  if niveau == 1:
    last_residual = dataframe["y"]
    residual = []
    for list in a_lister:
      loop_level = 0
      for element in list:
        residual.append(last_residual - element)
        loop_level += 1
      last_residual = residual
      residual = []

    bolig_konstanter["residual": last_residual]

  return bolig_konstanter, a_lister

Output: Residualet i forhold til det største element i hver liste
"""

def residual(dataframe, hældningsdataframe, niveau = 1):
    name_a = "a_" + str(niveau)
    name_a_max = "a_" + str(niveau) + "_max"
    name_b = "b_" + str(niveau)

    bolig_konstanter = {}
    a_lister = {}

    variabler = []
    for key in hældningsdataframe.index:
        variabler.append(key)

    a_max, a_max_variabel = find_max(hældningsdataframe)
    variabler.remove(a_max_variabel)

    b = standardisation_intersection(dataframe, variabler, a_max_variabel)

    return 1, {"a_1": 2}



"""
Input: Dataframe af variabler

standardiseret_skæring(dataframe, variabler, a_max_variabel):

  skæringsdict = {"b": skæringen(dataframe["y"], dataframe[a_max_variabel])}

  for i in range(len(variabler)):
    skæringsdict["b{}".format(i+2)] = skæringen(dataframe["y"], dataframe[variabler[i]])

  standardiserede_skæringer = standardisering(skæringsdict)

  return standardiserede_skæringer["b"]

Output: Standardiseret skæring med y-aksen for a_max_variabel (et tal)
"""

def standardisation_intersection(dataframe, variables, a_max_variable):
    dataframe_intersections = pd.DataFrame([intersection(dataframe[a_max_variable], dataframe["Kontantpris"])], [a_max_variable], ["Skæringer"])

    for variable in variables:
        dataframe_intersections.loc[variable] = intersection(dataframe[variable], dataframe["Kontantpris"])

    return standardisation(dataframe_intersections)