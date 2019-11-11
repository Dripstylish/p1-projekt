import matplotlib.pyplot as plt
import seaborn as sb

def scatterplot_two_variable(x, y, data):
    plt.plot(x, y, data=data, linestyle="none", marker="o")
    plt.show()
