from tkinter import *

root = Tk()
root.geometry("1200x900+300+300")
root.iconbitmap('Skylet_logo.ico')

# Keep track of the button state on/off
global is_on
is_on = True

# Create label
my_label = Label(root, text="The AV01 is ON!")
my_label.pack()

# Define function
def switch():
    global is_on
    # Determine is on or off
    if is_on:
        on_button.config(image=off)
        my_label.config(text='The AV01 is OFF!', fg='red')
        is_on = False
    else:
        on_button.config(image=on)
        my_label.config(text='The AV01 is ON!', fg='green')
        is_on = True


# Define Images
on = PhotoImage(file='valve_on.png')
off = PhotoImage(file='valve_off.png')

# Create a button
on_button = Button(root, image=on, bd=0, command=switch)
on_button.pack(pady=50)







root.mainloop()





