# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:06:33 2024

@author: tjmah
"""
import pandas as pd

df = pd.read_csv("movie_dataset.csv", index_col=0)

""" Deal with missing values by replacing with the mean"""
# Fill in missing with average
avg_cal = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(avg_cal, inplace=True)
# Fill in missing with average
avg_cal = df["Metascore"].mean()
df["Metascore"].fillna(avg_cal, inplace=True)

print(df.info())
#print(df.describe())

print("\n-------Question 1--------")

print("highest rating = ", df['Rating'].max() )
print("highest rated movie in the dataset: ",
      df[df['Rating'] == df['Rating'].max()]["Title"])

print("\n-------Question 2--------")

print("Average revenue = ", df["Revenue (Millions)"].mean())

print("\n-------Question 3--------")

year_2015_17 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
print("Average revenue of movies from 2015 to 2017 = ",
      year_2015_17["Revenue (Millions)"].mean())

print("\n-------Question 4--------")

print("No. of movies released in the year 2016 = ", (df[df['Year'] == 2016].count())["Title"])

print("\n-------Question 5--------")

print("No. of movies directed by Christopher Nolan = ", (df[df['Director'] == "Christopher Nolan"].count())["Title"])

print("\n-------Question 6--------")

print("No. of movies that have a rating of at least 8.0 = ", (df[df['Rating'] >= 8.0].count())["Title"])

print("\n-------Question 7--------")

print("Median rating of movies directed by Christopher Nolan = ", (df[df['Director'] == "Christopher Nolan"]["Rating"]).median())

print("\n-------Question 8--------")

print("average ratings = \n",(df.groupby('Year')['Rating'].mean()))

print("\n-------Question 9--------")

year_list = (df.groupby('Year')["Year"].count())

print("Percentage increase in number of movies made between 2006 and 2016 = ",
      ((year_list[2016] - year_list[2006]) / year_list[2006])*100)

print("\n-------Question 10--------")

actors = []

for i in range(len(df.index)):

    actor_list = df["Actors"][i+1].split(", ")

    for j in actor_list:
        actors.append(j)

df_actors = pd.DataFrame(actors, columns=["Actors"])

print("Most common actor in all the movies = ",(df_actors.groupby("Actors")["Actors"]).count().sort_values().tail(1))

print("\n-------Question 11--------")

genre = []
for i in range(len(df.index)):

    genre_list = df["Genre"][i+1].split(",")

    for j in genre_list:
        genre.append(j)

df_genre = pd.DataFrame(genre, columns=["Genre"])
df_genre_sorted = (df_genre.groupby("Genre")["Genre"]).count().sort_values()
count = df_genre_sorted.count()

print("unique genres are there in the dataset = ", count)

print("\n-------Question 12--------")

# Pandas - Data Correlations
cor = df[df.columns[5:]]
cor_info = cor.corr()

from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Profiling Report")

profile.to_file("profiling_report.html")

