import csv
import serial
from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import messagebox
import time
import threading

from matplotlib.backend_bases import NavigationToolbar2

from ini_read import getINI
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from subprocess import call
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as animation
from matplotlib import style

iniData = getINI()
commPort = 'COM3'
ser = serial.Serial(commPort, baudrate=9600, timeout=1)
global rec_on, status
max_len = 3
is_on = True
rec_on = True
numRowsCollect = int(iniData['numRowsCollect'])
numPoints = 4
dataList = [0] * numPoints
plt.style.use('seaborn-darkgrid')
plt.rcParams.update({'font.size': 6})

#df = pd.DataFrame(list())
#df.to_csv('analog-data2.csv')
x_vals = []
y_vals = []
xList = []
yList = []
#y2List = []
fig = Figure(figsize=(5, 5), dpi=60)
plt1 = fig.add_subplot(111)

LARGE_FONT= ("Verdana", 12)
with open('analog-data2.csv', 'r+') as f:
    writer = csv.writer(f, dialect='excel-tab', delimiter=',')
    writer.writerow(["DateTime", "FT-01", "TT-01", "pH-01", "TDS-01", "WS-01"])


def plot(i):

    d1 = pd.read_csv('analog-data2.csv')
    print(d1)
    xList = d1["DateTime"]
    y1List = d1["FT-01"]
    y2List = d1["TT-01"]
    plt1.cla()

    plt1.grid(color='green', linestyle='--', linewidth=0.5)
    plt1.plot(xList, y1List, label='FT-01')
    plt1.plot(xList, y2List, label='TT-01')
    plt1.legend(loc='upper left')
    plt1.tight_layout()

    root.after(1000, plot)

def animate(i):
    d = pd.read_csv('analog-data2.csv')
    print(d)
    x = d["DateTime"]
    y1 = d["FT-01"]
    y2 = d["TT-01"]
    plt.cla()
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.plot(x, y1, label='FT-01')
    plt.plot(x, y2, label='TT-01')

    plt.legend(loc='upper left')
    plt.tight_layout()

    '''t4 = threading.Thread(target=animate)
    t4.daemon = True
    t4.start()'''


def readSensor():
    global val01
    mcD = ser.readline().rstrip()
    data0 = str(mcD)
    data0 = data0[2:-1]
    u = data0.split(" ")
    if len(u) > 1:
        if int(u[1]) == 4:
            wslbl["text"] = u[0]
            wslbl.insert(0, wslbl["text"])
        if int(u[1]) == 5:
            tdslbl["text"] = u[0]
            tdslbl.insert(0, tdslbl["text"])
        if int(u[1]) == 6:
            phlbl["text"] = u[0]
            phlbl.insert(0, phlbl["text"])
        if int(u[1]) == 7:
            lbl["text"] = u[0]
            lbl.insert(0, lbl["text"])
            print(lbl["text"])

        if int(u[1]) == 8:
            labl["text"] = u[0]
            labl.insert(0, labl["text"])
    root.after(1000, readSensor)


def enter_button():
    global after_id, lbl
    now = datetime.datetime.now()
    header = ["DateTime", "FT-01", "TT-01", "pH-01", "TDS-01", "WS-01"]
    with open('analog-data2.csv', 'a') as f:
        w = csv.writer(f, dialect='excel-tab', delimiter=',')
        w.writerow([now.strftime("%Y-%m-%d %H:%M"), lbl["text"], labl["text"], phlbl["text"], tdslbl["text"], wslbl["text"]])
        label_rec_on.config(text="Record in progress!")
    after_id = root.after(5000, enter_button)


def stop():
    global after_id
    if after_id:
        root.after_cancel(after_id)
        after_id = None
        label_rec_on.config(text="Not Recording!")


def turnOn():
    if blinkState.get() == 1:
        blinkLED()
    else:
        ser.write(b'o')


def turnOff():
    ser.write(b'x')


def blinkLED():
    if blinkState.get() == 1:
        ser.write(b'b')
        time.sleep(1)
        delay = userDelay.get()
        numBlinks = entryBlink.get()
        userInputValid = userDataCheck(numBlinks)
        if userInputValid == True:
            dataToSend = delay + '-' + numBlinks
            ser.write(dataToSend.encode())


def userDataCheck(userInput):
    try:
        int(userInput)
        return True
    except:
        messagebox.showerror("Error", "Enter a valid integer!", icon='error')
        return False


def menuSave():
    print("Selected Save")


def exitGUI():
    root.destroy()


def menuBlinkEnable():
    if blinkState.get() != 1:
        blinkState.set(1)
    blinkLED()


def menuTurnOn():
    if blinkState.get() == 1:
        blinkState.set(0)
    ser.write(b'o')


def menuTurnOff():
    if blinkState.get() == 1:
        blinkState.set(0)
    ser.write(b'x')


def menuDelaySelect(index):
    if blinkState.get() == 0:
        blinkState.set(1)
    userDelay.set(blinkTime[index])


def av01On():
    global is_on
    if is_on:
        label_av01.config(text="AV01 Off", bg='red')
        btn_av01.config(text='Disengaged', state=ACTIVE)
        is_on = False
    else:
        label_av01.config(text="AV01 On", bg='green')
        btn_av01.config(text='Engaged', state=ACTIVE)
        is_on = True


'''def rec_on():
    global rec_on
    if rec_on:
        label_rec_on.config(text="Not Recording!")
        B1.config(text='Start Recording', image=photoimage1, compound=LEFT)
        rec_on = False
    else:
        label_rec_on.config(text="Record in progress!")
        B1.config(text='Start Recording', image=photoimage1, compound=LEFT)
        rec_on = True'''


def openLog():
    call("notepad analog-data2.csv")
    '''t3 = threading.Thread(target=openLog)
    t3.daemon = True
    t3.start()'''


def getValues():
    # ser.write(b'g')
    arduinoData = ser.readline().decode().split('\r\n')  # ("ascii")
    return arduinoData[0]
    root.after(527, getValues)


'''def printToFile(data, index):
    file = open(fileName, "a")
    file.write(data)
    if index != (numPoints - 1):
        file.write(' , ')
    else:
        file.write('\n')'''


def recordData():
    for row in range(0, numRowsCollect):
        for i in range(0, numPoints):
            data = getValues()
            printToFile(data, i)
            dataList[i] = data
            print(dataList)
        break
        file.close()




root = Tk()
root.title('Basic Control on Arduino')
root.geometry("600x400")
root.iconbitmap('Skylet_logo.ico')


btn_On = tk.Button(root, text="Turn On", command=turnOn)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOff)
btn_Off.grid(row=0, column=1)

label_av01 = tk.Label(root, text="AV01 On", bg='green')
label_av01.grid(row=6, column=0)
btn_av01 = tk.Button(root, text="Engaged", command=av01On)
btn_av01.grid(row=6, column=1)

blinkState = IntVar()
chkBtn_Blink = tk.Checkbutton(root, text="Blink", variable=blinkState, command=blinkLED)
chkBtn_Blink.grid(row=0, column=2)

blinkTime = ['50', '100', '200', '400', '600', '800', '1000', '1200']
userDelay = StringVar()
delayMenu = tk.OptionMenu(root, userDelay, *blinkTime)
userDelay.set('800')
delayLabel = tk.Label(root, text="Blink (ms)")
delayLabel.grid(row=1, column=0)
delayMenu.grid(row=1, column=1)

entryBlink = Entry(root, width=6)
entryBlink.insert(0, "5")
entryBlinkLabel = tk.Label(root, text="# of Blinks")
entryBlinkLabel.grid(row=2, column=0)
entryBlink.grid(row=2, column=1)

menuBar = Menu(root)
root.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Save', command=menuSave)
fileMenu.add_command(label='Exit', command=exitGUI)

settings = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Settings', menu=settings)
settings.add_command(label='Blink', command=menuBlinkEnable)
settings.add_command(label='Turn On', command=menuTurnOn)
settings.add_command(label='Turn Off', command=menuTurnOff)

delaySubMenu = Menu(settings, tearoff=0)
settings.add_cascade(label='Delay', menu=delaySubMenu)
for i in range(0, len(blinkTime)):
    delaySubMenu.add_command(label=blinkTime[i], command=(lambda i=i: menuDelaySelect(i)))

##############################################################################################


lbl_01 = tk.Label(root, text="Temperature FT (°C):")
lbl_01.grid(row=7, column=0)

lbl = tk.Entry(root, width=2, font=('courier', 8, 'bold'))
lbl.grid(row=7, column=1)

labl_01 = tk.Label(root, text="Temperature TT (°C):")
labl_01.grid(row=8, column=0)

labl = tk.Entry(root, width=2, font=('courier', 8, 'bold'))
labl.grid(row=8, column=1)

phlbl_01 = tk.Label(root, text="pH FT:")
phlbl_01.grid(row=9, column=0)

phlbl = tk.Entry(root, width=4, font=('courier', 8, 'bold'))
phlbl.grid(row=9, column=1)

tdslbl_01 = tk.Label(root, text="Total Dissolved Solids (ppm):")
tdslbl_01.grid(row=10, column=0)

tdslbl = tk.Entry(root, width=3, font=('courier', 8, 'bold'))
tdslbl.grid(row=10, column=1)

wslbl_01 = tk.Label(root, text="Water level (%):")
wslbl_01.grid(row=11, column=0)

wslbl = tk.Entry(root, width=5, font=('courier', 8, 'bold'))
wslbl.grid(row=11, column=1)

labl.after(5, readSensor)
lbl.after(5, readSensor)
phlbl.after(5, readSensor)
tdslbl.after(5, readSensor)

logBtn = Button(root, text='Log File', command=openLog)
logBtn.grid(row=0, column=4)

photo1 = PhotoImage(file=r"record.png")
photo2 = PhotoImage(file=r"stop.png")


photoimage1 = photo1.subsample(10, 10)
photoimage2 = photo2.subsample(7, 7)
B1 = Button(root, text="Start recording", image=photoimage1, command=enter_button, compound=LEFT)
label_rec_on = tk.Label(root, text="....")
label_rec_on.grid(row=1, column=5)
B2 = Button(root, text="Stop recording", image=photoimage2, command=stop, compound=LEFT)
B1.grid(row=0, column=5)
B2.grid(row=0, column=6)

#plot_button = Button(master=root, command=plot, text="Plot")
#plot_button.grid(row=2, column=6)

#canvas = FigureCanvasTkAgg(fig, root)
#toolbar = NavigationToolbar2Tk(fig, root)
#canvas.get_tk_widget().grid(row=11, column=0)

#ani1 = animation.FuncAnimation(fig, plot, interval=1000, blit=False)
#canvas._tkcanvas.grid(row=13, column=0)
#toolbar.update()
ani = FuncAnimation(plt.gcf(), animate, interval=1000, blit=False)

plt.show()
#canvas.show()


t1 = threading.Thread(target=readSensor)  # fix it!!!
t1.daemon = True
t1.start()

t2 = threading.Thread(target=enter_button)
t2.daemon = True
t2.start()

t4 = threading.Thread(target=animate)
t4.daemon = True
t4.start()
root.mainloop()
