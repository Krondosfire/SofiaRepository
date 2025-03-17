import tkinter as tk

def fun():
    global count
    lbl.config(text=text+'.'*count)

    count += 1
    if count == 14:
        count=0

    root.after(1000, fun)


root = tk.Tk()

count = 0
text='Running'

lbl = tk.Label(root, text=text, font="Arial, 12", bg="light green")
lbl.place(x=102, y=70)
fun()

root.mainloop()