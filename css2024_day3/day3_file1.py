# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:44:15 2024

@author: tjmah
"""

"""Site for plotting"""
# https://www.data-to-viz.com/

import matplotlib.pyplot as plt

react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]

plt.figure()
plt.plot(temp,react_conv)
plt.xlabel("Temperature ($^o$C)")
plt.ylabel("Reaction conversion")
plt.title("Chemical experiment")

plt.show()

"""Write to html"""
import plotly.express as px

fig = px.line(x=temp,y=react_conv)

fig.write_html("plot.html")

"""Bar plot"""

day1_attendees = [70, 20, 64, 90, 80]
day1_names = ["blessing", "mali", "pangi", "tafi", "shini"] 

plt.figure()
plt.bar(day1_names,day1_attendees)
plt.xlabel("Names")
plt.ylabel("Marks (%)")
plt.title("Day 1 lecture")
plt.show()


"""Scatter plot"""

x_scatter = [1,2,3,4,5]
y_scatter = [2,4,6,9,10] 

plt.figure()
plt.scatter(x_scatter,y_scatter)
# plt.xlabel("Names")
# plt.ylabel("Marks (%)")
# plt.title("Day 1 lecture")
plt.show()


x_histograms = [1,5,9,6,2,5,8,5,3,6,8,9,6,3,6,7,6]
plt.hist(x_histograms)
plt.show()




"""Plotly"""


# Line graphs

import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.write_html("plot.html")





