import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer


# collect the data

# excel_file = r"Combined_Values.csv"
Combined_Values = pd.read_csv(r"Combined_Values.csv")
spCommData = pd.read_csv(r"comSP.csv")

X = spCommData.drop(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'USD to EUR', 'Volume', 'GDP', 'NonFarm Payroll', '3 month Libor', 'Unemployment', 'MILKBFP3', 'LH1', 'BCOMXAL', 'VIX', 'DJUS', 'DJUSRE', 'DJUSCL', 'DL1', 'NG1', 'CO1'], axis=1)
# X = spCommData['OC1']
y = spCommData['Close']
y = y.reset_index()
y = y['Close']
X = X.iloc[:9900, :]
y = y.loc[:9899]
X = X.reset_index()

# print(X.head())
# print(y.head())
# print(X.columns.values[1:])

feats = X.columns.values[1:]




Combined_Values = Combined_Values.drop(Combined_Values.index[0:9]) #gets rid of first N/A
Combined_Values = Combined_Values.drop(Combined_Values.index[1000:17989]) #gets rid of last N/A
Combined_Values.head()
xvals = Combined_Values['Date']
yvals = Combined_Values['Close']
# Combined_Values.plot(kind='scatter',x='Date',y='Close',color='red')
# plt.show()
