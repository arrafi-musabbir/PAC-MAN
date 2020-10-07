import cv2 as cv
import numpy as np
import ingame_variables as iv


class Maze:

    def __init__(self, img_path):
        self.img_path = img_path
        self.arr = np.zeros([iv.mwidth, iv.mheight])
        self.walls = self.mazify()

    def mazify(self):
        i = cv.imread(self.img_path, cv.IMREAD_GRAYSCALE)
        res = cv.resize(i, (iv.mwidth, iv.mheight))
        for i in range(len(res)):
            for j in range(len(res)):
                if res[i][j] > 0:
                    res[i][j] = 1
        res[0:15, 0:] = 1
        res[0:, 0:15] = 1
        res[785:800, 0:] = 1
        res[0:, 785:800] = 1
        for row in range(len(res)):
            for col in range(len(res)):
                self.arr[row][col] = res[row][col]
        # cv.imshow('image', res)
        # cv.waitKey(2000)
        # cv.destroyAllWindows()
