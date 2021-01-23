''' The following code is the first step towards making a social distancing project. 
	One milestone will be face recognition. till then, all the integration will be done
	on this code only.
'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
  ret, frame = cap.read()
  frame = cv2.flip(frame, -1) #flips camera vertically
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  cv2.imshow('frame', frame)
  cv2.imshow('gray', gray)

  k = cv2.waitKey(30) & 0xff
  if k == 27: #press 'ESC' to quit
    break

cap.release()
cv2.destroyAllWindows()