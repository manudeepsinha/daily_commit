#exploring OpenCV
import cv2

#image is present in the same directory as this notebook
#using imread() to load/read an image
image = cv2.imread('road.jpg')

#printing the list of shape aspects of the image, i.e. height, width
print(image.shape)

#saving the height and width of image in h and w variables
h,w = image.shape[:2]

#the colors in OpenCV is in the format BGR instead of conventional RGB
#taking a random pixel by passing 100 for height and 100 for width
(B, G, R) = image[100,100]

#displaying the pixel values
print(f'Blue: {B} Red: {R} Green: {G}')

#extracting region of interest (roi) by slicing the pixels of the image
roi = image[100: 450, 200: 550]

#resizing the image by resize() and passing 2 parameters, image and the dimension
resize = cv2.resize(image, (600,600))

#to retain the aspect ratio of the image
#calculating the ratio
ratio = 600/w

#creating a tuple containing height and width
dim = (600, int(h*ratio))

#finally resizing
resize_aspect = cv2.resize(image, dim)

#rotating the image by 45 degree anticlockwise
#finding the center
center = (w//2, h//2)

#generating rotation matrix taking parameters of center, degree of rotation, scaling factor
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

#performing the affine transformation
rotated = cv2.warpAffine(image, matrix, (w,h))