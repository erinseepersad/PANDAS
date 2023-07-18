# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:38:39 2023

@author: qercA
"""
#practice problems I found online

#write a pandas program to create and display a one dimensional array like object containing an array of data 
import pandas as pd
"""
myarray= pd.Series(['hi', 'my','name',' is','erin'])
print(myarray)

#write a pandas program to convert a Panda module series to a python list and its type 
myarray= pd.Series(['hi', 'my','name',' is','erin'])
#myarray= pd.Series([1, 2,3,4,5])
print('before:', type(myarray))
#converting to a list 
print('converting to a list...')
print(myarray.tolist())
print('after:', type(myarray.tolist))

#write a pandas program to add, subtract, multiple and divide 2 series
problem1= pd.Series([2,4,6,8,10]) 
problem2= pd.Series([1,3,5,7,9])
sumofproblems= problem1 + problem2
print(sumofproblems)
#problem3= (problem2.add,problem1.add)
#print(problem3)
subofproblems= problem1-problem2
print(subofproblems)
multiofproblems= problem1*problem2
print(multiofproblems)
diviofproblems= problem1/problem2
print(diviofproblems)
# another way 
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])
df = pd.DataFrame({'series1': series1, 'series2': series2})
addition = df['series1'].add(df['series2'])
print(addition)
subtraction = df['series1'].sub(df['series2'])
print("\nSubtraction:")
print(subtraction)
multiplication = df['series1'].mul(df['series2'])
print("\nMultiplication:")
print(multiplication)
division = df['series1'].div(df['series2'])
print("\nDivision:")
print(division)

# write a pandas program to compare the elements of the two pandas series 
series1= [2,4,6,8,10]
series2=[1,3,5,7,10]
if series1>series2:
    print('Finally!')
else:
    ('dang better luck next time')

#to list:
#DataFrame.tolist()

#to series:
#DataFrame.Series()

#to array
#DataFrame.values()

#write a Pandas program to convert the first column of a DataFrame as a series
sample = {'col1': [1, 2, 3, 4, 7, 11], 
          'col2': [4, 5, 6, 9, 5, 0],
          'col3': [7, 5, 8, 12, 1,11]}
df= pd.DataFrame(sample)
#first column to series 
firstcol= df.iloc[:,0] #: gets the rows the comma represents al rows and 0 is the index we want 
print(firstcol)

#write a program to sort a given series
series= pd.Series(['100', '200', 'python', '300.12', '400'])
new_s = pd.Series(series).sort_values()
print(new_s)


# write a program to convert series of lsits to one series
series = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
s = series.apply(pd.Series).stack().reset_index(drop=True)
print(s)

# write a Pandas program to add some data to an existing Series.
#.concat
existing_series = pd.Series([1, 2, 3])
new_data = pd.Series([4, 5])
updated_series = pd.concat([existing_series, new_data])
# Reset the index of the updated Series
updated_series.reset_index(drop=True, inplace=True)
print(updated_series)

#change the order of index within a series
# .reindex()
series = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
new_order = ['B', 'A', 'C', 'D','E']
reordered_series = series.reindex(new_order)
print(reordered_series)

#mean and sd
s= pd.Series([1,2,3,4,5,6,7,8,9,5,3])
print(s.mean())  
print(s.std())

# write a program to get the items which are not common of the two given series
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
result = sr1[~sr1.isin(sr2)] #~ means NOT
print(result)

#practice with the not function
import pandas as pd
series = pd.Series([True, False, True, False])
updated_series = ~series
print(updated_series)

#Write a Pandas program to get the items which are not common of two given series.
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])
# Get items that are not common between the two series
not_common_items = series1[~series1.isin(series2)].append(series2[~series2.isin(series1)])
#not in 1. append to not in 2.
print(not_common_items)
"""
#OR: THIS IS ANOTHER WAY 
import numpy as np
"""
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print("Original Series:")
print("sr1:")
print(sr1)
print("sr2:")
print(sr2)
print("\nItems of a given series not present in another given series:")
sr11 = pd.Series(np.union1d(sr1, sr2))
sr22 = pd.Series(np.intersect1d(sr1, sr2))
result = sr11[~sr11.isin(sr22)]
print(result)

#. Write program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.
series = pd.Series([10, 20, 30, 40])
# Using describe() function
description = series.describe()
print("Using describe():")
print(description)
# Using individual functions
minimum = series.min()
percentile_25 = series.quantile(0.25)
median = series.median()
percentile_75 = series.quantile(0.75)
maximum = series.max()
print("\nUsing individual functions:")
print("Minimum:", minimum)
print("25th Percentile:", percentile_25)
print("Median:", median)
print("75th Percentile:", percentile_75)
print("Maximum:", maximum)

#Write program to calculate the frequency counts of each unique value of a given series.
count=0
series=[1,1,1,2,4,3,5,8,6,9,9,6]
for num in series:
    if num in series:
        count+=1
        print(count)
counts = {}
series = [1, 1, 1, 2, 4, 3, 5, 8, 6, 9, 9, 6]
for num in series:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
for num, count in counts.items():
   print("{}: {}".format(num, count)) #{} specificies num and count like range
#OR this is another way
series = pd.Series([1, 1, 1, 2, 4, 3, 5, 8, 6, 9, 9, 6])
frequency_counts = series.value_counts()
print(frequency_counts)

#display most frequent value in a given series and replace everything else as ‘Other’ in the series.
#from the website
num_series = pd.Series(np.random.randint(1, 5, [15]))
print("Original Series:")
print(num_series)
print("Top 2 Freq:", num_series.value_counts())
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'
print(num_series)

# program to find the positions of numbers that are multiples of 5 of a given series 
# empty dictonary
# for loop to to look at each number
#% 5==0 
empty= {}
series=pd.Series(np.random.randint(1,10,9))
for num in series:
    if num%5==0 in series:
        print('True')
    else:
        print('False')

#program to extract items at given positions of a given series
def extract_items(series, positions):
    extracted_items = []
    for i in positions:
        if i < len(series):
            extracted_items.append(series[i])

    return extracted_items
#random numbers for an example:
series = [10, 20, 30, 40, 50, 60]
positions = [1, 3, 5] #going to print numbers at that position 

extracted_items = extract_items(series, positions)
print(extracted_items)
#another way I can do it is to make an empty list have the user put 5 random numbers in the list then decide what index it is at
#another way is: this is from the website 
num_series = pd.Series(list('2390238923902390239023'))
element_pos = [0, 2, 6, 11, 21]
print("Original Series:")
print(num_series)
result = num_series.take(element_pos) #.take "Take elements from an array along an axis."
print("\nExtract items at given positions of the said series:")
print(result)

#.iloc:"Select a subset of a DataFrame by labels."
#.loc: "Select a subset of a DataFrame by positions."

#get the positions of items of a given series in another given series.

series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
series2 = pd.Series([1, 3, 5, 7, 9])
extracted_items = series1[series2]
print(extracted_items)
# can use:
#positions = series1[series1.isin(series2)].index.to_list()
#result = [pd.Index(series1).get_loc(i) for i in series2]

# convert the first and last character of each word to upper case in each word of a given series.
def string_capitalize(x):
    def capitalize_word(word):
        if len(word) > 1:
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            new_word = word.upper()
        return new_word

    return x.apply(capitalize_word)

# Example:
series1 = pd.Series(['php', 'python', 'java', 'c#'])
capitalized_series = string_capitalize(series1)
print(capitalized_series)

#series.map: "Map values of Series according to an input mapping or function. Used for substituting each value in a Series with another value, that may be derived from a function"
#lambda: annon. function

#calculate the number of characters in each word in a given series.
series1 = pd.Series(['Php', 'Python', 'Java', 'C#'])
for word in series1:
    count = len(word)
    print(count)

# program to convert a series of date strings to a timeseries.
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("\nSeries of date strings to a timeseries:")
print(pd.to_datetime(date_series))
"""
#get the day of month, day of year, week number and day of week from a given series of date strings.
series1 = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
# Convert strings to datetime objects
dates = pd.to_datetime(series1)

day_of_month = dates.dt.day.tolist()
print(day_of_month)

day_of_year = dates.dt.dayofyear.tolist()
print(day_of_year)

week_number = dates.dt.week.tolist()
print(week_number)

day_of_week = dates.dt.dayofweek.tolist()
print(day_of_week)

# DataFrame to store the results
#result = pd.DataFrame({
 #   'Date': series1,
  #  'Day of Month': day_of_month,
   # 'Day of Year': day_of_year,
    #'Week Number': week_number,
    #'Day of Week': day_of_week
#})

#print(result)
