import cv2 as cv
import numpy as np
import ingame_variables as iv

class Maze:

    def __init__(self):
        self.img_path = iv.maze_path
        self.arr = np.zeros([iv.mwidth, iv.mheight])

    def mazify(self):
        i = cv.imread(self.img_path, cv.IMREAD_GRAYSCALE)
        res = cv.resize(i, (iv.mwidth, iv.mheight))
        for i in range(iv.mwidth):
            for j in range(iv.mheight):
                if res[i][j] == 255:
                    res[i][j] = 100
                if res[i][j] > 0 and res[i][j] != 100:
                    res[i][j] = 255
        res[0:15, 0:] = 255
        res[0:, 0:15] = 255
        res[iv.mwidth-15:iv.mwidth, 0:] = 255
        res[0:, iv.mheight-15:iv.mheight] = 255
        self.coined(res)
        return res

    # def imgdic(self):
    #     self.arr = self.mazify()
    #     dic = dict()
    #     for x in range(iv.mwidth):
    #         for y in range(iv.mheight):
    #             dic[(y, x)] = self.arr[x][y]
    #     return dic


    def write_to_txt(self):
        self.arr = self.mazify()
        np.save("D:/github/PAC-MAN/maze.npy", self.arr)

    # def printimg(self):
    #     t = self.mazify()
    #     cv.imshow('image', t)
    #     cv.waitKey(10000)
    #     cv.destroyAllWindows()
# #


m = Maze()
m.write_to_txt()
# m.printimg()
