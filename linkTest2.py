import pandas as pd
from pyramid.arima import auto_arima

# collect the data

Combined_Values = pd.read_csv(r"Combined_Values.csv")
spCommData = pd.read_csv(r"comSP.csv")
dates = spCommData['Date']
# read and format the data
X = spCommData.drop(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'USD to EUR', 'Volume', 'GDP', 'NonFarm Payroll', '3 month Libor', 'Unemployment', 'MILKBFP3', 'LH1', 'BCOMXAL', 'VIX', 'DJUS', 'DJUSRE', 'DJUSCL', 'DL1', 'NG1', 'CO1'], axis=1)
y = spCommData['Close']
y = y.reset_index()
y = y['Close']
X = X.iloc[:9900, :]
y = y.loc[:9899]
X = X.reset_index()

feats = X.columns.values[1:]

Combined_Values = Combined_Values.drop(Combined_Values.index[0:9]) #gets rid of first N/A
Combined_Values = Combined_Values.drop(Combined_Values.index[1000:17989]) #gets rid of last N/A
Combined_Values.head()

xvals = Combined_Values['Date']
xvals = xvals[::-1]

yvals = Combined_Values['Close']
yvals = yvals[::-1]

# takes in the y values to fit, and the number of days to predict to
# returns the final forecasted value, the original x then y vals, then the forcastex x, then y vals
def fitFunc(yvals, ndays):
    model = auto_arima(yvals, trace=True, error_action='ignore', suppress_warnings=True)
    model.fit(yvals)

    n_periods = ndays
    forecast = model.predict(n_periods)
    oned = range(len(yvals), len(yvals) + len(forecast))
    oned2 = range(0, len(yvals))
    return [forecast[-1], oned2, yvals, oned, forecast]
