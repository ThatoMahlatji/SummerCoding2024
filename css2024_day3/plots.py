# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:06:36 2024

@author: tjmah
"""

# https://www.data-to-viz.com/

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/tjmah/Documents/CodingSummerSchool_2024/Day2/css2024_day2/data_02/time_series_data.csv", index_col=0)

df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")


"""Line graph"""
plt.figure()
plt.plot(df["Date"],df["Temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature ($^o$C)")
plt.title("Time series data")

plt.show()

"""Histogram"""
plt.figure()
plt.hist(df["Temperature"])
plt.ylabel("Frequency")
plt.xlabel("Temperature ($^o$C)")
plt.title("Time series data")

plt.show()

"""-------------------------------------"""


