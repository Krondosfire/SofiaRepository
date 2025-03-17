import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM3',9600)
time.sleep(2)
data =[]
for i in range(50):
    b = ser.readline()
    str_rn = b.decode().rstrip()
    #str = str_rn
    f = int(str_rn)
    print(f)
    data.append(f)  # add to the end of data list
    time.sleep(0.1)
# show the data

for line in data:
    print(line)

plt.plot(data)
plt.xlabel('Time (seconds)')
plt.ylabel('Temp Reading')
plt.title('Temperature Reading vs. Time')
plt.show()
ser.close()
#exit()
