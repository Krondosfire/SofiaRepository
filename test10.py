from serial import *
from tkinter import *
import time
import sys
global root

def split_coords(astring):
    a, b = astring.split("; ")
    a = int(a)
    b = int(b)

    return (a, b)

def paintRectangle1():
    print("entered Rect 1")
    canvas.create_rectangle(207, 152, 616, 375, outline= "", fill ='red')
    canvas.pack()
    root.after(200, repaintRectangles)

def paintRectangle2():
    print("entered Rect 2")
    canvas.create_rectangle(665, 152, 1073, 375, outline= "", fill ='red')
    canvas.pack()
    root.after(200, repaintRectangles)

def paintRectangle3():
    print("entered Rect 3")
    canvas.create_rectangle(207, 425, 616, 648, outline= "", fill ='red')
    canvas.pack()
    root.after(200, repaintRectangles)

def paintRectangle4():
    print("entered Rect 4")
    canvas.create_rectangle(665, 425, 1073, 648, outline= "", fill ='red')
    canvas.pack()
    root.after(200, repaintRectangles)

def repaintRectangles():
    print("entered Repaint")
    canvas.create_rectangle(207, 152, 616, 375, outline= "", fill ='white')
    canvas.create_rectangle(665, 152, 1073, 375, outline= "", fill ='white')
    canvas.create_rectangle(207, 425, 616, 648, outline= "", fill ='white')
    canvas.create_rectangle(665, 425, 1073, 648, outline= "", fill ='white')
    canvas.pack()

root = Tk()
root.geometry("1280x800")
root.attributes('-fullscreen', True)
#bg = PhotoImage(file= “ / home / pi / Pictures / SCREEN2.png”)
canvas = Canvas(root)
canvas.pack(fill= "both", expand = True)
canvas.config(cursor= 'none')
#canvas.create_image(0, 0, image=bg, anchor= "nw")

serialPort = "COM3"
ser = Serial(serialPort, 9600, timeout=0)
ser.flush()

while True:

           root.update()

           if ser.in_waiting > 0:
             line = ser.readline().decode('utf-8').rstrip()
             if (line == "inits"):
               x, y = 1000, 1000

             else:
               x, y = split_coords(line)
               print("x:", x, "- y:", y)
               ser.flush()

             if (19 < x < 60) and (20 < y < 40):
                print("OK button1")
                paintRectangle1()
             if (68 < x < 110) and (20 < y < 40):
                print("OK button2")
                paintRectangle2()
             if (19 < x < 60) and (45 < y < 80):
                print("OK button3")
                paintRectangle3()
             if (68 < x < 110) and (45 < y < 80):
                print("OK button4")
                paintRectangle4()
             if (-10 < x < 20) and (-10 < y < 20):
                sys.exit()
root.mainloop()