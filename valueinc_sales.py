#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:34:38 2022

@author: olufunmifalokun
"""
import pandas as pd
# file_name = pd . read-csv(('))
data = pd.read_csv('transaction.csv', sep=';')

data.info()


var1=9
var2 = 'twinsbur
var3 = {'apple','banana','ppear'}
var = True

#working with calculations
#defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#MMathOperations
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction= (SellingPricePerItem - CostPerItem) * NumberOfItemsPurchased

data.info()
#data.info(verbose=True)
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding new column to dataframe
data['CostPerTransaction'] = CostPerTransaction
data['CostPerTransaction'] =  data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalesPertransaction'] =  data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit calculation
# profit = Sales - Cost
# Markup = (Sales - Cost) / Cost
data['ProfitPertransaction'] =  data['SalesPertransaction'] -  data['CostPerTransaction']
data['Markup'] = ( data['SalesPertransaction'] -  data['CostPerTransaction'] ) /  data['CostPerTransaction']

data['Markup'] = data['ProfitPertransaction'] /  data['CostPerTransaction']


#Rounding Markp
roundmarkup = round(data['Markup'],2)
data['Markup']  = round(data['Markup'],2)

#Combining data
my_name = 'Ayo ' + 'Falokun'
my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

#checking columns data type
print(data['Day'].dtype)

#Change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year
data['date']= my_date

#using iloc to view specific columns
data.iloc[0]        #views row with index = 0
data.iloc[0:3]      #first 3 rows
data.iloc[-5:]      #last 5 rows

data.head(5)        #first 5 rows
data.iloc[:,2]      #all rows but first 2 columns
data.iloc[4,2]      #aRow 4, column 2

#using split to split the client keywords

#newvar = column.str.split('sep', expand = True)
split_col = data['ClientKeywords'].str.split(',', expand=True)

#create new columns for clientkeywords
data['ClientAge'] = split_col[0]
data['Clientype'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using replace function, lower function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

data['ItemDescription'] = data['ItemDescription'] .str.lower()


data = pd.merge(data, seasons, on = 'Month')
#drop a few columns
data = data.drop('ClientKeywords', axis = 1  )
data = data.drop('Day', axis = 1  )
data = data.drop(['Year', 'Month'], axis = 1  )

#export into CSV
data.to_csv('ValueInc_Cleaned2.csv', index = False)


new_date  = data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

