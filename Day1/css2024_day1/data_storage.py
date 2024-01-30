# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:24 2024

@author: tjmah
"""

import pandas

"""
Storing data in Python
1. Lists
2. Dictionaries
3. Data frames - specific to Pandas
"""

print("-----------1. Lists ----------------")
print("\n")

age = [39, 25, 29, 46, 22, 35, 22, 49, 30, 40, 30]
print("Age = ", age)
print("Min age = ", min(age))
print("Max age = ", max(age))
print("Length = ", len(age))
print("Sum = ", sum(age))
print("Average = ", sum(age)/len(age))
print("Range = ", age[0:2])
# Add value
age.append(56)
print("new age = ", age)
# Remove value
age.pop(-1)
print("original age = ", age)
# Insert value
# age.insert(index, object)


gender = ["M","M","F","M","F","F","F","M","M","F","M"]


country = ["South Africa",
           "Botswana",
           "South Africa",
           "South Africa",
           "Kenya",
           "Mozambique",
           "Lesotho",
           "Kenya",
           "Kenya",
           "Egypt",
           "Sudan"]
print("Country = ", country)

print("\n")
print("-----------1. Dictionaries ----------------")
print("\n")

"""
Dictionaries - key:value pairs
- unordered
"""

mammals = {"cat":"a cute animal", 
           "lion":"king of the jungle",
           "elephant":"a gigantic herbivore"}

print("A cat is",mammals["cat"])


print("\n")
print("-----------1. Data frames ----------------")
print("\n")


fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits': fruits,
    'sizes':size_nm
    }


"""
df = dataframe
"""

df = pandas.DataFrame(fruit_sizes)


print("fruits = ", df['fruits'])
print("Sizes = ", df['sizes'])
print(df.describe())

# fruit sizes larger than 10
print(df[df['sizes'] > 10])

# Range of rows to display
print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]


# Add new column data
df['prices'] = prices

# Remove column data
df.drop(columns=["sizes"], inplace=True)

