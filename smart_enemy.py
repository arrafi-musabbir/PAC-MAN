import pygame
import random
import ingame_variables as iv
vec = pygame.math.Vector2


class Enemy:
    def __init__(self, Game, pos, colour, personality):
        self.Game = Game
        self.e_colour = colour
        self.Game.cell_width = self.Game.cell_width
        self.Game.cell_height = self.Game.cell_height
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.radius = self.Game.cell_width // 2
        self.personality = personality
        self.direction = vec(1, 0)
        self.target = None
        self.able_to_move = True

    def update(self):
        # print(self.grid_pos)
        # print(self.grid_pos)
        if self.time_to_move():
            self.move()
        if self.able_to_move:
            self.pix_pos += self.direction
        # ##### Setting grid position in reference to pix position
        self.grid_pos[0] = (self.pix_pos[0] - iv.tbf -
                            self.Game.cell_width // 2)
        self.grid_pos[1] = (self.pix_pos[1] - iv.tbf -
                            self.Game.cell_width // 2)

    def appear(self):
        # print(self.pix_pos)
        pygame.draw.circle(self.Game.screen, self.e_colour,
                           (int(self.pix_pos.x) + 1, int(self.pix_pos.y) + 1), self.radius)

    def get_pix_pos(self):
        return vec(int(self.grid_pos.x * self.Game.cell_width)
                   + iv.tbf,
                   int(self.grid_pos.y * self.Game.cell_height)
                   + iv.tbf)

    def time_to_move(self):
        if ((self.grid_pos[0]) % self.Game.cell_width) == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if ((self.grid_pos[1]) % self.Game.cell_height) == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True
        return False

    def move(self):
        try:
            if self.set_personality() == "bfs":
                self.direction = self.get_bfs([int(self.grid_pos.x), int(self.grid_pos.y)], [
                                              int(self.Game.player.grid_pos[0]), int(self.Game.player.grid_pos[1])])
            elif self.set_personality() == "dfs":
                self.direction = self.get_bfs([int(self.grid_pos.x), int(self.grid_pos.y)], [
                                              int(self.Game.player.grid_pos[0]), int(self.Game.player.grid_pos[1])])
        except IndexError:
            self.Game.game = "GameOver"

    def set_personality(self):
        if self.personality == "d":
            return "dfs"
        if self.personality == "b":
            return "bfs"
        if self.personality == "a":
            return "analogue"

    def get_bfs(self, enemy, player):
        start = [enemy[0] // self.Game.cell_width,
                 enemy[1] // self.Game.cell_height]
        goal = [player[0] // self.Game.cell_width,
                player[1] // self.Game.cell_height]
        queue = [start]
        path = list()
        count = 0
        visited = list()
        neighbors = [vec(0, 1), vec(1, 0), vec(-1, 0), vec(0, -1)]

        def can_move(current, d):
            temp = current + d
            if temp[0] < 0 and temp[1] < 0:
                return False
            else:
                if self.Game.tiles[(temp[0], temp[1])] == 1:
                    return False
            return True

        while queue:
            current = queue.pop(0)
            visited.append(current)
            if current == goal:
                break
            for neighbor in neighbors:
                if can_move(current, neighbor):
                    next_pixel = vec(current[0], current[1]) + neighbor
                    if next_pixel not in visited:
                        queue.append(next_pixel)
                        path.append({"current": current,
                                     "Next cell": next_pixel})
        shortest = [goal]
        while goal != start:
            for step in path:
                if step["Next cell"] == goal:
                    goal = step["current"]
                    shortest.insert(0, step["current"])
        nextdir = [shortest[1][0] - start[0], shortest[1][1] - start[1]]
        return vec(nextdir[0], nextdir[1])

    def get_dfs(self, enemy, player):
        start = [enemy[0] // self.Game.cell_width,
                 enemy[1] // self.Game.cell_height]
        goal = [player[0] // self.Game.cell_width,
                player[1] // self.Game.cell_height]
        queue = [start]
        path = list()
        visited = list()
        neighbors = [vec(0, 1), vec(1, 0), vec(-1, 0), vec(0, -1)]

        def can_move(current, d):
            temp = current + d
            if temp[0] < 0 and temp[1] < 0:
                return False
            else:
                if self.Game.tiles[(temp[0], temp[1])] == 1:
                    return False
            return True

        while queue:
            current = queue.pop()
            visited.append(current)
            if current == goal:
                break
            for neighbor in neighbors:
                if can_move(current, neighbor):
                    next_pixel = vec(current[0], current[1]) + neighbor
                    if next_pixel not in visited:
                        queue.append(next_pixel)
                        path.append({"current": current,
                                     "Next cell": next_pixel})
        shortest = [goal]
        while goal != start:
            for step in path:
                if step["Next cell"] == goal:
                    goal = step["current"]
                    shortest.insert(0, step["current"])
        nextdir = [shortest[1][0] - start[0], shortest[1][1] - start[1]]
        print(nextdir)
        return vec(nextdir[0], nextdir[1])
