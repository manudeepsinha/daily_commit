#Importing pyplot submodule
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Apples','Bananas','Lichi','Pineapple'])
y = np.array([100,45,60,90])

#using bar() to represent data in bar graph
plt.subplot(1,2,2)
plt.bar(x,y, width = 0.5)
plt.title('Vertical')
plt.show() 


#for showing the graph horizontally, barh() is used and instead of width, height is used
plt.subplot(1,2,1)
plt.barh(x,y, height = 0.5)
plt.title('Horizontal')

plt.suptitle('Prices of fruits per kg')
plt.show() 
