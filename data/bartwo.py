import matplotlib.pyplot as plt
   
country = ['Canada','USA','Norway','Germany','Sweden','Russia','Austria','Switzerland','Finland']
goldMedals = [315,167,159,137,127,94,79,76,66]

plt.barh(country, goldMedals, color=(0/255, 100/255, 100/255), linewidth=3.0)

plt.ylabel("Country")
plt.xlabel("Gold Medals")

#add a title to the chart
plt.title("Most Gold Medals", pad="20")

plt.show()