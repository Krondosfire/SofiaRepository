from tkinter import *
root = Tk()
root.geometry("400x200")

def button_command():
    #print("Test")
    #text = entry1.get()
    #print(text)
    text = "How to display data from Serial Port here?"
    entry1.insert(0, text)
    return None

entry1 = Entry(root, width=20)
entry1.pack()

Button(root, text="Button", command=button_command).pack()






root.mainloop()