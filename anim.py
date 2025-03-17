from tkinter import *

root = Tk()
root.title('Animation')
root.geometry('400x300')
canvas = Canvas(root)
count = 0
size = 26
pos = 100


def dash():
    


 def contract():
    global count, size, pos
    if count <= 10 and count > 0:
        size -= 2
        my_button.config(font=('Arial', size))

        # Change the button position
        my_button.pack_configure(pady=pos)
        count -= 1
        pos -= 20
        root.after(10, contract)

def expand():
    global count, size, pos
    if count < 10:
        size += 2
        # Configure the button
        my_button.config(font=('Arial', size))
        # Change the button position
        my_button.pack_configure(pady=pos)
        count += 1
        pos += 20
        root.after(10, expand)

    elif count == 10:
        contract()


# Create an object
my_button = Button(root, text='Click!', command=expand, font=('Arial', 24), fg='red')
my_dash = canvas.create_line(100, 330, 120, 330, dash=(4, 2), fill='blue', width=2, tags='dash')
my_dash01 = canvas.create_line(100, 330, 120, 330, dash=(2, 4), fill='blue', width=2, tags='dash')
my_button.pack(pady=100)
#my_dash.pack()






root.mainloop()
