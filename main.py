import cv2
import numpy as np
images = []

for i in range(0,15):
    img = cv2.imread(f'h{i}.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    images.append(img)


res = np.zeros(images[0].shape, dtype='uint8')
for image in images:
    res += image // len(images)

cv2.imshow('sdf',res)

cv2.waitKey()