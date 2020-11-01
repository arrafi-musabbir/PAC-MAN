import pygame
import GAME
import ingame_variables as iv
import random
pygame.init()
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
        # print(self.pix_pos)
        if self.when_to_move():
            self.move()

        # updating grip position
        self.grid_pos.x = (((self.pix_pos[0]
                             - iv.top_bottom_buffer
                             + self.Game.cell_width // 2)
                            // self.Game.cell_width) - 0.1)
        self.grid_pos.y = (((self.pix_pos[1]
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
                           (int(self.pix_pos[0]), int(self.pix_pos[1])),
                           self.Game.cell_width + 6)

    def can_move(self, d):
        temp = self.pix_pos + d
        if (self.Game.map[(int(temp[0] - iv.top_bottom_buffer // 2)),
                          (int(temp[1] - iv.top_bottom_buffer // 2))]) == 255:
            return False
        return True

    def when_to_move(self):
        if (int(self.pix_pos[0] + (iv.top_bottom_buffer // 2)) %
                self.Game.cell_width == 0):
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                return True
        if (int(self.pix_pos[1] + (iv.top_bottom_buffer // 2)) %
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
            self.direction = self.run_bfs()

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

    def run_bfs(self):
        start = self.pix_pos
        goal = self.get_bfs()
        mod_gol = (goal[0]*25+12, goal[1]*25+12)
        target=vec(int(mod_gol[0] * self.Game.cell_width)
                   + iv.top_bottom_buffer // 1.15,
                   int(mod_gol[1] * self.Game.cell_height)
                   + iv.top_bottom_buffer // 1.1)
        # self.pix_pos = mod_gol
        print("START", start)
        print("GOAL", mod_gol)
        print("START", start)
        print("GOAL", mod_gol)
        return target

    def get_bfs(self):
        mapt = self.Game.tiles
        enemy = self.pix_pos
        player = self.Game.player.pix_pos
        # print(player)
        start = [(enemy[0] // 25), (enemy[1] // 25)]
        goal = [(player[0] // 25), (player[1] // 25)]
        mapt[(goal[0], goal[1])] = 0
        mapt[(start[0], start[1])] = 0
        queue = [start]
        path = list()
        count = 0
        visited = list()
        neighbors = [vec(0, 1), vec(1, 0), vec(-1, 0), vec(0, -1)]

        def bfs_can_move(d, current):
            temp = vec(current[0],current[1]) + d
            if int(temp[0]) > -1 and int(temp[1]) > -1:
                try:
                    if mapt[(int(temp[0]),int(temp[1]))] == 1:
                        return False
                except:
                    return True
            return True
        while queue:
            current = queue.pop(0)
            visited.append(current)
            if current == goal:
                break
            for neighbor in neighbors:
                if bfs_can_move(neighbor, current):
                    next_pixel = vec(current[0], current[1]) + neighbor
                    if next_pixel not in visited:
                        queue.append(next_pixel)
                        path.append({"current": current,
                                    "Next cell": next_pixel})
        shortest = [goal]
        count = 0
        while goal != start:
            for step in path:
                if step["Next cell"] == goal:
                    goal = step["current"]
                    shortest.insert(0, step["current"])
        return shortest[1]
