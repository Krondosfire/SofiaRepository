import serial
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#commPort = 'COM3'
#ser = serial.Serial(commPort, baudrate=9600, timeout=1)
#data = open('analog-data.csv', 'a')
plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

#index = count()

def animate(i):
    d = pd.read_csv('analog-data1.csv')
    print(d)
    x = d["DateTime"]
    y1 = d["FT-01"]
    y2 = d["TT-01"]

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

