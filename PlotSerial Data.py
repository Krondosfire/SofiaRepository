from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr
import threading
import time

# Global variables
data = np.array([])
cond = False


# Plot Data
def plot_data():
    global cond, data
    if (cond == True):
        a = s.readline()
        a.decode('utf8')

        if (len(data) < 100):
            try:
                data = np.append(data, float(a[0:4]))
            except:
                pass
        else:
            data[0:99] = data[1:100]
            data[99] = float(a[0:4])
        #data_sp = np.append(data_sp, sp)
        #ax.clear()
        #ax.plot(data)
        lines.set_xdata(np.arange(0, len(data)))
        lines.set_ydata(data)

        canvas.draw()
    root.after(1, plot_data)

def plot_start():
    global cond
    cond = True
    s.reset_input_buffer()
    t1 = threading.Thread(target=plot_data)
    t1.daemon = True
    t1.start()

def plot_stop():
    global cond
    cond = False

# Main GUI
root = tk.Tk()
root.title('Real Time Plot')
root.configure(background='light blue')
root.geometry("900x600")

# Create Plot object
# add figure canvas
fig = Figure();
ax = fig.add_subplot(111)

# ax = plt.axes(xlim=(0,100), ylim=(0, 120));
ax.set_title("Some Data")
ax.set_xlabel("Sample")
ax.set_ylabel("Units (C)")
ax.set_xlim(0, 100)
ax.set_ylim(-0.5, 6)
lines = ax.plot([], [])[0]

canvas = FigureCanvasTkAgg(fig, master=root) # tk.DrawingArea
canvas.get_tk_widget().place(x=10, y=10, width=600, height=400)
canvas.draw()

# Create buttons
root.update()
start = tk.Button(root, text="Start", font=("courier", 12), command=lambda: plot_start())
start.place(x=100, y=450)

root.update()
stop = tk.Button(root, text="Stop", font=("courier", 12), command=lambda: plot_stop())
stop.place(x=start.winfo_x()+start.winfo_reqwidth() + 20, y=450)

# Start serial port
s = sr.Serial('COM3', 9600)
s.reset_input_buffer()

root.after(1, plot_data)
root.mainloop()