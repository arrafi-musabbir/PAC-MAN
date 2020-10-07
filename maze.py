import cv2 as cv
#import numpy as np

#imat = np.array(12,12)

i = cv.imread("D:/github/PAC-MAN/maze1.png", cv.IMREAD_GRAYSCALE)
res = cv.resize(i, (800, 800))

cv.imshow('image', res)
cv.waitKey(5000)
cv.destroyAllWindows()


for i in range(len(res)):
    for j in range(i):
        if res[i][j]>87:
            print(res[i][j])
