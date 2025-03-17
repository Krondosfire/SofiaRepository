from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
import webbrowser

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

def open_url(url):
   webbrowser.open_new_tab(url)
   
av01 = win.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115,
                                  20, 115, 30, 95, 20)
# Create a Label Widget
label= Label(win, text= "Welcome to TutorialsPoint", cursor= "hand2", foreground= "green", font= ('Aerial 18'))
label.pack(pady= 30)

# Define the URL to open
url= 'https://www.tutorialspoint.com/'

# Bind the label with the URL to open in a new tab
label.bind("<Button-1>", lambda e:open_url(url))
win.mainloop()