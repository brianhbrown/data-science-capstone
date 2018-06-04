import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data, wb
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import cufflinks as cf

startTime = datetime.datetime(2006, 1, 1) #set start date to Jan 1, 2006
endTime = datetime.datetime(2016, 1, 1) #set end date to Jan 1, 2016

BAC = data.DataReader("BAC", 'quandl', startTime, endTime) #Bank of America Reader
C = data.DataReader("C", 'quandl', startTime, endTime) #CitiBank Reader
GS = data.DataReader("GS", 'quandl', startTime, endTime) #Goldman Sachs Reader
JPM = data.DataReader("JPM", 'quandl', startTime, endTime) #JPMorgan Chase Reader
MS = data.DataReader("MS", 'quandl', startTime, endTime) #Morgan Stanley Reader
WFC = data.DataReader("WFC", 'quandl', startTime, endTime) #Wells Fargo Reader

tickers = ["BAC", "C", "GS", "JPM", "MS", "WFC"] #create a list of ticker symbols
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers) #create a data frame with banks as columns and dates as index
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

print(bank_stocks.head())
print()

print(bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()) #What is the max Close for each Bank?
print()

returns = pd.DataFrame() #Create a new data frame for stock returns

for i in tickers: #loops through each stock and adds the return calculation to the returns frame
    returns[i + " Return"] = bank_stocks[i]["Close"].pct_change()
print(returns.head()) #prints the head of the returns data frame
print()

#sns.pairplot(returns[1:])#create a pairplot for the returns of every stock
#plt.show()

print(returns.idxmin()) #Worst single day performance
print()
print(returns.idxmax()) #Best single day performance
print()

print(returns.std()) #Standard deviation
print()

print(returns[returns.index.year==2015].std()) #Standard deviation for 2015
print()

# sns.distplot(returns[returns.index.year==2015]["MS Return"].dropna(), color="green", bins=100) #dist plot for MS 2015, needed to drop Nan values
# plt.show()
#
# sns.distplot(returns[returns.index.year==2008]["C Return"].dropna(), color="red", bins=100) #dist plot for C 2008, needed to drop Nan values
# plt.show()

# for i in tickers: #create a line plot of the close for all stocks, add a legend for the stock color, loop method
#     bank_stocks[i]["Close"].plot(label = i, figsize=(12, 4))
# plt.legend()
# plt.show()
#
# bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot() #xs method
# plt.show()

# plt.figure(figsize=(12,6)) #plot BAC rolling 30 day average vs close price
# BAC[BAC.index.year==2008]["Close"].rolling(window=30).mean().plot(label='30 Day Avg')
# BAC[BAC.index.year==2008]["Close"].plot(label='BAC CLOSE')
# plt.legend()
# plt.show()

# sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True) #Heat map for stock Close price correlation
# plt.show()

# sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True) #Clustermap for stock Close price correlation
# plt.show()


