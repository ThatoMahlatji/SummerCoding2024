# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:41:41 2024

@author: tjmah
"""

# https://www.data-to-viz.com/

import pandas as pd
import matplotlib.pyplot as plt

"""Scatter plot"""

file = pd.read_csv("C:/Users/tjmah/Documents/CodingSummerSchool_2024/Day2/css2024_day2/data_02/iris.csv")

file["class"] = file["class"].str.replace("Iris-","")

#x_scatter = file["sepal_length"]
#y_scatter = file["sepal_width"]

setosa = file[file['class'] == "setosa"]
x_scatter_setosa = setosa["sepal_length"]
y_scatter_setosa = setosa["sepal_width"]

setosa = file[file['class'] == "versicolor"]
x_scatter_versicolor = setosa["sepal_length"]
y_scatter_versicolor = setosa["sepal_width"]

setosa = file[file['class'] == "virginica"]
x_scatter_virginica = setosa["sepal_length"]
y_scatter_virginica = setosa["sepal_width"]

plt.figure()
plt.scatter(x_scatter_setosa,y_scatter_setosa)
plt.scatter(x_scatter_versicolor,y_scatter_versicolor)
plt.scatter(x_scatter_virginica,y_scatter_virginica)
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.legend(["setosa","versicolor","virginica"])

plt.show()

"""Bar graph"""
plt.figure()
plt.bar(file["class"], file["sepal_length"])
plt.show()

"""Pie chart"""


plt.pie([15,35,45,5], labels = ["A","B","C","D"])
plt.show()


