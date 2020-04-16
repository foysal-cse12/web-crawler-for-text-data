# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:34:21 2020

@author: foysal
"""

import pandas as pd
import numpy as np

df = pd.read_csv('D:\\Genie Internship (final code for learning)\\web crawler for text data\\corona_info.csv',sep= ',')
print('data frame: \n',df)


print('unique Continant list :',df['Continant'].unique())
print('unique Country list :',df['Country'].unique())
#drop the rows where Continant = nan
df = df.dropna(subset=['Continant'])
#print('unique Continant list :',df['Continant'].unique())
#print('unique Country list :',df['Country'].unique())


# =============================================================================
# #convert none values into NaN values for other columns
# #The following line replaces None with NaN:
# #df['column'].replace('None', np.nan, inplace=True)
# df.replace(to_replace=[None], value=np.nan, inplace=True)
# print('after converting none values into NaN: ',df)
# =============================================================================
# =============================================================================
# #convert none values to NaN values
# print('before total deaths: ',df['Total deaths'])
# df['Total deaths'].fillna(value=pd.np.nan, inplace=True)
# print('after total deaths: ',df['Total deaths'])
# =============================================================================


#convert the NaN values into 0 for other columns
df = df.fillna(0)

# =============================================================================
# We have two columns which has catagorical values. The columns are Continant and country.we use label encoding
# to convert the catagorical values to numerical values 
# =============================================================================
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dfle = df #create a new data frame
dfle.Continant = le.fit_transform(dfle.Continant) # fit and transform Continant column
dfle.Country = le.fit_transform(dfle.Country) # fit and transform Continant column
print('after label encoding in Continant and Country columna: \n',dfle)

#check data type of each column before normalize data
dataTypeSeries = dfle.dtypes
print('Data type of each column of Dataframe :')
print(dataTypeSeries)


# =============================================================================
# #Change datatype
# #dfle=dfle.astype(float)
# #dfle['Total Cases']=str(dfle['Total Cases'])
# #dfle['Total Cases'] = dfle['Total Cases'].applymap(float)
# #dfle['Total deaths'] = dfle['Total deaths'].astype(np.float64)
# cols_to_norm = ['Active Cases','Deaths/ 1M pop','New Cases','New deaths','Srious/Critical Cases','Tests/ 1M pop','Tot Cases/1M pop','Total Cases','Total Recovered','Total Tests']
# dfle[cols_to_norm] = dfle[cols_to_norm].astype(np.float64)
# #dfle['Total Cases'] = pd.to_numeric(dfle['Total Cases'], errors='ignore')
# dataTypeSeries = dfle.dtypes
# print('Data type of each column of Dataframe after converting to int :')
# print(dataTypeSeries)
# =============================================================================


# =============================================================================
# apply normalization on numarical data. Here we use Min-Max Normalization
# =============================================================================
# =============================================================================
# 
# cols_to_norm = ['Active Cases','Deaths/ 1M pop','New Cases','New deaths','Srious/Critical Cases','Tests/ 1M pop','Tot Cases/1M pop','Total Cases','Total Recovered','Total Tests']
# 
# from sklearn.preprocessing import MinMaxScaler #if u want to use minmax Scaler
# #from sklearn.preprocessing import StandardScaler # if u want to use StandardScaler
# m_scaler = MinMaxScaler()
# #s_scaler=StandardScaler()
# #m_scaler.fit(df[cols_to_norm])
# dfle['Active Cases'] = m_scaler.fit_transform(dfle['Active Cases'])
# #m_scaler.fit(dfle['Active Cases'])
# #scaled_data=m_scaler.transform(dfle['Active Cases'])
# print('scaled data using Min_Max Scaler: \n',dfle['Active Cases'])
# =============================================================================

#Normalize using pandas

dfle['Active Cases'] = dfle['Active Cases'].apply(lambda v: (v-dfle['Active Cases'].min()) / (dfle['Active Cases'].max()-dfle['Active Cases'].min()))
dfle['Deaths/ 1M pop'] = dfle['Deaths/ 1M pop'].apply(lambda v: (v-dfle['Deaths/ 1M pop'].min()) / (dfle['Deaths/ 1M pop'].max()-dfle['Deaths/ 1M pop'].min()))
dfle['New deaths'] = dfle['New deaths'].apply(lambda v: (v-dfle['New deaths'].min()) / (dfle['New deaths'].max()-dfle['New deaths'].min()))
dfle['Srious/Critical Cases'] = dfle['Srious/Critical Cases'].apply(lambda v: (v-dfle['Srious/Critical Cases'].min()) / (dfle['Srious/Critical Cases'].max()-dfle['Srious/Critical Cases'].min()))
dfle['New Cases'] = dfle['New Cases'].apply(lambda v: (v-dfle['New Cases'].min()) / (dfle['New Cases'].max()-dfle['New Cases'].min()))
dfle['Tests/ 1M pop'] = dfle['Tests/ 1M pop'].apply(lambda v: (v-dfle['Tests/ 1M pop'].min()) / (dfle['Tests/ 1M pop'].max()-dfle['Tests/ 1M pop'].min()))
dfle['Tot Cases/1M pop'] = dfle['Tot Cases/1M pop'].apply(lambda v: (v-dfle['Tot Cases/1M pop'].min()) / (dfle['Tot Cases/1M pop'].max()-dfle['Tot Cases/1M pop'].min()))
dfle['Total Cases'] = dfle['Total Cases'].apply(lambda v: (v-dfle['Total Cases'].min()) / (dfle['Total Cases'].max()-dfle['Total Cases'].min()))
dfle['Total Recovered'] = dfle['Total Recovered'].apply(lambda v: (v-dfle['Total Recovered'].min()) / (dfle['Total Recovered'].max()-dfle['Total Recovered'].min()))
dfle['Total Tests'] = dfle['Total Tests'].apply(lambda v: (v-dfle['Total Tests'].min()) / (dfle['Total Tests'].max()-dfle['Total Tests'].min()))

print('new data info after normalize: \n',dfle)





