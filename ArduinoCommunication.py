import serial
import time
from ini_read import getINI

iniData = getINI()
numRowsCollect = int(iniData['numRowsCollect'])
numPoints = int(iniData['numPoints'])

ser = serial.Serial("COM3", baudrate=9600, timeout=1)
time.sleep(3)

dataFile = open('dataFile.txt', 'w')
dataList = [0]*numPoints


def getValues():
    ser.write(b'g')
    arduinoData = ser.readline().decode().split('\r\n')  #("ascii")

    #print(type(arduinoData))
    #print('arduinoData[0]: ')
    #print(arduinoData[0])
    #print(type(arduinoData[0]))
    #print('arduinoData[1]: ')
    #print(arduinoData[1])
    #print(type(arduinoData[1]))

    return arduinoData[0]


def printToFile(data, index):
    dataFile.write(data)
    if index != (numPoints - 1):
        dataFile.write(',')
    else:
        dataFile.write('\n')


def getAverage(dataSet, row):

    dataAvg = sum(dataSet) / len(dataSet)
    print('Average for ' + str(row) + ' is: ' + str(dataAvg))


while 1:
    userInput = input('Get data points?')

    if userInput == 'y':
        for row in range(0, numRowsCollect):
            for i in range(0, numPoints):
                data = getValues()
                #dataFile.write(data + ' ')
                #data = float(data)
                printToFile(data, i)
                #dataInt = int(data)
                dataList[i] = data    # dataList[i] = dataInt

            #print(sum(dataList)/numPoints)
            #getAverage(dataList, row)
            print(dataList, row)


        dataFile.close()
        break