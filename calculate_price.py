import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

import math_methods as mm

csv_file_path = "home/HOME.csv"

def import_csv_file():
    csv_file = pd.read_csv('home/HOME.csv', delimiter=';')
    return csv_file


dataset = import_csv_file()