
import tkinter
import serial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import time

class App:
    def __init__(self, master):

        self.arduinoData = serial.Serial('com3', 9600, timeout=0)

        frame = tkinter.Frame(master)

        self.go = 0

        self.start = tkinter.LabelFrame(frame, text="Start", borderwidth=10, relief=tkinter.GROOVE, padx=10, pady=10)
        self.start.grid(row=0, column=0, padx=20, pady=20)

        self.run = tkinter.Button(self.start, text="RUN", bd=10, height=5, width=10, command=self.getData)
        self.run.grid(row=0, column=0, padx=5, pady=5)

        self.stop_frame = tkinter.LabelFrame(frame, text="STOP", borderwidth=10, relief=tkinter.GROOVE, padx=10, pady=10 )
        self.stop_frame.grid(row=0, column=1, padx=20, pady=20)

        self.stop = tkinter.Button(self.stop_frame, text="STOP", bd=10, height=5, width=10, command=self.stopTest)
        self.stop.grid(row=0, column=0, padx=5, pady=5)

        self.fig = plt.Figure()
        self.ax1 = self.fig.add_subplot(211)
        self.line0, = self.ax1.plot([], [], lw=2)
        self.line1, = self.ax1.plot([], [], lw=2)
        self.line2, = self.ax1.plot([], [], lw=2)
        self.line3, = self.ax1.plot([], [], lw=2)
        self.ax2 = self.fig.add_subplot(212)
        self.line4, = self.ax2.plot([], [], lw=2)
        self.line5, = self.ax2.plot([], [], lw=2)
        self.line6, = self.ax2.plot([], [], lw=2)
        self.line7, = self.ax2.plot([], [], lw=2)
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=4, padx=20, pady=20)
        frame.grid(row=0, column=0, padx=20, pady=20)

    def getData(self):
        self.k = 0
        self.xdata = []
        self.pressure1 = []
        self.displacement1 = []
        self.cycle1 = []
        self.pressure2 = []
        self.displacement2 = []
        self.cycle2 = []
        self.pressure3 = []
        self.displacement3 = []
        self.cycle3 = []
        self.pressure4 = []
        self.displacement4 = []
        self.cycle4 = []
        self.arduinoData.flushInput()
        self.go = 1
        self.readData()

    def readData(self):
        if self.go == 1:
            self.xdata.append(self.k)
            while (self.arduinoData.inWaiting()==0):
                pass
            x = self.arduinoData.readline()
            strip_data = x.strip()
            split_data = x.split("|")
            actuator1 = split_data[0].split(".")
            actuator2 = split_data[1].split(".")
            actuator3 = split_data[2].split(".")
            actuator4 = split_data[3].split(".")
            self.pressure1.append(int(actuator1[0]))
            self.displacement1.append(int(actuator1[1]))
            self.cycle1 = int(actuator1[2])
            self.pressure2.append(int(actuator2[0]))
            self.displacement2.append(int(actuator2[1]))
            self.cycle2 = int(actuator2[2])
            self.pressure3.append(int(actuator3[0]))
            self.displacement3.append(int(actuator3[1]))
            self.cycle3 = int(actuator3[2])
            self.pressure4.append(int(actuator4[0]))
            self.displacement4.append(int(actuator4[1]))
            self.cycle4 = int(actuator4[2])
            self.printData()
            root.after(0, self.readData)


    def printData(self):
        print(str(self.pressure1[self.k-1]) + " " + str(self.displacement1[self.k-1]) + " " + str(self.cycle1) + " "
        + str(self.pressure2[self.k-1]) + " " + str(self.displacement2[self.k-
        1]) + " " + str(self.cycle2) + " " + str(self.pressure3[self.k-1]) + " " + str(self.displacement3[self.k-1]) \
        + " " + str(self.cycle3) + " " + str(self.pressure4[self.k-1]) + " " + str(self.displacement4[self.k-1]) + " " \
        + str(self.cycle4))

    def stopTest(self):
        self.arduinoData.write("<H>")
        self.go = 0


    def resetTest(self):
        self.k = 0
        self.xdata = []
        self.pressure1 = []
        self.displacement1 = []
        self.cycle1 = []
        self.pressure2 = []
        self.displacement2 = []
        self.cycle2 = []
        self.pressure3 = []
        self.displacement3 = []
        self.cycle3 = []
        self.pressure4 = []
        self.displacement4 = []
        self.cycle4 = []
        self.line1.set_data(self.xdata, self.ydata1)
        self.line2.set_data(self.xdata, self.ydata2)
        self.ax1.set_ylim(0,1)
        self.ax1.set_xlim(0,1)
        self.ax2.set_ylim(0,1)
        self.ax2.set_xlim(0,1)

    def start(self):
        self.xdata = []
        self.pressure1 = []
        self.displacement1 = []
        self.cycle1 = []
        self.pressure2 = []
        self.displacement2 = []
        self.cycle2 = []
        self.pressure3 = []
        self.displacement3 = []
        self.cycle3 = []
        self.pressure4 = []
        self.displacement4 = []
        self.cycle4 = []
        self.k = 0
        self.arduinoData.write("<L>")

root = tkinter.Tk()
app = App(root)
root.mainloop()