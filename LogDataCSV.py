import serial

arduino_port = "COM3" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName = "analog-data1.csv" #name of the CSV file generated
ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)


def createCSV():

    file = open(fileName, "a")
    print("Created file")
    samples = 20  # how many samples to collect
    print_labels = False
    line = 0  # start at 0 because our header is 0 (not real data)

    while line <= samples:
        if print_labels:
            if line == 0:
                print("Printing Column Headers")
            else:
                print("Line " + str(line) + ": writing...")
        getData = str(ser.readline().decode())
        data = getData[0:][:-2]
        print(data)

        file = open(fileName, "a")
        file.write(data + "\n") #write data with a newline
        line = line+1

    print("Data collection complete!")
    file.close()
