from tkinter import *
import csv
import datetime

def enter_button():
    now = datetime.datetime.now()
    amount = e1.get()
    amount1 = e2.get()
    amount2 = e3.get()
    with open('File.csv', 'a') as f:
        w = csv.writer(f,dialect='excel-tab')
        w.writerow([now.strftime("%Y-%m-%d %H:%M"), amount, amount1, amount2])


master = Tk()
e1 = Entry(master)
Label(master, text='Enter Number Here').grid(row=0)
e2 = Entry(master)
Label(master, text='Enter Number Here').grid(row=1)
e3 = Entry(master)
Label(master, text='Enter Number Here').grid(row=2)
myButton = Button(master,text='Enter', command=enter_button)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
myButton.grid(row=3,column=0)
mainloop()