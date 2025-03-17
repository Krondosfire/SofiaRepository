import matplotlib.pyplot as plt
import csv

plt.style.use('dark_background')
x = []
y = []
y1 = []

with open('analog-data1.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(str(row[0]))
        y.append(str(row[1]))
        #y1.append(str(row[2]))

plt.plot(x, y, y1, color='g', linestyle='dashed',
         marker='o', label="Temp Data")

plt.xticks(rotation=25)
plt.xlabel('Date/Time')
plt.ylabel('Temperature(°C)')
#plt.y1label('Temperature(°C)')
plt.title('Temp Report', fontsize=20)
plt.grid()
plt.legend()
plt.show()