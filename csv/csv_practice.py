import csv

readerFileHandle = open("W65Z.csv","r", newline='')
reader1 = csv.reader(readerFileHandle)
#using for loop to retrieve from the CSV file lune by line
output = 1
for row in reader1:
    if output == 0:
        print(row)
        output = 1
    else:
        output = 0

readerFileHandle.close()
