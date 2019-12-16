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

    result = (((dataframe2.sum()) * (power.sum())) - (dataframe1.sum()) * (mul.sum())) / ((n * power.sum()) - (dataframe1.sum() ** 2))
    #result = (((dataframe2.sum()/2) * (power.sum()/2)) - (dataframe1.sum()/2) * (mul.sum()/2)) / ((n * power.sum()) - (dataframe1.sum() ** 2))/4
    return result


def standardised_intersection(dataframe, variables, a_max_variable):
    """
    Standardises the values from a dataframe of intersections.
    :param dataframe: a dataframe containing all data
    :param variables: a list of variables
    :param a_max_variable: the maximum variable
    :return: standardised intersection values in a dataframe
    """
    dataframe_intersections = pd.DataFrame([intersection(dataframe[a_max_variable], dataframe["Kontantpris"])], [a_max_variable], ["Skæringer"])

    if not len(variables) <= 0:
        for variable in variables:
            dataframe_intersections.loc[variable] = intersection(dataframe[variable], dataframe["Kontantpris"])
            dataframe_intersections_standardised = standardisation(dataframe_intersections)
        return dataframe_intersections_standardised.at[a_max_variable, "Skæringer"]
    else:
        return dataframe_intersections.at[a_max_variable, "Skæringer"]

def standardised_slopes(dataframe, variables):
    """
    Finds the slopes of a dataframe and standardises them
    :param dataframe: a dataframe containing all data
    :param variables: a list of variables
    :return: standardised slope values in a dataframe
    """

    subset_price = dataframe.loc[:, "Kontantpris"]

    slopes = []
    for variable in variables:
        subset_variable = dataframe.loc[:, variable]
        slopes.append(slope(subset_variable, subset_price))

    dataframe = pd.DataFrame(slopes, variables, ["Hældninger"])

    if not len(variables) <= 1:
        return standardisation(dataframe)
    else:
        return dataframe

def residual(dataframe, dataframe_slopes, niveau = 1):
    """
    Find the residual and other important information
    :param dataframe: a dataframe containing all data
    :param dataframe_slopes: a dataframe of slopes
    :param niveau: counter for how many times the function has run (default is 1)
    :return: a dict of dataframes and a dict of information including the residual
    """
    name_a = "a_" + str(niveau)
    name_a_max = "a_" + str(niveau) + "_max"
    name_b = "b_" + str(niveau)

    final_variables_dict = {}
    a_dataframes = {}

    variables = []
    for key in dataframe_slopes.index:
        variables.append(key)

    a_max, a_max_variabel = find_max(dataframe_slopes)
    # trække hældning for a_max_variabel ud af dataframe_slopes og overskrive a_max med den nye værdi
    # a_max er den standardiserede hældning, når den kommer ud af find_max
    a_max = ...
    variables.remove(a_max_variabel)

    b = standardised_intersection(dataframe, variables, a_max_variabel)

    final_variables_dict[name_a] = a_max_variabel
    final_variables_dict[name_a_max] = a_max
    final_variables_dict[name_b] = b

    dataframe_a = dataframe.loc[:, a_max_variabel]
    dataframe_a = dataframe_a.mul(a_max)
    dataframe_a = dataframe_a.add(b)

    a_dataframes[name_a] = dataframe_a

    dataframe_y2 = pd.DataFrame(data=dataframe.loc[:, "Kontantpris"].sub(dataframe_a), columns=["Kontantpris"])
    dataframe2 = pd.concat([dataframe_y2, dataframe.loc[:, variables]], axis=1, sort=False)

    new_slopes = standardised_slopes(dataframe2, variables)
    niveau2 = niveau + 1

    final_variables_dict["dataframe_y{}".format(niveau)] = dataframe_y2

    if len(variables) >= 1:
        final_variables_dict2, a_dataframes2 = residual(dataframe2, new_slopes, niveau2)
        final_variables_dict.update(final_variables_dict2)
        a_dataframes.update(a_dataframes2)

        if niveau == 1:
            last_residual = dataframe["Kontantpris"]
            for key in a_dataframes:
                new_residual = last_residual - a_dataframes[key]
                last_residual = new_residual

            clean_residual = last_residual.dropna()
            final_variables_dict["residual"] = clean_residual

    return final_variables_dict, a_dataframes