import serial
import time


global row
ser = serial.Serial('COM3', baudrate=9600, timeout=1)
time.sleep(3)
numPoints = 1
dataList = [0]*numPoints
dataLog = open('dataLog.txt', 'w')


def getValues(timeStamp):
    if timeStamp == 'false':
        arduinoData = ser.readline().decode().split('\r\n')
        arduinoOutput = arduinoData[0]
    if timeStamp == 'true':
        ser.write(b'c')
        arduinoOutput = ser.readline().decode().split(' ')

    return arduinoOutput


def printToFile(data, index):
    dataLog.write(data)
    if index != (numPoints - 1):
        dataLog.write(',')
    else:
        dataLog.write('\n')


def getAverage(dataSet, row1):

    dataAvg = sum(dataSet) / len(dataSet)
    print('Average for ' + str(row1) + ' is: ' + str(dataAvg))


while 1:
    global row1
    userInput = input('Get data points ')

    if userInput == 'y':
        timeStamp = 'false'
        for i in range(0, numPoints):
            data = getValues(timeStamp)
            printToFile(data, i)
            dataList[i] = data
        #getAverage(dataList, row1)

    if userInput == 'c':
        timeStamp = 'true'
        data = getValues(timeStamp)
        dataPoint = data[0]
        timeCollected = data[1]
        timeCollected = timeCollected.strip()
        unitTime = timeCollected[-2:]
        deltaTime = timeCollected[:-2]

        if unitTime == 'ms':
            timeValue = int(deltaTime)
            timeValue = timeValue / 1000

        if unitTime == 'us':
            timeValue = int(deltaTime)
            timeValue = timeValue / 1000000

        print('Data Point: ' + dataPoint +
                  '  Time from last point: ' + str(timeValue) + 's')

    if userInput == 'n':
    #print(dataList)
        dataLog.close()
    #break
