from tkinter import *
import serial.tools.list_ports
import threading
import signal

def signal_handler(signum, frame):
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

class Graphics():
    pass

def connect_menu_init():
    global root, connect_btn, refresh_btn, graph
    root = Tk()
    root.title("Serial Communication")
    root.geometry("640x480")
    root.config(bg="white")
    root.iconbitmap('Skylet_logo.ico')

    port_label = Label(root, text="Available Port(s): ", bg="white")
    port_label.grid(column=1, row=2, pady=20, padx=10)

    port_bd = Label(root, text = "Baud Rate: ", bg="white")
    port_bd.grid(column=1, row=3, pady=20, padx=10)

    refresh_btn = Button(root, text="Refresh", height=2, width=10, command = update_coms)
    refresh_btn.grid(column=3, row=2)

    connect_btn = Button(root, text="Connect", height=2, width=10, state="disabled", command=connection)
    connect_btn.grid(column=3, row=4)
    baud_select()
    update_coms()

    graph = Graphics()

    graph.canvas = Canvas(root, width=300, height=300, bg="white", highlightthickness=0)
    graph.canvas.grid(row=5, columnspan=5)

    # dynamic update
    graph.outer = graph.canvas.create_arc(10, 10, 290, 290, start=90, extent=100, outline="#f11", fill="#f11", width=2)
    # static update
    graph.canvas.create_oval(75, 75, 225, 225, outline="#f11", fill="white", width=2)
    # dynamic update for the text
    graph.text = graph.canvas.create_text(150, 150, anchor = E, font = ("Courier", "20"), text="---")
    # Static
    graph.canvas.create_text(175, 150, anchor=CENTER, font=("Courier", "20"), text="mV")



def connect_check(args):
    if "-" in clicked_com.get() or "-" in clicked_bd.get():
        connect_btn["state"] = "disable"
    else:
        connect_btn["state"] = "active"





def baud_select():
    global clicked_bd, drop_bd
    clicked_bd = StringVar()
    bds = ["-",
           "300",
           "600",
           "1200",
           "2400",
           "4800",
           "9600",
           "14400",
           "19200",
           "28800",
           "38400",
           "56000",
           "57600",
           "115200",
           "128000",
           "256000"]
    clicked_bd.set(bds[6])
    drop_bd = OptionMenu(root, clicked_bd, *bds, command = connect_check)
    drop_bd.config(width=20)
    drop_bd.grid(column=2, row=3, padx=50)

def update_coms():
    global clicked_com, drop_COM
    ports = serial.tools.list_ports.comports()
    coms = [com[0] for com in ports]
    #print(coms)
    coms.insert(0,"-")
    try:
        drop_COM.destroy()    # this is OKAY!
    except:
        pass
    clicked_com = StringVar()
    clicked_com.set(coms[0])
    drop_COM = OptionMenu(root, clicked_com, *coms, command=connect_check)
    drop_COM.config(width=20)
    drop_COM.grid(column=2, row=2, padx=50)
    connect_check(0)

def split_coords(astring):
    a, b = astring.split(";")
    a = int(a)
    b = int(b)
    return a, b

def graph_control(graph):
    global sensor
    graph.canvas.itemconfig(graph.outer, exten=int(graph.sensor))
    graph.canvas.itemconfig(graph.text, text=f"{int(graph.sensor)}")


def readSerial():
    global serialData, graph, sensor
    average = 0
    sampling = 50
    sample = 0
    while serialData:
        data = ser.readline()
        if len(data) > 0:
            try:
                sensor = str(data.decode('utf8').rstrip(';'))
                data_sensor = int(data.decode('utf8').rstrip(';'))
                average += data_sensor
                sample += 1
                if sample == sampling:
                    sensor = int(average/sampling)
                    average = 0
                    sample = 0

                    graph.sensor = sensor
                    t2 = threading.Thread(target=graph_control, args=(graph, ))
                    t2.deamon = True
                    t2.start()
                print(sensor)

            except:
                pass
def connection():
    global ser, serialData
    if connect_btn["text"] in "Disconnect":
        serialData = False
        connect_btn["text"] = "Connect"
        refresh_btn["state"] = "active"
        drop_bd["state"] = "active"
        drop_COM["state"] = "active"

    else:
        serialData = True
        connect_btn["text"] = "Disconnect"
        refresh_btn["state"] = "disable"
        drop_bd["state"] = "disable"
        drop_COM["state"] = "disable"
        port = clicked_com.get()
        baud = clicked_bd.get()
        #print(port, baud)
        try:
           ser = serial.Serial(port, baud, timeout=0)
        except:
            pass
        t1 = threading.Thread(target=readSerial)
        t1.daemon = True
        t1.start()


def close_window():
    global root, serialData
    serialData = False
    root.destroy()

connect_menu_init()
root.protocol("WM_DELETE_WINDOW", close_window)

root.mainloop()