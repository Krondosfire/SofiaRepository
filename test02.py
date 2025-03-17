import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH

#import RPi.GPIO as GPIO

# Declare global variables


av01_on = None
av01_off = None

# Pin definitions
#led_pin = 12

# This gets called whenever the ON button is pressed
def on():

    global av01_on
    global av01_off

    # Disable ON button, enable OFF button, and turn on LED
    av01_on.config(state=tk.DISABLED, fill='green')
    av01_off.config(state=tk.NORMAL, fill='red')
    #GPIO.output(led_pin, GPIO.HIGH)

# This gets called whenever the OFF button is pressed
def off():

    global av01_on
    global av01_off

    # Disable OFF button, enable ON button, and turn off LED
    av01_on.config(state=tk.NORMAL, fill='green')
    av01_off.config(state=tk.DISABLED, fill='red')
    #GPIO.output(led_pin, GPIO.LOW)

# Use "GPIO" pin numbering
#GPIO.setmode(GPIO.BCM)

# Set LED pin as output and turn it off by default
#GPIO.setup(led_pin, GPIO.OUT)
#GPIO.output(led_pin, GPIO.LOW)

# Create the main window
root = tk.Tk()
root.title("Test")

# Create the main container
frame = tk.Frame(root)

# Lay out the main container
frame.grid()

# Create widgets
#button_font = font.Font(family='Helvetica', size=24, weight='bold')

canvas = Canvas()
av01_on = canvas.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115,
                                  20, 115, 30, 95, 20, width=4, state=tk.NORMAL, fill='green' )
av01_off = canvas.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115,
                                  20, 115, 30, 95, 20, width=4, state=tk.DISABLED, fill='red')

# Lay out widgets
av01_on.pack(row=0, column=0)
av01_off.pack(row=1, column=0)

# Run forever!
root.mainloop()

# Neatly release GPIO resources once window is closed
#GPIO.cleanup()
