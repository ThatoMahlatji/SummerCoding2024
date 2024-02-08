# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import os
#os.chdir("G:\My Drive\Seminars\CHPC summer school")

#%%
# Import the data
animals = pd.read_csv('super-animals.csv')

#%%
# Obtain the variable names included in the data set
list(animals)

# Obtain the number of observations
animals.shape[0]

# Obtain the number of columns
animals.shape[1]

# Draw a histogram for the size of the animals
axis = sns.histplot(data = animals, x = "Size")
axis.set(ylabel = "Frequency")
plt.show()

#%%
# Recode the vulnerability column
# 1 - Critically endangered (CR)
# 2 - Vulnerable (VU)
# 3 - Near Threatened (NT)
# 4 - Least Concern (LC)
recode_dict = {1: "CR",
               2: "VU",
               3: "NT",
               4: "LC"}

animals["Vulnerability"] = animals["Vulnerability"].map(recode_dict)

#%%
# Which animal species are included in the data set?
# Make a frequency table
species = animals["Species"].value_counts()

# Calculate the proportions in the frequency table
species_proportions = animals["Species"].value_counts(normalize = True)

# Draw a barplot of the animal species included in the data set.
sns.barplot(x=species.index, y=species.values)

#%%
# Create a data set that only contains the birds (subset)
birds = animals.loc[animals["Species"] == "Bird", :]

# Create a frequency table of the vulnerability indices of the birds.
birds_vulnerability = birds["Vulnerability"].value_counts()

# Draw a barplot of the vulnerability indices of the birds.
sns.barplot(x=birds_vulnerability.index, y=birds_vulnerability.values)

# Sort the vulnerability index
birds_vulner_sorted = birds_vulnerability.reindex(["CR", "VU", "NT", "LC"])

sns.barplot(x=birds_vulner_sorted.index, y=birds_vulner_sorted.values)

#%%
# Obtain a quick summary of the size of the birds
summary = birds["Size"].describe()

# Average size of the birds
birds["Size"].mean()
summary["mean"]

# Minimum size of the birds
birds["Size"].min()
summary["min"]

# Maximum size of the birds
birds["Size"].max()
summary["max"]

# Standard deviation of the size of the birds
birds["Size"].std()
summary["std"]

#%%
# Draw a histogram for the size of the birds
sns.histplot(data = birds, x = "Size")

# Draw a boxplot for the size of the birds
sns.boxplot(data = birds, x = "Size")

#%%
# Median of the size of the birds
birds["Size"].median()
summary["50%"]

# Interquartile range of the size of the birds
summary["75%"] - summary["25%"]

#%%
# Draw a scatterplot of the size vs the weight of the birds
sns.scatterplot(data = birds, x = "Size", y = "Weight")

#%%
# Do a log transformation on the size and the weight of the birds
birds_log_size = np.log(birds["Size"])
birds_log_weight = np.log(birds["Weight"])

# Draw a scatterplot
sns.scatterplot(x = birds_log_size, y = birds_log_weight)

#%%
## EXTRA: EXPLORING NUMERICAL DATA ACROSS CATEGORIES

# Subset the birds and the mammals
birds_mammals = animals.loc[animals["Species"].isin(["Bird","Mammal"]), :]

# Draw a side-by-side boxplot
sns.boxplot(data = birds_mammals, x = "Size", y = "Species")



