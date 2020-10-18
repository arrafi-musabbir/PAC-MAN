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
        res[785:800, 0:] = 255
        res[0:, 785:800] = 255
        self.coined(res)
        return res

    # def imgdic(self):
    #     self.arr = self.mazify()
    #     dic = dict()
    #     for x in range(iv.mwidth):
    #         for y in range(iv.mheight):
    #             dic[(y, x)] = self.arr[x][y]
    #     return dic

    def coined(self, tarr):
        for i in range(50, iv.mwidth-50, 20):
            for j in range(50, iv.mheight-49, 20):
                if tarr[i][j] != 255:
                    for x in range(i-50, i+50):
                        for y in range(j-50, j+50):
                            if tarr[x][y] != 255:
                                tarr[i][j] = 180
        return tarr

    def write_to_txt(self):
        self.arr = self.mazify()
        np.save("D:/github/PAC-MAN/maze.npy", self.arr)
            
#     def printimg(self):
#         # t = self.imgarr()
#         cv.imshow('image', self.imgarr())
#         cv.waitKey(10000)
#         cv.destroyAllWindows()
#
m = Maze()
m.write_to_txt()
