import numpy as np
import ingame_variables as iv
import pygame
vec = pygame.math.Vector2


class Map:

    def __init__(self):
        self.imgarr = np.load(iv.maze_npy)
        self.map_dic = {}
        self.coins = []

    def load_map(self):
        for i in range(len(self.imgarr)):
            for j in range(len(self.imgarr)):
                self.map_dic[(j, i)] = self.imgarr[i][j]

        return self.map_dic

    def load_coins(self):
        for key in self.map_dic.keys():
            if self.map_dic[key] == 180:
                self.coins.append(vec(key))
        return self.coins

# m= Map()
# f = m.load_map()
# print(f)
