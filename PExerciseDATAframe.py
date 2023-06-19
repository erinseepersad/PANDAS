# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print(5+5)

import pandas as pd
# data frames- tables Exercise 1
pd.DataFrame({'Apples': [30], 'Bananas': [21]})
#exercise 2- indexes aka row names 
pd.DataFrame({'Apples': [35,41], 'Bananas': [21,34]},
            index= ['2017 Sales', '2018 Sales'])
#exercise 3- series(lists)
pd.Series([4,1,2,1], index=['Flour', 'Milk','Eggs','Spam'], name= 'Product A')
 #need to add measurements for the cups and change the dtype
#fixed
data = {'Flour': '4 cups',
        'Milk': '1 cup',
        'Eggs': '2 large',
        'Spam': '1 can'}

serieslist = pd.Series(data, name='Dinner')
print(serieslist)
