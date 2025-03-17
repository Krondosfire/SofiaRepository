from tkinter import *
from tkinter import ttk
import random



#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("1900x1200")

def change_style():
   label.config(font=('Impact', 15 ,'italic'), foreground= "white", background="black")
   button.config(text= "Close", command=lambda:win.destroy())

#Create an canvas object
canvas= Canvas(win, width= 1000, height= 750)
#Load an image inside the canvas
smiley = PhotoImage(file='test.gif')
#Create an image in the canvas object
image_item = canvas.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115, 20, 115, 30, 95, 20, width=2)
#Bind the Button Event to the Canvas Widget
canvas.tag_bind(image_item, '<Button-1>', lambda e:
canvas.delete(image_item))
canvas.pack()
win.mainloop()