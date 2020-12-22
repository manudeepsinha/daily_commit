#Importing pyplot submodule
import matplotlib.pyplot as plt
import numpy as np

#defining graph 1
y= np.array([0,17,6,42,20])

#using subplot() to show more than one graphs
plt.subplot(1,2,1)
plt.plot(y)
#using title() to add name to a particular graph
plt.title('SALES')

#defining graph 2
y= np.array([0,4,6,18,20])

plt.subplot(1,2,2)
plt.plot(y)
plt.title('INCOME')

#using suptitle() to add title to entire figure
plt.suptitle('MY SHOP')
plt.show()
