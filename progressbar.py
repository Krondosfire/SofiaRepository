import tkinter as tk
from tkinter import *


def create_window():
    from tkinter import ttk
    import time

    def start():
        myprogress.start()

    def stop():
        myprogress.stop()

    root = Tk()
    root.geometry("660x400")
    myprogress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='indeterminate',
                                 maximum=100)
    myprogress.pack(pady=20)

    mybutton = Button(root, text="start", command=start)
    mybutton.pack(pady=20)
    mybuttonstop = Button(root, text="stop", command=stop)
    mybuttonstop.pack(pady=20)
    root.mainloop()


root = tk.Tk()
b = tk.Button(root, text="Create new window", command=create_window)
b.grid(row=4, column=3, sticky=W + E, padx=10, pady=20)

root.mainloop()
