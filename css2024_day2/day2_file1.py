# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:53:27 2024

@author: tjmah
"""

# Link to Pandas Documentation
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

import pandas as pd

# Read files in a different location
#df = pd.read_csv("data_02/iris.csv")

# Read from a URL
#df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")


column_names = ["sepal_length","sepal_width","petal_length","petal_width","class"]

# Add column names
df = pd.read_csv("data_02/iris.csv", header=None, names=column_names)
#print(df)

# Text file
file_text = pd.read_csv("data_02/Geospatial Data.txt", sep=";")

# Excel file
file_excel = pd.read_excel("data_02/residentdoctors.xlsx")

# Jason file
file_jason = pd.read_json("data_02/student_data.json")


# url
# url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

# file_url = pd.read_csv(url)

# print(file_url.info())
# print(file_url.describe())

# Vibration data

column_names = ["date_time", "x", "y", "z"]
file_vibration = pd.read_csv("data_02/Accelerometer_data.csv", names=column_names)

# Remove index column (if data contains index column)
df_country = pd.read_csv("data_02/country_data_index.csv",index_col=0)


# Resident doctors
file_excel = pd.read_excel("data_02/residentdoctors.xlsx")

"""Regular Expressions"""
file_excel["LOWER_AGE"] = file_excel["AGEDIST"].str.extract('(\d+)-')
file_excel["LOWER_AGE"] = file_excel["LOWER_AGE"].astype(int)
#print(file_excel.info())


"""Working with dates"""
df_dates = pd.read_csv("C:/Users/tjmah/Documents/CodingSummerSchool_2024/Day2/css2024_day2/data_02/time_series_data.csv", index_col=0)

#df_dates["Date"] = pd.to_datetime(df_dates["Date"])

# Add format
df_dates["Date"] = pd.to_datetime(df_dates["Date"], format="%Y-%m-%d")

#print(df_dates.info())

# Extract Year, Month, Day

df_dates['Year'] = df_dates['Date'].dt.year
df_dates['Month'] = df_dates['Date'].dt.month
df_dates['Day'] = df_dates['Date'].dt.day
df_dates['Time'] = df_dates['Date'].dt.time



"""Patient data"""
df = pd.read_csv("data_02/patient_data_dates.csv", index_col=0)

df.drop(index=26, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])#, format="%Y-%m-%d")

# Fill in missing with average
avg_cal = df['Calories'].mean()
df["Calories"].fillna(avg_cal, inplace=True)


"""Best practices"""

df.dropna(inplace=True)
df = df.reset_index(drop=True)

# Replace with average

#df['Duration'] = df['Duration'].replace([450], 0)
#avg_cal = df["Duration"].mean()
#df["Duration"] = df['Duration'].replace([0], avg_cal)

df.at[7, 'Duration'] = 0
avg_cal = df["Duration"].mean()
df.at[7, 'Duration'] = avg_cal


#df = pd.read_csv("data_02/iris.csv")

#----------------------------------------------------------------------

column_names = ["sepal_length","sepal_width","petal_length","petal_width","class"]
df = pd.read_csv("data_02/iris.csv")#, header=None, names=column_names)
col_names = df.columns.tolist()
print(col_names)

df["sepal_length_sq"] = df["sepal_length"]**2
# Or 
#df["sepal_length_sq"] = df["sepal_length"].apply(lambda x:x**2)


grouped = df.groupby("class")

mean_square_values = grouped['sepal_length_sq'].mean()
print(mean_square_values)


#--------------------------------------------------------------------
"""Working with multiple files"""

df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")

df = pd.concat([df1,df2], ignore_index=True)



"""Working with files that have different column"""
df1 = pd.read_csv("data_02/person_education.csv")
df2 = pd.read_csv("data_02/person_work.csv")

df_merge_inner = pd.merge(df1,df2, on="id")#, how="outer")


#-------------------------------

column_names = ["sepal_length","sepal_width","petal_length","petal_width","class"]
df = pd.read_csv("data_02/iris.csv")

df["class"] = df["class"].str.replace("Iris-","")


"""Filter"""

df = df[df['sepal_length'] > 5]
df = df[df["class"] == "virginica"]


#=--------------------------------------------

"""Write to file"""
df.to_csv("iris_clean.csv")

#-----------------------
url = "https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv"

df = pd.read_csv(url)

