import csv

readerFileHandle = open("W65Z.csv","r", newline='')
reader1 = csv.reader(readerFileHandle)
#using for loop to retrieve from the CSV file lune by line
for row in reader1:
	print(row)

readerFileHandle.close()
