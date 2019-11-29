import math
import pandas as pd

"""
Input: To lister

hældning(x, y)

hældningen(liste1, liste2):

  liste_sq = []
  for loop liste1:
    liste_sq.append(liste1[x]^2)

  return (len(liste1) * sum(liste1 * liste2)) - (sum(liste1) * sum(liste2)) / ((len(liste1) * sum(liste_sq)) - (liste1)^2)

Output: Hældningen (et tal)
"""

def slope(dataframe1, dataframe2):
    """
    Finds the slope between two dataframes.
    :param dataframe1: variable x
    :param dataframe2: variable y
    :return: slope
    """
    power = dataframe1.pow(2)
    mul = dataframe1.mul(dataframe2)
    n = len(dataframe1)

    return float((n * mul.sum() - dataframe1.sum() * dataframe2.sum()) / (n * power.sum() - (dataframe1.sum()**2)))


"""
Input: Usorteret liste af hældninger

aritmetisk_middelværdi(hældningsliste):

  return sum(hældningsliste)/(len(hældningsliste)

Output: Middelværdi (et tal)
"""

def mean(list):
    """
    Finds the mean value of a list.
    :param list: A list of slopes or intersections
    :return: mean value
    """
    return sum(list) / len(list)


"""
Input: Liste af hældninger

standardafvigelse(hældningliste):

  SD_plus = kvadratrod(sum(abs(hældningsliste - aritmetisk_middelværdi(hældningsliste))/len(hældningliste))
  SD_minus = (-SD_plus)

  return SD_plus, SD_minus

Output: Standardafvigelse (et positivt og et negativt tal)
"""

def standard_deviation(list):
    """
    Finds the standard deviation of a list.
    :param list: A list of slopes or intersections
    :return: standard deviation
    """
    values = []
    for item in list:
        values.append(abs(item - mean(list)))

    return math.sqrt(sum(values)/len(list)), -math.sqrt(sum(values)/len(list))


"""
Input: Usorteret dictionary

standardisering(hældningsdict):

  SD_plus, _ = standardafvigelse(hældningsdict.values())
  standardiseret_hældningsdict = {}

  for key in hældningsdict.keys():
    standardiseret_hældningsdict[key] = (hældningsdict[key] - aritmetisk_middelværdi(hældningsdict.values()))/(SD_plus)

  return standardiseret_hældningsdict

Output: Standardiseret hældningsdictionary
        standardiseret_hældningsdict = {Liggetid: tal, Grundareal: tal, ....}
"""

def standardisation(dataframe):
    std_dev, _ = standard_deviation(dataframe.values)
    dataframe_sub = dataframe.sub(mean(dataframe.values))
    dataframe_div = dataframe_sub.div(std_dev)
    return dataframe_div