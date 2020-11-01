# import MAZE as mz
import pygame
import ingame_variables as iv
import GAME
pygame.init()
vec = pygame.math.Vector2


class Player:

    def __init__(self, Game, pos):
        self.Game = Game
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.move(self.direction)
        self.able_to_move = True
        self.current_score = 0

    def update(self):
        # print("pix", self.pix_pos)
        # print("grid", self.grid_pos)
        if self.when_to_move():
            if self.stored_direction is not None:
                self.direction = self.stored_direction
                self.able_to_move = self.can_move()
        if self.able_to_move:
            self.pix_pos += self.direction
        if self.on_coins():
            self.eat_coins()
        self.grid_pos[0] = (self.pix_pos[0] - iv.tbf -
                            self.Game.cell_width // 2)
        self.grid_pos[1] = (self.pix_pos[1] - iv.tbf -
                            self.Game.cell_width // 2)

    def get_pix_pos(self):
        return vec(int(self.grid_pos.x * self.Game.cell_width)
                   + iv.tbf,
                   int(self.grid_pos.y * self.Game.cell_height)
                   + iv.tbf)

    def appear(self):
        pygame.draw.circle(self.Game.screen, iv.PLAYER_COLOUR,
                           (int(self.pix_pos.x), int(self.pix_pos.y)),
                           self.Game.cell_width // 2)

    def move(self, direction):
        self.stored_direction = direction

    def on_coins(self):
        temp = self.grid_pos // self.Game.cell_width
        if temp in self.Game.coins:
            self.Game.coins.remove(temp)
            return True
        return False

    def eat_coins(self):
        self.current_score += 1

    def can_move(self):
        temp = self.grid_pos // self.Game.cell_width + self.direction
        # print(temp)
        if temp[0] < 0 and temp[1] < 0:
            return False
        else:
            if self.Game.tiles[(temp[0], temp[1])] == 1:
                return False
        return True

    def when_to_move(self):
        if (self.grid_pos.x % self.Game.cell_width == 0):
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if (self.grid_pos.y % self.Game.cell_height == 0):
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True
