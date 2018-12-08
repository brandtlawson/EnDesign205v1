import pandas as pd
import numpy as np
from sklearn import linear_model


def getIndex(lst, itm):

    idx = 0
    for item in lst:
        if itm != item:
            idx +=1
        else:
            return idx

# read in the data
Combined_Values = pd.read_csv(r'Combined_Values.csv')

# getting data in a range where we have data from all columns
Combined_Values = Combined_Values.drop(Combined_Values.index[0:9])  # gets rid of first N/A
Combined_Values = Combined_Values.drop(Combined_Values.index[1000:17989])  # gets rid of last N/A
Combined_Values.index = pd.DatetimeIndex(end=pd.datetime.today(), periods=len(Combined_Values), freq='1D')

feats = list(Combined_Values.columns.values)[7:]
A = Combined_Values.values
dates = Combined_Values['Date']
dates = dates[::-1]
A = A[::-1]  # this is needed to reverse the order of the data so that the oldest data is read and plotted first!
y = A[:, 5]


y = y.reshape(-1, 1)
x = A[:, [7, 8, 9, 10, 11]]
x = x.reshape(-1, 5)
index = 1
numberPossibleFeatures = 5
answerMatrix = []
inters = []

# used to generate all possible combinations the user can input
# *** we did come up with an iterative solution but was not implemented due to time... see permute.py

iter = 0
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    if a + b + c + d + e != 0:
                        binaryArray = [a, b, c, d, e]
                        # print(binaryArray)
                        individualMatrix = []
                        while (iter < numberPossibleFeatures):
                            # print(iter)
                            if binaryArray[iter] == 1:
                                individualMatrix.append(x[:, iter].reshape(-1, 1))
                            iter += 1

                        iter = 0
                        index += 1

                        NIM = np.array(individualMatrix)
                        NIM2 = np.squeeze(NIM)
                        NIM2 = np.transpose(NIM2)

                        if a + b + c + d + e == 1:
                            NIM2 = np.reshape(NIM2, (-1, 1))

                        reg = linear_model.LinearRegression()
                        reg.fit(NIM2, y)

                        inters.append(reg.intercept_[0])
                        answerList = [0] * 5  # [0][0][0][0][0]
                        iter2 = 0
                        coefNum = 0
                        while (iter2 < numberPossibleFeatures):
                            if binaryArray[iter2] == 1:
                                answerList[iter2] = reg.coef_[0][coefNum]

                                coefNum += 1
                            iter2 += 1
                        answerMatrix.append(answerList)

print(answerMatrix)
