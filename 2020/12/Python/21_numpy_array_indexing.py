#importing the module 
import numpy as np

arr0d = np.array(42)
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#Accessing 0D array is direct, i.r. w/o any index passing
print(arr0d)

#Accessing 1D array is by passing the index number
print(arr1d[2])
#This will print 3rd element of the array

#Accessing 2D array is by passing the array number followed by index number seperated by a comma
print(arr2d[1,0])
#This will print 1st elemnt of the second array

#Accessing 3D array is by passing the 1st array number followed by 2nd array number and then index number, all seperated by a comma
print(arr2d[0,1,0])
#This will print 1st elemnt of the second array of the first array