import csv

readerFileHandle = open("W65Z.csv","r", newline='')
reader1 = csv.reader(readerFileHandle)


#use a (for) loop to retrieve data from the CSV file line by line
output = "yes"
for row in reader1:
    if output == "yes":
        print(row)
        output = "no"
    else:
        #no printing
        output = "yes"


readerFileHandle.close()
