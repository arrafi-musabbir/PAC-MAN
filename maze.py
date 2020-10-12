import cv2 as cv
import numpy as np
import ingame_variables as iv
import pygame
pygame.init()


class Maze:

    def __init__(self):
        self.img_path = iv.maze_path
        self.arr = np.zeros([iv.mwidth, iv.mheight])

    def mazify(self):
        i = cv.imread(self.img_path, cv.IMREAD_GRAYSCALE)
        res = cv.resize(i, (iv.mwidth, iv.mheight))
        for i in range(iv.mwidth):
            for j in range(iv.mheight):
                if res[i][j] > 0:
                    res[i][j] = 255
        res[0:15, 0:] = 255
        res[0:, 0:15] = 255
        res[785:800, 0:] = 255
        res[0:, 785:800] = 255
        # for row in range(len(res)):
        #     for col in range(len(res)):
        #         self.arr[row][col] = res[row][col]
        # cv.imshow('image', res)
        # cv.waitKey(10000)
        # cv.destroyAllWindows()
        # print(res[248][70])
        return res

    def imgarr(self):
        self.arr = self.mazify()
        return self.arr
# m = Maze().mazify()
