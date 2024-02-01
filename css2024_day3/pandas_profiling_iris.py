# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:21:18 2024

@author: tjmah
"""

import pandas as pd
import matplotlib.pyplot as plt

from ydata_profiling import ProfileReport

"""Scatter plot"""

df = pd.read_csv("C:/Users/tjmah/Documents/CodingSummerSchool_2024/Day2/css2024_day2/data_02/iris.csv")

#file["class"] = file["class"].str.replace("Iris-","")


profile = ProfileReport(df, title="Profiling Report")

profile.to_file("report.html")
