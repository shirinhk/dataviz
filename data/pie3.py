import matplotlib.pyplot as plt
import numpy as np

y = np.array([0, 93, 5, 269, 179, 98])
sports = ['Biathlon', 'Bobsleigh', 'Curling','Ice hockey','Skating','Skiing']

plt.pie(y, labels = sports)
plt.xlabel("USA")
plt.title("Which Sport had Most Medal", pad="20")

plt.show() 

