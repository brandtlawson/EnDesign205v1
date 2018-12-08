import tkinter as tk
from tkinter import ttk
import linkTest as lt
import matplotlib
matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

LARGE_FONT = ("Verdana", 12)


class StockPredictGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Stock Predictor GUI")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Let's make a prediction", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # tkvar = StringVar(root)
        # dropDownChoices = {'Oats', 'Live Cattle', 'Unemployment'}

        featureLbl = tk.Label(self, text = 'Choose the index you wish to examine')
        featureLbl.pack()

        dropDown = ttk.Combobox(self, values=['SP500', 'Russel 2000'])
        dropDown.pack()

        label2 = tk.Label(self, text='Which features do you think will change?')
        label2.pack()

        # learn to iteratively make the drop down check boxes based off of information from the chosen index
        winSt = {1: 1, 2: 1, 3: 0, 4: 0}
        cbTexts = {}
        cbVariables = {}
        cb = {}
        cb_x = {"1": "0.0", "2": "0.0", "3": "0.6", "4": "0.6"}
        cb_y = {"1": "0.1", "2": "0.8", "3": "0.1", "4": "0.8"}
        for i in range(len(lt.feats)):
            cbTexts[i] = lt.feats[i]
            # cbTexts[i].set(lt.feats[i])
            cbVariables[i] = tk.IntVar()

            # print(str(cbTexts[i]) + " "+ lt.feats[i])

            cb[i] = tk.Checkbutton(self, text=cbTexts[i], variable=cbVariables[i])
            cb[i].pack()

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: multitool(cbVariables, cbTexts, controller))
        button3.pack()

        print(cbVariables[2].get())

        # for cbVariable 1 means clicked and 0 means not clicked
        button4 = ttk.Button(self, text="print cbvars", command=lambda : printstuff(cbVariables, cbTexts))
        button4.pack()

def printstuff(cbV, cbT):
    for i in range(len(cbV)):
        print(cbT[i],"   ",cbV[i].get())

def multitool(cbV, cbT, cont):
    cont.show_frame(PageThree)
    for i in range(len(cbV)):
        print(cbT[i],"   ",cbV[i].get())


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        a.plot(lt.xvals, lt.yvals)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = StockPredictGUI()
app.mainloop()