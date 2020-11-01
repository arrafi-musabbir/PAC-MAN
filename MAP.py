import numpy as np
import ingame_variables as iv
import pygame
vec = pygame.math.Vector2


class Map:

    def __init__(self):
        # self.imgarr = np.load(iv.maze_npy)
        self.map_dic = {}
        self.coins = []
        self.map_tiles = {}

    def load_map(self):
        for i in range(len(self.imgarr)):
            for j in range(len(self.imgarr)):
                self.map_dic[(j, i)] = self.imgarr[i][j]

        return self.map_dic

    def read_tiles(self):
        lis = list()
        with open(iv.tiles_txt, "r") as f:
            for line in f:
                for i in line:
                    if i != " " and i != "\n":
                        lis.append(int(i.strip()))

        for i in range(iv.rows):
            for j in range(iv.collumns):
                self.map_tiles[(j, i)] = lis.pop(0)

        return self.map_tiles

if __name__ == '__main__':
    m = Map()
    f = m.read_tiles()
    # g = m.load_map()
    print(f)
#     print(g)
    # print(f[2][2])
