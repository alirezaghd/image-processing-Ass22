import cv2 as cv
import numpy as np

a = cv.imread('a.tif')
b = cv.imread('b.tif')

a = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
b = cv.cvtColor(b,cv.COLOR_RGB2GRAY)

b = 255 - b
a = 255 - a

res = cv.subtract(a,b)
cv.imshow('output',res)
cv.imwrite('ramz.jpg',res)

cv.waitKey()
