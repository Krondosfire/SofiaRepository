from tkinter import Tk, Canvas
global is_on
is_on = True
window = Tk()

c = Canvas(window, width=300, height=300)

def clear():
    c.delete(ALL)

def clicked01(*args):
    global is_on
    # Determine is on or off
    if is_on:
        c.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115,20, 115, 30,
                     95, 20, fill="green", tags="av01")
        is_on = False

    else:
        c.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115, 20, 115, 30,
                      95, 20, fill="red", tags="av01")
        is_on = True

    #print("You clicked play!")

av01 = c.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115,
                                  20, 115, 30, 95, 20, fill="red",tags="av01")
#playtext = canvas.create_text(150, 50, text="Play", font=("Papyrus", 26), fill='blue',tags="av01")

c.tag_bind("av01","<Button-1>",clicked01)

c.pack()

window.mainloop()