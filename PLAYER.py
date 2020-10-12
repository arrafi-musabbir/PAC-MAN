import MAZE as mz
import pygame
import ingame_variables as iv
import GAME
vec = pygame.math.Vector2
pygame.init()


class Player:

    def __init__(self, Game, pos):
        self.Game = Game
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True

    def update(self):

        if self.able_to_move:
            self.pix_pos += self.direction
        if self.when_to_move():
            if self.stored_direction is not None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()
        self.grid_pos.x = (((self.pix_pos.x
                             - iv.top_bottom_buffer
                             + self.Game.cell_width // 2)
                            // self.Game.cell_width) - 0.1)
        self.grid_pos.y = (((self.pix_pos.y
                             - iv.top_bottom_buffer
                             + self.Game.cell_height // 2)
                            // self.Game.cell_height) + 0.2)
        print("pix pos ", self.pix_pos)
        print("Grid pos ", self.grid_pos)
        print("maze ", self.Game.arr[int(self.pix_pos.y)-25][int(self.pix_pos.x)-25])
        # print("one")

    def appear(self):
        pygame.draw.circle(self.Game.screen, iv.PLAYER_COLOUR,
                           (int(self.pix_pos.x), int(self.pix_pos.y)),
                           self.Game.cell_width + 5)
        # pygame.draw.rect(self.Game.screen, iv.RED,
        #                  ((self.grid_pos.x * self.Game.cell_width)
        #                   + iv.top_bottom_buffer // 1,
        #                   (self.grid_pos.y * self.Game.cell_height)
        #                   + iv.top_bottom_buffer // 1.15,
        #                   self.Game.cell_width, self.Game.cell_height), 1)

    def move(self, direction):
        self.direction = direction

    def can_move(self):
        if self.Game.arr[int(self.pix_pos.y)-25][int(self.pix_pos.x)-25] == 255:
            return False
        # for wall in self.Game.walls:
        #     if vec(self.grid_pos+self.direction) == wall:
        #         return False
        else:
            return True

    def when_to_move(self):
        if (int(self.pix_pos.x + iv.top_bottom_buffer // 2) %
                self.Game.cell_width == 0):
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                return True
        if (int(self.pix_pos.y + iv.top_bottom_buffer // 2) %
                self.Game.cell_height == 0):
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                return True

    def get_pix_pos(self):
        return vec(int(self.grid_pos.x * self.Game.cell_width)
                   + iv.top_bottom_buffer // 1.15,
                   int(self.grid_pos.y * self.Game.cell_height)
                   + iv.top_bottom_buffer // 1.1)
