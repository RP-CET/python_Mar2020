import matplotlib.pyplot as plt

#set up values
VALUESA = [100,150,125,170]
VALUESB = [0,15,40,80]
POS = [0,1,2,3]
LABELS = ['Q1 2018','Q2 2018','Q3 2018','Q4 2018']

#set up the first bar
plt.bar(POS,VALUESB)
#set up the stacked bars
plt.bar(POS,VALUESA,bottom=VALUESB)
plt.xticks(POS, LABELS)
plt.ylabel('Sales')
plt.xticks(POS, LABELS)

#to display the chart
plt.show()
