#Importing pyplot submodule
import matplotlib.pyplot as plt
import numpy as np

#defining y coordinates using numpy array
ordinate = np.array([0,17,6,42,20])

#using plot() and passing y coordinates along with fmt parameters as marker|line|color
plt.plot(ordinate, 'd-.r')

#using show() to show the generated output
plt.show()