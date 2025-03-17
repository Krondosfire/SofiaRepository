import tkinter as tk
import serial  # Serial imported for Serial communication
import time  # Required to use delay functions

# Create the master object
root = tk.Tk()

ArduinoSerial = serial.Serial('com3', 9600)  # Create Serial port object called arduinoSerialData
time.sleep(2)

templabel = tk.Label(root, text="Temperature :" )
tempEntry = tk.Label(root, text=str(ArduinoSerial.readline()) )

templabel.grid(row=1, column=0)
tempEntry.grid(row=1, column=2)

templabel1 = tk.Label(root, text="Temperature :" )
tempEntry1 = tk.Label(root, text=str(ArduinoSerial.readline()) )

templabel1.grid(row=2, column=0)
tempEntry1.grid(row=2, column=2)

root.mainloop()