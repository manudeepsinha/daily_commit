#Importing pyplot submodule
import matplotlib.pyplot as plt
import numpy as np

#for simplicity, randomly generating an array with 250 vals that concentrate around 100, and the standard deviation is 10
x = np.random.normal(170,10,250)

#using hist() to generate a histogram, passing array as an argument
plt.hist(x)
plt.title('Heights of 250 persons in cm')
plt.show()
