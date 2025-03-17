from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
import tkinter as tk
import tkinter
from tkinter.ttk import *
from time import strftime
import time
import serial
import threading
import continuous_threading
import struct
import copy
import collections
from threading import Thread

# from Flash import flashColour

# Keep track of the button state on/off
from TestGUI01 import serialPlot

#'°C'

global is_on
is_on = True
ser = serial.Serial('COM3', 9600)
time.sleep(2)
data = []
#for i in range(50):


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Master Sheet P&ID")
        self.pack(fill=BOTH, expand=1)

        def clicked01(*arg):
            global is_on
            global button_flashing

            if is_on:
                canvas.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115,
                                   20, 115, 30, 95, 20, width=2, fill="#80F341", tags="av01")
                canvas.create_text(105, 40, text="AV01", font=("Arial", 9), fill='#80F341', tags="av01")


                is_on = False

            else:
                canvas.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115,
                                   20, 115, 30, 95, 20, width=2, fill="red", tags="av01")
                canvas.create_text(105, 40, text="AV01", font=("Arial", 9), fill='red', tags="av01")

                is_on = True

        def clicked02(*arg):
            global is_on


            if is_on:
                canvas.create_line(255, 130, 255, 125, 260, 125, 260, 135, 255, 135, 255, 130, 250, 130, 255, 120, 245,
                                   120,
                                   255, 140, 245, 140, 255, 120, width=2, fill='#80F341', tags='av02')
                canvas.create_text(230, 130, text="AV02", font=("Arial", 9), fill='#80F341', tags="av02")

                is_on = False

            else:
                canvas.create_line(255, 130, 255, 125, 260, 125, 260, 135, 255, 135, 255, 130, 250, 130, 255, 120, 245,
                                   120,
                                   255, 140, 245, 140, 255, 120, width=2, fill='red', tags='av02')
                canvas.create_text(230, 130, text="AV02", font=("Arial", 9), fill='red', tags="av02")
                is_on = True

        def clicked03(*arg):
            global is_on

            if is_on:
                canvas.create_line(355, 340, 350, 340, 350, 335, 360, 335, 360, 340, 355, 340, 355, 345, 345, 340, 345,
                                   350,
                                   365, 340, 365, 350, 345, 340, width=2, fill='#80F341', tags='av03')
                canvas.create_text(355, 360, text="AV03", font=("Arial", 9), fill='#80F341', tags="av03")
                is_on = False

            else:
                canvas.create_line(355, 340, 350, 340, 350, 335, 360, 335, 360, 340, 355, 340, 355, 345, 345, 340, 345,
                                   350,
                                   365, 340, 365, 350, 345, 340, width=2, fill='red', tags='av03')
                canvas.create_text(355, 360, text="AV03", font=("Arial", 9), fill='red', tags="av03")
                is_on = True

        def clicked04(*arg):
            global is_on

            if is_on:
                canvas.create_line(610, 225, 605, 225, 605, 220, 615, 220, 615, 225, 610, 225, 610, 230, 600, 225, 600,
                                   235, 620, 225, 620, 235, 600, 225, width=2, fill='#80F341', tags='av04')
                canvas.create_text(610, 245, text="AV04", font=("Arial", 9), fill='#80F341', tags="av04")
                is_on = False

            else:
                canvas.create_line(610, 225, 605, 225, 605, 220, 615, 220, 615, 225, 610, 225, 610, 230, 600, 225, 600,
                                   235, 620, 225, 620, 235, 600, 225, width=2, fill='red', tags='av04')
                canvas.create_text(610, 245, text="AV04", font=("Arial", 9), fill='red', tags="av04")
                is_on = True

        def clicked05(*arg):
            global is_on

            # Determine is on or off
            if is_on:
                canvas.create_line(695, 290, 695, 285, 700, 285, 700, 295, 695, 295, 695, 290, 690, 290, 695, 280, 685,
                                   280,
                                   695, 300, 685, 300, 695, 280, width=2, fill='#80F341', tags='av05')
                canvas.create_text(670, 290, text="AV05", font=("Arial", 9), fill='#80F341', tags="av05")
                is_on = False

            else:
                canvas.create_line(695, 290, 695, 285, 700, 285, 700, 295, 695, 295, 695, 290, 690, 290, 695, 280, 685,
                                   280,
                                   695, 300, 685, 300, 695, 280, width=2, fill='red', tags='av05')
                canvas.create_text(670, 290, text="AV05", font=("Arial", 9), fill='red', tags="av05")
                is_on = True

        def clicked06(*arg):
            global is_on

            # Determine is on or off
            if is_on:
                canvas.create_line(745, 290, 745, 285, 750, 285, 750, 295, 745, 295, 745, 290, 740, 290, 745, 280, 735,
                                   280, 745, 300, 735, 300, 745, 280, width=2, fill='#80F341', tags='av06')
                canvas.create_text(720, 290, text="AV06", font=("Arial", 9), fill='#80F341', tags="av06")
                is_on = False

            else:
                canvas.create_line(745, 290, 745, 285, 750, 285, 750, 295, 745, 295, 745, 290, 740, 290, 745, 280, 735,
                                   280, 745, 300, 735, 300, 745, 280, width=2, fill='red', tags='av06')
                canvas.create_text(720, 290, text="AV06", font=("Arial", 9), fill='red', tags="av06")
                is_on = True

        def clickedP1(*arg):
            global is_on

            # Determine is on or off
            if is_on:
                canvas.create_oval(445, 325, 485, 365, fill="#07ed1e", width=2, tags='pumpin')
                canvas.create_arc(475, 325, 445, 365, start=135,
                                  extent=90, outline="#060500", fill="#060500")
                canvas.create_text(465, 375, text="PumpIN", font=("Arial", 9), fill='#07ed1e', tags="pumpin")
                is_on = False

            else:
                canvas.create_oval(445, 325, 485, 365, fill="#ed071a", width=2, tags='pumpin')
                canvas.create_arc(475, 325, 445, 365, start=135,
                                  extent=90, outline="#060500", fill="#060500")
                canvas.create_text(465, 375, text="PumpIN", font=("Arial", 9), fill='#ed071a', tags="pumpin")
                is_on = True

        def clickedP2(*arg):
            global is_on

            # Determine is on or off
            if is_on:
                canvas.create_oval(850, 580, 890, 620, fill="#07ed1e", width=2, tags='pumpout')
                canvas.create_arc(850, 580, 890, 620, start=135,
                                  extent=90, outline="#060500", fill="#060500")
                canvas.create_text(870, 630, text="PumpOUT", font=("Arial", 9), fill='#07ed1e', tags="pumpout")
                is_on = False

            else:
                canvas.create_oval(850, 580, 890, 620, fill="#ed071a", width=2, tags='pumpout')
                canvas.create_arc(850, 580, 890, 620, start=135,
                                  extent=90, outline="#060500", fill="#060500")
                canvas.create_text(870, 630, text="PumpOUT", font=("Arial", 9), fill='#ed071a', tags="pumpout")
                is_on = True

        def clickedSF(*arg):
            global is_on

            # Determine is on or off
            if is_on:
                canvas.create_oval(850, 440, 870, 460, fill="#07ed1e", width=2, tags='sf')
                canvas.create_arc(870, 440, 850, 460, start=135,
                                  extent=90, outline="#060500", fill="#060500")
                canvas.create_polygon(points_04, outline='#2ab0c3', fill='#09e388', width=2, tags='sf')
                canvas.create_line(910, 430, 910, 470, dash=(4, 2), tags='sf')
                canvas.create_text(911, 450, text=">>", font=("Arial bold", 14), fill='#0947e3', tags="sf")
                canvas.create_text(890, 485, text="Sump Filter", font=("Arial", 9), fill='#07ed1e', tags="sf")
                is_on = False

            else:
                canvas.create_oval(850, 440, 870, 460, fill="#ed071a", width=2, tags='sf')
                canvas.create_arc(870, 440, 850, 460, start=135,
                                  extent=90, outline="#060500", fill="#060500")
                canvas.create_polygon(points_04, outline='#2ab0c3', fill='#e3bf09', width=2, tags='sf')
                canvas.create_text(910, 450, text="!", font=("Arial bold", 20), fill='#ed071a', tags="sf")
                canvas.create_text(890, 485, text="Sump Filter", font=("Arial", 9), fill='#ed071a', tags="sf")
                is_on = True

        def clickedUV(*arg):
            global is_on

            # Determine is on or off
            if is_on:
                canvas.create_polygon(points_05, outline='#2ab0c3', fill='#c737fa', width=2, tags='UV')
                canvas.create_text(960, 470, text="UV Light", font=("Arial", 9), fill='#760f9a', tags="UV")
                is_on = False

            else:
                canvas.create_polygon(points_05, outline='#2ab0c3', fill='#760f9a', width=2, tags='UV')
                canvas.create_text(960, 470, text="UV Light", font=("Arial", 9), fill='#760f9a', tags="UV")
                is_on = True

        canvas = tk.Canvas(self, background='#D0D0CD')

        # display time on the label
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(canvas, font=('Courier', 10, 'bold'),
                    background='#D0D0CD',
                    foreground='#1e287c')
        lbl.pack(anchor='n')
        time()


        def readserial():
            b = ser.readline()
            str_rn = b.decode()
            str = str_rn.rstrip()
            f = float(str)
            print(f)
            #data.append(f)  # add to the end of data list
            #time.sleep(0.1)
            varLabel = IntVar()
            tkLabel = Label(temp, text=f, font=("Verdana", 10, 'bold'),
                                    background='#b7dbec', foreground='#1e287c')
            tkLabel.pack()

            varLabel2 = IntVar()
            tkLabel2 = Label(temp1, text=f, font=("Verdana", 8, 'bold'),
                                     background='#b7dbec', foreground='#1e287c')
            tkLabel2.pack()



        b = tk.Canvas
        temp = Label(canvas, text='Temp/FT01:', font=("Verdana", 10, 'bold'), background='#b7dbec',
                             foreground='#1e287c').place(x=840, y=300)



        temp1 = Label(canvas, text='Temp/TT01:   ', font=("Verdana", 8, 'bold'), background='#b7dbec',
                         foreground='#1e287c').place(x=140, y=300)



        t1 = continuous_threading.PeriodicThread(0.5, readserial)








        level = tk.Label(canvas, text='Level/LS01:   ', font=("Verdana", 10, 'bold'), background='#b7dbec',
                        foreground='#1e287c').place(x=840, y=340)
        t1.start()
        canvas.create_line(15, 25, 25, 25)
        canvas.create_line(25, 20, 25, 30, 45, 20, 45, 30, 25, 20)
        canvas.create_line(105, 20, 102, 20, 102, 17, 108, 17, 108, 20, 105, 20, 105, 25, 95, 20, 95, 30, 115,
                           20, 115, 30, 95, 20, width=2, fill='red', tags='av01')
        canvas.tag_bind("av01", "<Button-1>", clicked01)
        canvas.create_text(105, 40, text="AV01", font=("Arial", 9), fill='red', tags="av01")
        canvas.create_line(45, 25, 58, 25, fill='blue', width='2')
        canvas.create_line(82, 25, 95, 25)
        canvas.create_oval(68, 23, 72, 27)
        canvas.create_line(58, 20, 68, 25, 58, 30, 58, 20)
        canvas.create_line(72, 25, 82, 20, 82, 30, 72, 25)
        canvas.create_line(70, 27, 75, 37, 65, 37, 70, 27)
        canvas.create_line(70, 37, 70, 57, 45, 57)
        canvas.create_line(25, 52, 25, 62, 45, 52, 45, 62, 25, 52)
        canvas.create_text(36, 72, text="MV01", font=("Arial", 9), fill='black', tags="mv01")
        canvas.create_text(36, 40, text="MV02", font=("Arial", 9), fill='black', tags="mv02")
        canvas.create_text(70, 12, text="3-Way-1", font=("Arial", 9), fill='black', tags="3way-1")
        canvas.create_text(742, 216, text="3-Way-3", font=("Arial", 9), fill='black', tags="3way-3")
        canvas.create_text(693, 216, text="3-Way-2", font=("Arial", 9), fill='black', tags="3way-2")
        canvas.create_text(115, 90, text="FilterIN", font=("Arial", 9), fill='black', tags="filterin")
        canvas.create_text(465, 375, text="PumpIN", font=("Arial", 9), fill='#ed071a', tags="pumpin")
        canvas.create_text(870, 630, text="PumpOUT", font=("Arial", 9), fill='#ed071a', tags="pumpout")
        canvas.create_text(890, 485, text="Sump Filter", font=("Arial", 9), fill='#ed071a', tags="sf")
        canvas.create_text(960, 470, text="UV Light", font=("Arial", 9), fill='#760f9a', tags="UV")
        canvas.create_text(1015, 475, text="Check \nValve", font=("Arial", 9), fill='black', tags="check")
        canvas.create_line(25, 57, 10, 57)
        #canvas = Tk.Tk()
        p1 = canvas.create_line(115, 25, 145, 25, 145, 65, fill='blue', width='2', tags='AV01')
        #my_button = canvas.tag_bind(p1, buttonCallback(self), foreground=flash_colours[0])
        #my_button.pack()

        canvas.create_line(145, 65, 135, 75, 145, 85, 155, 75, 145, 65)
        canvas.create_line(135, 75, 155, 75, dash=(4, 2))
        canvas.create_line(135, 230, 135, 350, 265, 350, 265, 230, fill="#7F5D00", width=3)
        canvas.create_line(130, 245, 130, 225, 270, 225, 270, 245, fill="#7F5D00", width=3)
        canvas.create_rectangle(137, 245, 263, 348, outline="#b7dbec", fill="#b7dbec")
        canvas.create_line(145, 85, 145, 315)
        canvas.create_line(253, 345, 345, 345)
        canvas.create_line(355, 340, 350, 340, 350, 335, 360, 335, 360, 340, 355, 340, 355, 345, 345, 340, 345, 350,
                           365, 340, 365, 350, 345, 340, width=2, fill='red', tags='av03')
        canvas.tag_bind("av03", "<Button-1>", clicked03)
        canvas.create_text(355, 360, text="AV03", font=("Arial", 9), fill='red', tags="av03")
        canvas.create_line(365, 345, 445, 345)
        canvas.create_oval(445, 325, 485, 365, fill="#ed071a", width=2, tags='pumpin')
        canvas.create_arc(475, 325, 445, 365, start=135,
                          extent=90, outline="#060500", fill="#060500")
        canvas.tag_bind("pumpin", "<Button-1>", clickedP1)
        canvas.create_line(485, 345, 545, 345, 545, 230, 600, 230)
        canvas.create_line(610, 225, 605, 225, 605, 220, 615, 220, 615, 225, 610, 225, 610, 230, 600, 225, 600, 235,
                           620, 225, 620, 235, 600, 225, width=2, fill='red', tags='av04')
        canvas.tag_bind("av04", "<Button-1>", clicked04)
        canvas.create_text(610, 245, text="AV04", font=("Arial", 9), fill='red', tags="av04")
        canvas.create_line(620, 230, 680, 230)
        canvas.create_line(680, 225, 680, 235, 688, 230, 680, 225)
        canvas.create_oval(688, 228, 692, 232)
        points_01 = [690, 232, 685, 240, 695, 240, 690, 232]
        canvas.create_polygon(points_01, outline='#060500', fill='#060500')
        canvas.create_line(692, 230, 700, 225, 700, 235, 692, 230)
        canvas.create_line(700, 230, 730, 230)
        canvas.create_line(730, 225, 738, 230, 730, 235, 730, 225)
        canvas.create_oval(738, 228, 742, 232)
        points_02 = [740, 232, 735, 240, 745, 240, 740, 232]
        canvas.create_polygon(points_02, outline='#060500', fill='#060500')
        canvas.create_line(780, 250, 780, 400, 1100, 400, 1100, 250, width=3, fill="#0b889a")
        canvas.create_rectangle(782, 265, 1098, 398, outline="#b7dbec", fill="#b7dbec")
        canvas.create_line(742, 230, 750, 225, 750, 235, 742, 230)
        canvas.create_line(750, 230, 810, 230, 810, 320)
        points_03 = [810, 320, 800, 330, 810, 340, 820, 330, 810, 320]
        canvas.create_polygon(points_03, outline='#e4c1ee', fill='#e4c1ee')
        canvas.create_line(800, 330, 820, 330, dash=(4, 2))
        canvas.create_line(810, 340, 810, 360)
        canvas.create_line(690, 240, 690, 280)
        canvas.create_line(740, 240, 740, 280)
        canvas.create_line(695, 290, 695, 285, 700, 285, 700, 295, 695, 295, 695, 290, 690, 290, 695, 280, 685, 280,
                           695, 300, 685, 300, 695, 280, width=2, fill='red', tags='av05')
        canvas.tag_bind("av05", "<Button-1>", clicked05)
        canvas.create_text(670, 290, text="AV05", font=("Arial", 9), fill='red', tags="av05")
        canvas.create_line(745, 290, 745, 285, 750, 285, 750, 295, 745, 295, 745, 290, 740, 290, 745, 280, 735, 280,
                           745, 300, 735, 300, 745, 280, width=2, fill='red', tags='av06')
        canvas.tag_bind("av06", "<Button-1>", clicked06)
        canvas.create_text(720, 290, text="AV06", font=("Arial", 9), fill='red', tags="av06")
        canvas.create_line(690, 300, 690, 600, 850, 600)
        canvas.create_oval(850, 440, 870, 460, fill="#ed071a", width=2, tags='sf')
        canvas.create_arc(870, 440, 850, 460, start=135,
                          extent=90, outline="#060500", fill="#060500")
        canvas.tag_bind("sf", "<Button-1>", clickedSF)
        canvas.create_line(740, 300, 740, 450, 850, 450)
        canvas.create_oval(850, 580, 890, 620, fill="#ed071a", width=2, tags='pumpout')
        canvas.create_arc(880, 580, 850, 620, start=135,
                          extent=90, outline="#060500", fill="#060500")
        canvas.tag_bind("pumpout", "<Button-1>", clickedP2)
        canvas.create_line(890, 600, 1100, 600, 1100, 630)
        canvas.create_line(1085, 640, 1085, 650, 1100, 650, 1100, 643, 1100, 650, 1115, 650, 1115, 640, width=3,
                           fill="#060500")
        canvas.create_line(870, 450, 890, 450)
        points_04 = [890, 450, 910, 470, 930, 450, 910, 430, 890, 450]
        canvas.create_polygon(points_04, outline='#2ab0c3', fill='#e3bf09', width=2, tags='sf')
        canvas.create_line(910, 430, 910, 470, dash=(4, 2), tags='sf')
        canvas.create_rectangle(840, 425, 935, 475, dash=(4, 2), outline="black")
        canvas.create_line(930, 450, 950, 450)
        points_05 = [950, 450, 960, 460, 970, 450, 960, 440, 950, 450]
        canvas.create_polygon(points_05, outline='#2ab0c3', fill='#760f9a', width=2, tags='UV')
        canvas.tag_bind("UV", "<Button-1>", clickedUV)
        canvas.create_line(970, 450, 1000, 450)
        canvas.create_line(1005, 440, 1015, 440, 1010, 440, 1010, 450, 1000, 445, 1000, 455, 1000, 445, 1020, 455, 1020,
                           445, width=2)
        canvas.create_line(1020, 450, 1115, 450, 1115, 230, 1085, 230, 1085, 280)
        canvas.create_line(300, 50, 300, 100, 350, 100, 350, 50, fill='#d21a6d', width=2)
        canvas.create_line(297, 53, 297, 47, 353, 47, 353, 53, fill='#d21a6d', width=2)
        canvas.create_rectangle(302, 60, 348, 98, outline="#b7dbec", fill="#9be518")
        canvas.create_line(320, 85, 250, 85, 250, 120)
        canvas.create_line(255, 130, 255, 125, 260, 125, 260, 135, 255, 135, 255, 130, 250, 130, 255, 120, 245, 120,
                           255, 140, 245, 140, 255, 120, width=2, fill='red', tags='av02')
        canvas.create_text(230, 130, text="AV02", font=("Arial", 9), fill='red', tags="av02")
        canvas.tag_bind('av02', '<Button-1>', clicked02)
        canvas.create_line(250, 140, 250, 315)

        # Create an image in the canvas object
        # image_item = canvas.create_image((200, 140), image=smiley)
        # Bind the Button Event to the Canvas Widget
        canvas.pack(fill=BOTH, expand=1, side=tk.LEFT)


def main():
    root = Tk()
    ex = Example()
    root.geometry("1200x900+300+300")
    root.iconbitmap('Skylet_logo.ico')



    root.mainloop()


if __name__ == '__main__':
    main()
