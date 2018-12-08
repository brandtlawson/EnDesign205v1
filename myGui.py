import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import coeffCals as cc
import linkTest2 as lt2

# ***********************************************************************************************************************************
# ***********************************************************************************************************************************
# THE OBJECT-ORIENTED LOGIC AND SETUP FOR THE GUI WAS ADOPTED FROM PYTHON'S OPEN SOURCE TUTORIALS
# https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/?completed=/tkinter-depth-tutorial-making-actual-program/
# ***********************************************************************************************************************************
# ***********************************************************************************************************************************



# import coeffecients and y intercepts from seperate file
coeffMat = cc.answerMatrix
inters = cc.inters

# set scheme and global vars
LARGE_FONT = ("Verdana", 14)
clickedList = []
idxToPlot = []
newPrices = []
numDays = -1
cb = []

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


class StockPredictGUI(tk.Tk):

    # initialize the page
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Stock Predictor GUI")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        frame = StartPage(container, self)

        frame.grid(row=0, column=0, sticky="nsew")

        frame.tkraise()
        frame.configure(background='#F0F8FF')




class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        def isFloat(x):
            try:
                x = float(x)
                return True
            except:
                return False

        def isInt(x):
            try:
                x = int(x)
                return True
            except:
                return False


        # ***************************************************************************************
        # given the number of days, want to display predicted prices in the text boxes
        # to get the predicted prices run lt2.fitFunc then return the last value in forecast
        # update the entries[i] text field
        # ***************************************************************************************

        # predPrices is called when the used does not change any of the feature prices
        def predPrices(frame, cbV, cbT, ent, days, plbl):

            numDays = int(days.get())
            np = []

            # make sure user entered in number of days
            if(isInt(numDays)):
                detailLabel['text']= 'Here are the prices in '+str(numDays)+' days from now:'
                # iteratively calculate and append the predicted prices
                for idx in cbT:
                    np.append(lt2.fitFunc(lt2.Combined_Values[idx], numDays)[0])
                for i in range(len(ent)):
                    ent[i].delete(0, tk.END)
                    ent[i].insert(0, round(np[i], 4))

            # plot the data
            plotData = lt2.fitFunc(lt2.Combined_Values['Close'][::-1], numDays)
            plbl['text'] = "The predicted price of the S&P500 in "+str(numDays)+" days is "+str(round(plotData[0], 4))
            plt.plot(plotData[1], plotData[2], label="Historical Price")
            plt.plot(plotData[3], plotData[4], label="Forcasted S&P Price")
            plt.xticks([50, 250, 450, 650, 850, 1050], ('2014', '2015', '2016', '2017', '2018', '2019'))
            plt.xlabel("Time")
            plt.ylabel("Price")
            plt.legend()
            plt.show()

        # allFeats is called when the used changes the prices of features
        # called by fewFeats and returns the predicted value based on input by user.
        def allFeats(curP):
            coeffs = []
            intercept = []
            likeParts = 0

            # this finds the proper coefficients and intercepts according the the combination
            # of clicked items in the checkbox
            for j in range(len(coeffMat)):
                item = coeffMat[j]
                for i in range(len(item)):
                    if((curP[i] ==  0) and item[i]==0):
                        likeParts +=1
                    if((curP[i]!=0) and item[i] !=0):
                        likeParts +=1
                    if(likeParts == len(item)):
                        coeffs = item
                        intercept = inters[j]
                        break

                if(likeParts == len(item)):
                    break
                else:
                    likeParts = 0

            numAdds = 0
            spP = 0
            for i in range(len(coeffs)):
                if(coeffs[i] !=0):
                    spP += coeffs[i]*curP[i]
                    numAdds +=1


            return float(spP)+float(intercept)


        def fewFeats(frame, cbV, cbT, ent, days, plbl):

            # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            # predict all current prices and get the predicted value
            # then find the predicted value based on the user's input
            # find the difference between the two, then add/subtract the difference to the arima prediction
            # and simply plot a straight line to that value
            # and print the arima prediction n days in the future also on that plot
            # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

            currPrices = []
            for i in range(len(cc.feats)):
                currPrices.append(lt2.Combined_Values[cbTexts[i]].iloc[0])
            # get prediction with change in price
            pred0= allFeats(currPrices)


            givenItems = []
            for item in cbV:
                givenItems.append(item.get())
            # similar to prev function

            coeffs = []
            intercept = []
            likeParts = 0
            for j in range(len(coeffMat)):
                item = coeffMat[j]
                for i in range(len(item)):
                    if((givenItems[i] ==  0) and item[i]==0):
                        likeParts +=1
                    if((givenItems[i]!=0) and item[i] !=0):
                        likeParts +=1
                    if(likeParts == len(item)):
                        coeffs = item
                        intercept = inters[j]
                        break

                if(likeParts == len(item)):
                    break
                else:
                    likeParts = 0

            numAdds = 0
            spP = 0
            for i in range(len(coeffs)):
                userin = float(ent[i].get())
                if(coeffs[i] !=0):
                    spP += coeffs[i]*userin
                    numAdds +=1

            spPred1 = float(spP)+float(intercept)



            # the difference between the predicted price n days ahead and the original prediction
            diff = float(spPred1 - float(pred0))

            plotData = lt2.fitFunc(lt2.Combined_Values['Close'][::-1], int(days.get()))
            armPredVal = plotData[0]

            # find the diff between arima and regression
            fixPred = float(armPredVal) + diff

            plbl['text'] = "The predicted price of the S&P500 in "+days.get()+" days is "+str(round(fixPred, 4))

            # These two lines plot the arima plot
            plt.plot(plotData[1], plotData[2], label="Historical Price")
            plt.plot(plotData[3], plotData[4], label="Forcasted S&P Price")
            #  plot the historical data
            plt.plot([plotData[1][-1], plotData[1][-1]+int(days.get())], [plotData[2].iloc[-1], fixPred], label="Forecast Given User Data")
            plt.xticks([50, 250, 450, 650, 850, 1050], ('2014', '2015', '2016', '2017', '2018', '2019'))
            plt.xlabel("Time")
            plt.ylabel("Price")
            plt.legend()
            plt.show()

        # set up the page
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Let's make a prediction", font=LARGE_FONT)
        label.configure(background="#F0F8FF")
        label.pack(pady=10, padx=10)
        featureLbl = tk.Label(self, text = 'Choose the index you wish to examine', font=("Helvetica", 12))
        featureLbl.configure(background="#F0F8FF")
        featureLbl.pack()
        dropDown = ttk.Combobox(self, values=['S&P 500'])
        dropDown.pack()
        label2 = tk.Label(self,pady='0.2' , text='Enter how many days ahead you would like to predict the price of the S&P 500\n then click predict prices.\n\nOr enter your prediction of the factors in the boxes and click the checkbox\non the chosen items', font=("Helvetica", 12))
        label2.configure(background="#F0F8FF")
        label2.pack()
        detailLabel = tk.Label(self, text='\nHere are the current prices of the indecies with the largest impact on the S&P 500:', font=("Helvetica", 12))
        detailLabel.configure(background="#F0F8FF")
        detailLabel.pack()

        # iteratively create feature labels
        cbTexts = []
        cbVariables = []
        cb.clear()
        entries = []
        for i in range(len(cc.feats)):
            cbTexts.append(cc.feats[i])
            cbVariables.append(tk.IntVar())

            cb.append(tk.Checkbutton(self, text=cbTexts[i], font=("Helvetica", 10), variable=cbVariables[i]))
            entries.append(tk.Entry(self))
            entries[i].insert(0, round(lt2.Combined_Values[cbTexts[i]].iloc[0], 4))
            cb[i].configure(background="#F0F8FF")
            cb[i].pack()
            entries[i].pack(pady='0.2')

        dayLbl = tk.Label(self, text='Specify number of days ahead', font=("Helvetica", 12))
        dayLbl.configure(background="#F0F8FF")
        dayLbl.pack()
        daysBtn = tk.Entry(self)
        daysBtn.pack()

        sp5PriceLbl = tk.Label(self, text="The current price of the S&P 500 is:  "+str(round(lt2.yvals.iloc[-1], 4)), font=("Helvetica", 12))
        sp5PriceLbl.configure(background="#F0F8FF")
        sp5PriceLbl.pack()

        button2 = ttk.Button(self, text="Predict Features",
                             command=lambda: predPrices(self, cbVariables, cbTexts, entries, daysBtn, sp5PriceLbl))
        button2.pack()

        button4 = ttk.Button(self, text="Predict Index", command=lambda : fewFeats(self, cbVariables, cbTexts, entries, daysBtn, sp5PriceLbl))
        button4.pack(pady=0.5)


app = StockPredictGUI()
app.mainloop()