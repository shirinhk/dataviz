import matplotlib.pyplot as plt
import numpy as np

sports = ['Biathlon', 'Bobsleigh', 'Curling','Ice hockey','Skating','Skiing']
Womenmedal = [2,4,10,81,14,12]
plt.scatter(sports, Womenmedal, color=(100/255, 0/255, 20/255), linewidth=3.0)

sports = ['Biathlon', 'Bobsleigh', 'Curling','Ice hockey','Skating','Skiing']
Menmedal = [0,8,15,139,25,5]
plt.scatter(sports, Menmedal, color=(0/255, 100/255, 100/255), linewidth=3.0)


plt.ylabel("Gold Medals Achieved")
plt.xlabel("Sports")

plt.title("Women vs Men in Canada", pad="20")


plt.show()