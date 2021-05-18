import numpy as np
my_dict = {}
genes={'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
import matplotlib.pyplot as plt
labels = 'USA','India','Brazil','Russia','UK'
#These five conuntries is the five part of the circle
sizes = '29862124','11285561','11205972','4360823','4234924'
explode = (0,0,0,0,0)
#To make it no interval in the circle
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('Coronavirus rates ')
plt.show()
