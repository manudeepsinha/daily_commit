#Importing numpy module
import numpy as np

#making a 3D array
arr3d = np.array([[[1, 2, 3],[4,5,6]],[[7,8,9],[10,11,12]]])

#making a 5D array
arr5d = np.array([1,2,3, 4], ndmin=5)

print('3D array is as follows: ')
print(arr3d)
print('\n5D array is as follows: ')
print(arr5d)
print('\nnumber of dimensions in 3D array :', arr3d.ndim) 
print('\nnumber of dimensions in 5D array :', arr5d.ndim)