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

def haeldning(dataframe1, dataframe2):
    """
    :param dataframe1: variabel x
    :param dataframe2: variabel y
    :return: hældningen
    """
    power = dataframe1.pow(2)
    mul = dataframe1.mul(dataframe2)
    n = len(dataframe1)

    return int((n * mul.sum() - dataframe1.sum() * dataframe2.sum()) / (n * power.sum() - (dataframe1.sum()**2)))

"""
Input: Usorteret liste af hældninger

aritmetisk_middelværdi(hældningsliste):

  return sum(hældningsliste))/(len(hældningsliste)

Output: Middelværdi (et tal)
"""

def aritmetisk_middelvaerdi(list1):
    return