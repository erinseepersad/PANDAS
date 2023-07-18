# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:35:47 2023

@author: qercA
"""

import pandas as pd
#1
a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar['y'])

#2
#colum first 

data = {"calories": [420, 380, 390],"duration": [50, 40, 45]}

#data into a DataFrame:
df = pd.DataFrame(data)

print(df) 

# you can refer to the row index
print(df.loc[0])
# or even more than one row at a time
print (df.loc[[0,1]])

#how to name each row aka the index
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
# you can locate specific ones using the index 
print(df.loc['day 2'])

#to get the entire DataFrame
df.to_string()

#replace empty values 
df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

#replace only specified columns 
df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)

#Insert the correct argument to make sure that the changes are done for the original DataFrame instead of returning a new one.
df.dropna(inplace=True )

#removed duplicates 
df.drop_duplicates(inplace = True)

#show the relationship between the columns
df.corr()

#Insert the correct syntax for specifying that the plot should be of type 'scatter'.
df.plot(kind='scatter', x = 'Duration', y = 'Calories')
# for histogram
kind='hist'