import cv2 as cv

img = cv.imread('board - origin.bmp')
test = cv.imread('board - test.bmp')

img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
test = cv.cvtColor(test,cv.COLOR_RGB2GRAY)
test = cv.flip(test,1)
res = cv.subtract(test,img) *3


cv.imshow('output',res)
cv.imwrite('board-test-res.bmp',res)

cv.waitKey()