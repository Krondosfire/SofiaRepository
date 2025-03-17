import csv
import serial
from tkinter import *
import tkinter as tk
import datetime
from tkinter import messagebox
import time
import threading
from ini_read import getINI
# from LogDataCSV import createCSV
from subprocess import call




def recordData():
    for row in range(0, numRowsCollect):
        for i in range(0, numPoints):
            data = getValues()
            printToFile(data, i)
            dataList[i] = data
            print(dataList)
        break
        file.close()


def printToFile(data, index):
    file = open(fileName, "a")
    file.write(data)
    if index != (numPoints - 1):
        file.write(' , ')
    else:
        file.write('\n')


def getValues():
    # ser.write(b'g')
    arduinoData = ser.readline().decode().split('\r\n')  # ("ascii")
    return arduinoData[0]
    root.after(527, getValues)


'''def graph(text):
    # Get the Entry Input
    tmptext = labl.get()
    tmptext = "$" + tmptext + "$" '''

recState = IntVar()
chkBtn_Rec = tk.Checkbutton(root, text="Record", variable=recState, command=enter_button)
chkBtn_Rec.grid(row=0, column=6)

recBtn = Button(root, text='Record', command=recordData)
recBtn.grid(row=0, column=5)

t2 = threading.Thread(target=recordData)
t2.daemon = True
t2.start()

with open('analog-data.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='excel-tab')
    writer.writerow(["Date", "Time", "FT01", "TT-01", "pH-01", "TDS-01"])


class TestTabs(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="Skylet_logo.ico")
        tk.Tk.wm_title(self, "Test Tabs")

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
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


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

        canvas = FigureCanvasTkAgg(fig, self)
        #canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


