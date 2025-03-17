import tkinter as tk
import time
import serial
import threading
import continuous_threading
global root
ser = serial.Serial('COM3', 9600, timeout=1)
val1 = 0
index = []
ser.flush()


def readserial():
    global val1
    ser_bytes = ser.readline()
    ser_bytes = ser_bytes.decode('utf-8')
    print(ser_bytes.rstrip())
    val1 = ser_bytes
    index.append(val1)
    if len(index) == 1:
        disp1 = tk.Label(root, text=index[0]).place(x=50, y=10)
    elif len(index) == 1:
        disp2 = tk.Label(root, text=index[1]).place(x=50, y=40)
    if len(index) == 2:
        index.clear()
    time.sleep(0.5)


t1 = continuous_threading.PeriodicThread(0.5, readserial)

root = tk.Tk()
root.geometry('400x250')

temp1 = tk.Label(root, text='Temp. ').place(x=10, y=10)
temp2 = tk.Label(root, text='Temp. ').place(x=10, y=40)
t1.start()


root.mainloop()
