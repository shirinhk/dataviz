import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 22, 50, 351, 159,40 ])
sports = ['Biathlon', 'Bobsleigh', 'Curling','Ice hockey','Skating','Skiing']

plt.pie(y, labels = sports)
plt.xlabel("Canada")
plt.title("Which Sport had Most Medal", pad="20")

plt.show() 

