#Importing pyplot submodule
import matplotlib.pyplot as plt
import numpy as np

#for simplicity, randomly generating an array with 250 vals that concentrate around 100, and the standard deviation is 10
x = np.array([100,45,60,90])
my_labels = np.array(['Apples','Bananas','Lichi','Pineapple'])
my_explode = np.array([0.2,0,0,0])

#using pie() to generate a pie chart, arguments labels will put label on each wedge, shadow will ensure to add shadow and explode will magnify a wedge
#by its given input
#labels and explode will take ab array as input and the elements of the array must match the number of elements in the pie chart
plt.pie(x,  shadow = True, explode = my_explode, startangle=90 )

#legend() will print out the list of all the wedges will their respective colors, passing title will add title to the list generated
plt.legend(labels = my_labels,title = 'Four Fruits:', loc="best")
plt.title('Prices of fruits per kg')
plt.show()
