import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def format_minutes(value, pos):
	return '{}m'.format(int(value))

def format_dollars(value, pos):
	return '${}'.format(value)

# read data from csv
fp = open("scatter.csv","r", newline='')
reader = csv.reader(fp)
data = list(reader)

data_x=[]
data_y=[]
for x, y in data:
	data_x.append(float(x))
	data_y.append(float(y))
	
plt.scatter(data_x, data_y)

plt.gca().xaxis.set_major_formatter(FuncFormatter(format_minutes))
plt.xlabel('Time in website')
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_dollars))
plt.ylabel('Spending')

plt.show()
