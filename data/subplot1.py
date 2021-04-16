import matplotlib.pyplot as plt
import numpy as np

#plot 1:
sports = ['Biathlon', 'Bobsleigh', 'Curling','Ice hockey','Skating','Skiing']
medals = [3, 22, 50, 351, 159,40 ]

plt.subplot(2, 1, 1)
plt.plot(sports,medals,color=(0/255, 100/255, 100/255), linewidth=3.0)
plt.ylabel("Canada")

#plot 2:
sports = ['Biathlon', 'Bobsleigh', 'Curling','Ice hockey','Skating','Skiing']
medals = [0, 93, 5, 269, 179, 98]

plt.subplot(2, 1, 2)
plt.plot(sports,medals,color=(0/255, 100/255, 100/255), linewidth=3.0)
plt.ylabel("USA")


plt.show()