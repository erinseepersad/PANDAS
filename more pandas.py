# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:03:38 2023

@author: qercA
"""

import numpy as np  
import pandas as pd 
#creating a series by passing a list of values, letting pandas create a default integer index
s= pd.Series([1,3,5,np.nan,6,8])
print(s)
#creating data frames by passing numpy array with a datetime index using date_range() and labeled columns:
dates= pd.date_range('20130101', periods=6)
print(dates)
df= pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
#creating the data Frame by passing a dictionary of objects thats converted into series 
df2 = pd.DataFrame(
        {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
            }
    )
print( df2 )
#the columns have different dtypes
df2.dtypes


# viewing data
df.head() #top row
df.tail(3)# bottom row
df.index
df.columns

#the difference between NumPy and Pandas is that NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column
df.to_numpy()
df2.to_numpy()

#desrcibe shows a quick statistic summary of your data 
df.describe()

#transposing your data 
df.T

#sort by an axis:
df.sort_index(axis=1, ascending= False)

#sort by values:
df.sort_values(by='B')

#Getting
df['A']
#Slicing the rows
df[0:3]
df["20130102":"20130104"]

#selection by label

#cross section using a label 
df.loc[dates[0]]

#multi-axis by label
df.loc[:, ['A','B']]

#label slicing, both endpoints included
df.loc["20130102":"20130104", ["A", "B"]]

#getting a scalar value 
df.loc[dates[0],'A']

#Selection by position 

#select with position of passed integers
df.iloc[3]

#integer slicing 
df.iloc[3:5, 0:2]

#integer positions 
df.iloc[[1,2,4], [0,2]]

#slicing by rows
df.iloc[1:3, :]

#slicing by columns 
df.iloc[:, 1:3]

#value explicitly 
df.iloc[1,1]


#Boolean indexing 
#single columns value
df[df['A']>0]

#boolean condition is met and you select values
df[df>0]

#isin() method for filtering 
df2= df.copy()
df2['E']= ['one','one','two', 'three', 'four', 'three']
print(df2)
df2[df2["E"].isin(["two", "four"])]


#Setting- a ne column automatically aligns the data by the indexes
s1= pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
print(s1)
df['F']= s1

#setting values by label 
df.at[dates[0],'A']=0

#setting values by position
df.iat[0,1]=0

#setting by assigning NumPy array:
df.loc[:,'D']= np.array([5]*len(df))
print(df)

#where operation with setting
df2= df.copy()
df2[df2>0]= -df2
print(df2)

#Missing data
#reindexing allows ypu to change/add/delte the index o n specified axis
df1= df.reindex(index= dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
print(df1)

#DataFrame.dropna() drops any rows that have missing data 
df1.dropna(how='any')

#DataFrame.fillna() fills missing data 
df.fillna(value=5)

#isna() gets the boolean mask where values are nan
pd.isna(df1)

#operations
df.mean()
df.mean(1)

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)
df.sub(s, axis='index')

#Apply
#DataFrame.apply() applies user defined function to the data 
#df.apply(np.cumsum)
#df.apply(lambda x: x.max() - xmin())

#Histogramming 
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
s.value_counts()

#String Methods- make it easy to operate on each element of the array, as in the code snippet below 
s = pd.Series(["A", "C", "B", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s.str.lower()

#concat- easily combining series and DatFrame
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
#break into pieces
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)


#Join
#merge()- enables SQL style join types along specific columns
left = pd.DataFrame({"key": ["ok", "cool"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left)
print(right)
pd.merge(left, right, on='key')

#splitting- the data into groups based on some criteria
#applying- a function to each group indeependently
#combining- the results into a data strucryre 
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

print(df)
df.groupby('A')[['C','D']].sum()

#reshaping- stack- compresses a level in the DataFrames columns 
tuples = list(
    zip(
        ["bar", "bar", "car", "car", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
print(df2)
stacked=df2.stack()
print(stacked)
#with a stacked dataframe the inverse operation of stack is unstack and unstacks the last level
stacked.unstack()
stacked.unstack(1)
stacked.unstack(0)


#pivot tables- pivots a DataFrame specifying the values, index, columns
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["erin", "chicken", "steak", "dumpling", "ice cream", "mochi"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
print(df)
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])


#Time series- helps perform resampling operations during frequency conversion 
rng = pd.date_range("1/1/2012", periods=100, freq="S")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample("5Min").sum()

#series.tz_localize()- localizes a time series to a time zone
rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
ts_utc = ts.tz_localize("UTC")
print(ts_utc)

#convert a timezone aware time series to another time zone
#Series.tz_convert()
ts_utc.tz_convert("US/Eastern")

#converting between time span representations:
rng = pd.date_range("1/1/2012", periods=5, freq="M")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print (ts)
ps = ts.to_period()
ps
ps.to_timestamp()

#converting between period and timestamp
prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9
ts.head()

#categoricals 
df = pd.DataFrame(
   {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
 )

#converting grades to caterogrial data
df["grade"] = df["raw_grade"].astype("category")
df['grade']

#renaming catergoies
new_cat=['good', 'aight', 'bad']
df['grade']= df['grade'].cat.rename_categories(new_cat)

#reorder the cat and add the missing ones
df['grade']= df['grade'].cat.set_catergories(
    ["very bad", "bad", "medium", "good", "very good"]
)
df['grades']

#sorting is per order in cat
df.sort_values(by='grade')

#grouping by a categorical column also shows empty cats
df.groupby('grade').size()


#plot
import matplotlib.pyplot as plt
plt.close('all')
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot();
#plot method is a convenience to plot all of the columns with labels 
df = pd.DataFrame(
     np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
 )
    
df = df.cumsum()
plt.figure();
df.plot();
plt.legend(loc='best');