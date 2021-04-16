import matplotlib.pyplot as plt
  
# women
sports = ['Biathlon', 'Bobsleigh', 'Curling','Ice hockey','Skating','Skiing']
Womenmedal = [2,4,10,81,14,12]
# plotting the line 1 points 
plt.plot(sports, Womenmedal, label = "Women's Gold Medal",color=(100/255, 0/255, 20/255), linewidth=3.0)
  
# men
sports = ['Biathlon', 'Bobsleigh', 'Curling','Ice hockey','Skating','Skiing']
Menmedal = [0,8,15,139,25,5]
# plotting the line 2 points 
plt.plot(sports, Menmedal, label = "Men's Gold Medal",color=(0/255, 100/255, 100/255), linewidth=3.0)
  
# naming the x axis
plt.xlabel("Sports")
# naming the y axis
plt.ylabel('Women Vs Men')
# giving a title to my graph
plt.title("Gold Medal in Canada by Gender", pad="20")
  
# show a legend on the plot
plt.legend()
  
# function to show the plot
plt.show()