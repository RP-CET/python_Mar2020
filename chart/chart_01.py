import matplotlib.pyplot as plt

#set up values
VALUES = [100,150,125,170]
POS = [0,1,2,3]
LABELS = ['Q1 2018','Q2 2018','Q3 2018','Q4 2018']

#set up the chart
plt.bar(POS,VALUES)
plt.xticks(POS, LABELS)
plt.ylabel('Sales')

#to display the chart
plt.show()
