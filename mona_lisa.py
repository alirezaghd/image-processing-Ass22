import cv2 as cv
import numpy as np

img = cv.imread('Mona_Lisa.jpg')
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
mask = np.ndarray((775,512), dtype=np.uint8)
for i in range(512):
    mask[:,i] = i / 2

mask[:,0:2] = 1

res = img / mask

cv.imshow('output',res)
cv.imwrite('mona_lisa_edit.tif',res)

cv.waitKey()