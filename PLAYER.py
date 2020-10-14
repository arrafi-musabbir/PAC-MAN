import MAZE as mz
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

        if self.able_to_move:
            self.pix_pos += self.direction
        if self.when_to_move():
            if self.stored_direction is not None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()
        if self.on_coins():
            self.eat_coins()
        self.grid_pos.x = (((self.pix_pos.x
                             - iv.top_bottom_buffer
                             + self.Game.cell_width // 2)
                            // self.Game.cell_width) - 0.1)
        self.grid_pos.y = (((self.pix_pos.y
                             - iv.top_bottom_buffer
                             + self.Game.cell_height // 2)
                            // self.Game.cell_height) + 0.2)

        # print("pix pos ", self.pix_pos)
        # print("maze ", self.Game.arr[int(self.pix_pos.y) - 25]
        #                             [int(self.pix_pos.x) - 25])

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
        self.stored_direction = direction

    def on_coins(self):
        temp = self.pix_pos - vec(25, 25)
        if temp in self.Game.coins:
            self.Game.coins.remove(temp)
            return True
        else:
            return False

    def eat_coins(self):
        print("eaten")
        self.current_score += 1

    def can_move(self):
        temp = self.pix_pos + self.direction
        if (self.Game.arr[int(temp[1] - iv.top_bottom_buffer // 2)]
                [int(temp[0] - iv.top_bottom_buffer // 2)]) == 255:
            return False
        else:
            return True

    def when_to_move(self):
        if (int(self.pix_pos.x + (iv.top_bottom_buffer // 2)) %
                self.Game.cell_width == 0):
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                return True
        if (int(self.pix_pos.y + (iv.top_bottom_buffer // 2)) %
                self.Game.cell_height == 0):
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                return True

    def get_pix_pos(self):
        return vec(int(self.grid_pos.x * self.Game.cell_width)
                   + iv.top_bottom_buffer // 1.15,
                   int(self.grid_pos.y * self.Game.cell_height)
                   + iv.top_bottom_buffer // 1.1)
