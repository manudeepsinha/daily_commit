#Importing pyplot submodule
import matplotlib.pyplot as plt
import numpy as np

#defining x and y coordinates using numpy array
abscissa = np.array([0,6])
ordinate = np.array([0,265])

#using plot() and passing x and y coordinates to plot the line
plt.plot(abscissa, ordinate)

#using show() to show the generated output
plt.show()