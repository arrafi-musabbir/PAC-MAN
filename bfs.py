import pygame
vec = pygame.math.Vector2
import MAP
M = MAP.Map()
import numpy
map = M.load_map()
mapt = M.read_tiles()
# print(map)
# print(len(mapt))
import ingame_variables as iv


def can_move(d, current):
    temp = vec(current[0],current[1]) + d
    # print([(int(temp[0]),int(temp[1]))])
    if int(temp[0]) > -1 and int(temp[1]) > -1:
        if map[(int(temp[0]),int(temp[1]))] == 1:
            return False
    return True


def get_bfs(enemy, player):
    # if enemy[0] > 25
    start = enemy
    goal = player
    queue = [start]
    path = list()
    count = 0
    visited = list()
    neighbors = [vec(0, 1), vec(1, 0), vec(-1, 0), vec(0, -1)]
    while queue:
        current = queue.pop(0)
        visited.append(current)
        if current == goal:
            break
        for neighbor in neighbors:
            if can_move(neighbor, current):
                next_pixel = vec(current[0],current[1]) + neighbor
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

print(get_bfs((99, 65), (112, 62)))
# print(0//25)
