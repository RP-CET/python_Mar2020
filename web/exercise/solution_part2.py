import csv

readerFileHandle = open("data.csv","r", newline='')
reader1 = csv.reader(readerFileHandle)

total = 0
count = 0
for row in reader1:
	print(row)
	total = total + float(row[1])
	count += 1

readerFileHandle.close()

average = total / count
print ("Average temperature is : " + str(average))