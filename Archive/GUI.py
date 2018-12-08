from tkinter import *
from tkinter.ttk import *
#Window Creation
window = Tk()
window.title("Stock Anaylsis")
window.geometry('1000x800')

#Window Text
lbl = Label(window, text="Select factors from the dropdownbox to anaylze the effect on the chosen indicator.")
lbl.grid(column=0, row=0)

#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=1)

#Factor 1 Text
lbl = Label(window, text="Factor 1")
lbl.grid(column=0, row=2)

#Combobox Widget
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(0) #set the selected item
combo.grid(column=0, row=3)

#Entry Box Text
lbl = Label(window, text="What is your estimate?")
lbl.grid(column=0, row=4)

#Entry box
txt = Entry(window,width=10)
txt.grid(column=0, row=5)
#puts the cursor into the entry box
txt.focus()





#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=6)

#Factor 2 Text
lbl = Label(window, text="Factor 2")
lbl.grid(column=0, row=7)

#Combobox Widget
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(0) #set the selected item
combo.grid(column=0, row=8)

#Entry Box Text
lbl = Label(window, text="What is your estimate?")
lbl.grid(column=0, row=9)

#Entry box
txt = Entry(window,width=10)
txt.grid(column=0, row=10)
#puts the cursor into the entry box
#txt.focus()






#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=11)

#Factor 3 Text
lbl = Label(window, text="Factor 3")
lbl.grid(column=0, row=12)

#Combobox Widget
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(0) #set the selected item
combo.grid(column=0, row=13)

#Entry Box Text
lbl = Label(window, text="What is your estimate?")
lbl.grid(column=0, row=14)

#Entry box
txt = Entry(window,width=10)
txt.grid(column=0, row=15)
#puts the cursor into the entry box
#txt.focus()







#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=16)

#Chosen Indicator Text
lbl = Label(window, text="Select Indicator")
lbl.grid(column=0, row=17)

#Combobox Widget
combo = Combobox(window)
combo['values']= ('S&P 500', 'Russell 2000', 'DJIA')
combo.current(0) #set the selected item
combo.grid(column=0, row=18)




#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=19)

#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=20)

#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=21)

#Predict for date Text
lbl = Label(window, text="Prediction Date")
lbl.grid(column=0, row=22)

#Entry Box Text
lbl = Label(window, text="What date would you like to predict?")
lbl.grid(column=0, row=23)

#Entry box
txt = Entry(window,width=10)
txt.grid(column=0, row=24)
#puts the cursor into the entry box
#txt.focus()





#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=37)

#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=38)



#Entry Box Text
lbl = Label(window, text="This is where entered goes from last entry spot.... put chart here")
lbl.grid(column=0, row=41)

#Space Text
lbl = Label(window, text=" ")
lbl.grid(column=0, row=40)

#Button
def clicked():
    res = "Entered " + txt.get()
    lbl.configure(text = res)
#def callback():
 #   print ("Button clicked")
btn = Button(window, text="Predict", command=clicked)
btn.grid(column=0, row=39)

window.mainloop()
