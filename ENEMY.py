import pygame
import GAME
import ingame_variables as iv
import random

vec = pygame.math.Vector2


class Enemy:

    def __init__(self, Game, pos, colour, personality):
        self.Game = Game
        self.e_colour = colour
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.personality = personality
        self.fg = 0
    def update(self):
        self.pix_pos += self.direction
        if self.when_to_move():
            self.move()

        # updating grip position
        self.grid_pos.x = (((self.pix_pos.x
                             - iv.top_bottom_buffer
                             + self.Game.cell_width // 2)
                            // self.Game.cell_width) - 0.1)
        self.grid_pos.y = (((self.pix_pos.y
                             - iv.top_bottom_buffer
                             + self.Game.cell_height // 2)
                            // self.Game.cell_height) + 0.2)

    def get_pix_pos(self):
        return vec(int(self.grid_pos.x * self.Game.cell_width)
                   + iv.top_bottom_buffer // 1.15,
                   int(self.grid_pos.y * self.Game.cell_height)
                   + iv.top_bottom_buffer // 1.1)

    def appear(self):
        pygame.draw.circle(self.Game.screen, self.e_colour,
                           (int(self.pix_pos.x), int(self.pix_pos.y)),
                           self.Game.cell_width + 8)

    def can_move(self, d):
        temp = self.pix_pos + d
        if (self.Game.map[(int(temp[0] - iv.top_bottom_buffer // 2)),
                          (int(temp[1] - iv.top_bottom_buffer // 2))]) == 255:
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
        return False

    def set_personality(self):
        if self.personality == "r":
            return "random"
        if self.personality == "b":
            return "bfs"

    def move(self):
        if self.set_personality() == "random":
            self.direction = self.get_random()
        elif self.set_personality() == "bfs":
            self.direction = self.get_bfs()

    def get_random(self):
        if self.can_move(self.direction):
            return self.direction
        else:
            while True:
                directions = [vec(0, 1), vec(1, 0), vec(-1, 0), vec(0, -1)]
                d = random.choice(directions)
                if self.can_move(d):
                    break
            return d

    def get_bfs(self):
        start = self.pix_pos
        goal = self.Game.player.pix_pos
        queue = [start]
        path = list()
        visited = list()
        neighbors = [vec(0, 100), vec(100, 0), vec(-100, 0), vec(0, -100)]
        while queue:
            current = queue.pop(0)
            visited.append(current)
            if current == goal:
                break
            else:
                for neighbor in neighbors:
                    if ((int(neighbor[0]+self.pix_pos[0] - iv.top_bottom_buffer // 2)) > 0 and (int(neighbor[1]+self.pix_pos[1] - iv.top_bottom_buffer // 2)) > 0):
                        if self.can_move(neighbor):
                            next_pixel = current + neighbor
                            if next_pixel not in visited:
                                queue.append(next_pixel)
                                path.append({"current": current,
                                            "Next cell": next_pixel})
            self.fg += 1
            print(self.fg)
        # print("done")
        shortest = [goal]
        while goal != start:
            if goal == start:
                break
            for step in path:
                if goal == start:
                    break
                if step["Next cell"] == goal:
                    goal = step["current"]
                    shortest.insert(0, step["current"])
            # print("yo")
        return shortest[0]
