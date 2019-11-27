import matplotlib.pyplot as plt
import seaborn as sb

def scatterplot_two_variable(x, y, data):
    plt.plot(x, y, data=data, linestyle="none", marker="o")
    plt.show()

def check_if_dirty(dataset):
    dirty_instances = 0
    create_headline("Checking for dirty data", 3)
    for dataset_key in dataset.keys():
        full_list_count = Counter(dataset[dataset_key])
        for count_key in full_list_count.keys():
            if count_key == "NaN":
                print(dataset_key + ": {} NA instances".format(full_list_count[count_key]))
                dirty_instances = dirty_instances + full_list_count[count_key]
    create_headline("Found {} dirty variable instances".format(dirty_instances), 1)

def clean_dataset(dataset):
    create_headline("Cleaning data", 1)
    data_cleaned = 0
    # TODO: correct datatypes
    list_to_int = ["Postnr"]
    for key in dataset.keys():
        if key == "Postnr":
            [float(i) for i in dataset[key]]

    # TODO: correct data (handle NA occurences)
    create_headline("Cleaning complete. Cleaned {} variables".format(data_cleaned), 2)
    return dataset

def count_occurences(dataset):
    create_headline("Counting occurences in lists in dataset", 1)
    for key in dataset.keys():
        print(key + ": ", Counter(dataset[key]))
    create_headline("Counting complete", 0)

def create_headline(text, newline):
    symbol = "-"
    amount = 5
    symbols = symbol*amount
    if newline == 0:
        print(symbols + " " + text + " " + symbols)
    elif newline == 1:
        print("\n" + symbols + " " + text + " " + symbols)
    elif newline == 2:
        print(symbols + " " + text + " " + symbols + "\n")
    else:
        print("\n" + symbols + " " + text + " " + symbols + "\n")

"""
    create_headline("Importing CSV file", 0)
    with open(csv_file_path, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        create_headline("Creating CSV dictionary", 0)

        row_count = 0
        labels = True
        for row in csv_reader:
            if labels:
                csv_dict = {}
                for label in row:
                    csv_dict[label] = []
                labels = False
            else:
                for key in row.keys():
                    list = csv_dict[key]
                    list.append(row[key])
                    csv_dict[key] = list
                row_count = row_count + 1
                if row_count > 10:
                    break
"""

from pylab import*
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from pandas import DataFrame

HD = pd.read_csv('home/HOME.csv', delimiter=';')

HD.set_index('EjdType',inplace=True)
HD_Villa1=HD.loc[['Villa, 1 fam.']].dropna(subset=['Grundareal'])
HD_Ejerlejlighed=HD.loc[['Ejerlejlighed']]
HD_Raekkehus=HD.loc[['Raekkehus']]

'''
def lin_reg_plot(df,x_label,y_label,xlim1,xlim2):
    X = df[x_label].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = df[y_label].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y)  # perform linear regression
    Y_pred = linear_regressor.predict(X)  # make predictions
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.xlim(xlim1,xlim2)
    r_sq = ('coefficient of determination',linear_regressor.score(X, Y))
    slope = ('slope:', linear_regressor.coef_)
    plt.text(1.1,15000000,r_sq, fontsize=12, bbox={'facecolor':'yellow','alpha':0.2})
    plt.text(1.1, 10000000, slope, fontsize=12, bbox={'facecolor': 'yellow', 'alpha': 0.2})
    return plt.show()
lin_reg_plot(HD_Ejerlejlighed,'Boligareal','Kontantpris',0,500)


a_k = (sum(y,0) * (sum(x_k)^2,0) - (sum(x_k,0))(sum(x_k*y)))/(n(sum(x_k^2,0)) - (sum(x_k,0)^2)


'''''''
variabler=HD.loc[:,['Kontantpris','Liggetid','Alder','Boligareal','Grundareal']]
def iteration_of_slope(df):
    slopes=[]
    for i in range(len(df.columns)-1):
        y=df.iloc[:,[1,1]]
        x=df.iloc[:, [i + 1, i + 1]]
        subset = {'variable':[x],'pris':[y]}
        subdata=DataFrame(subset,columns= ['variable','pris'])
        n=len(x)
        slopes.append((sum(subdata.pris) * (sum(subdata.variable)**2) - (sum(subdata.variable))(sum(subdata.variable * subdata.pris))) /
                      (n*(sum(subdata.variable**2)) - (sum(subdata.variable)**2)))
    return slopes

iteration_of_slope(variabler)
'''
variabler=HD.loc[:,['Kontantpris','Liggetid','Alder','Boligareal','Grundareal']]
y=variabler.loc[:,['Kontantpris', 'Liggetid']]
x=variabler.loc[:, ['Liggetid']]
subset = {'variable':[x],'pris':[y]}
subdata=DataFrame(subset, columns= ['variable','pris'])
print(subdata)