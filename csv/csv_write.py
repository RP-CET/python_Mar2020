import csv

writerFileHandle = open("new.csv", "w", newline='')
writer1 = csv.writer(writerFileHandle)
row1 = ["Arron","D","X","X","X","X"]
row2 = ["Bert","A","X","C","B","X"]
row3 = ["Bradley","C","A","C","X","X"]
rowlist = [row1,row2,row3]

for row in rowlist:
	writer1.writerow(row)

writerFileHandle.close()

