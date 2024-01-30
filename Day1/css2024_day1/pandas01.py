# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:50 2024

@author: tjmah
"""

# Documentation = https://pandas.pydata.org/docs/user_guide/io.html#csv-text-files

import pandas

print("---------country_data.csv------------")
file1 = pandas.read_csv("../data_01/country_data.csv")

print(file1)
print("\n")

print("File shape = " + str(file1.shape))

print("\n")
print(file1.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 - integer
 1   Gender   11 non-null     object - string
 2   Country  11 non-null     object - string
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
"""

print(file1.describe())
print("\n")

print("---------iris.csv------------")

file2 = pandas.read_csv("../data_01/iris.csv")

print(file2)
print("\n")

print("File shape = " + str(file2.shape))

print("\n")
print(file2.info())


print(file2.describe())


print("\n")

print("---------diab_data.csv------------")

file3 = pandas.read_csv("../data_01/diab_data.csv")

print(file3)
print("\n")

print("File shape = " + str(file3.shape))

print("\n")
print(file3.info())


print(file3.describe())


print("\n")

print("---------housing_data.csv------------")

column_names = ["1","2","3","4","5","6","7","8","9","10", "11","12","13","14"]

file4 = pandas.read_csv("../data_01/housing_data.csv", names=column_names)

print(file4)
print("\n")

print("File shape = " + str(file4.shape))

print("\n")
print(file4.info())


print(file4.describe())


print("\n")

print("---------insurance_data.csv------------")

file5 = pandas.read_csv("../data_01/insurance_data.csv" , skiprows=5)


print(file5)

print("\n")

print("File shape = " + str(file5.shape))

print("\n")
print(file5.info())


print(file5.describe())

# If data separated by ;
#file = pandas.read_csv("file_name", sep=";")

