import matplotlib.pyplot as plt

#set up values
VALUESA = [100,150,125,170]
VALUESB = [0,15,40,80]
VALUESC = [3,5,7,3]
POS = [0,1,2,3]
LABELS = ['Q1 2018','Q2 2018','Q3 2018','Q4 2018']

# Create the first plot
plt.subplot(2,1,1)

#creata a bar graph with informaton about VALUESA
plt.bar(POS,VALUESA)
plt.ylabel('Sales')

#create a different Y axis, and add information 
#about VALUESB as a line plot
plt.twinx()
plt.plot(POS,VALUESB,'o-',color='red')
plt.xticks(POS, LABELS)
plt.ylabel('Sales B')
plt.xticks(POS, LABELS)

#create another subplot and fill it iwth VALUESC
plt.subplot(2,1,2)
plt.plot(POS, VALUESC)
plt.gca().set_ylim(bottom=0)
plt.xticks(POS,LABELS)

plt.savefig('foo.png')

plt.show()
