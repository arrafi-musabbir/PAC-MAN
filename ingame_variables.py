from pygame.math import Vector2 as vec
import numpy as np

# screen width and height
swidth, sheight = 675, 675
top_bottom_buffer = 50
tbf = top_bottom_buffer // 2
mwidth, mheight = swidth - top_bottom_buffer, sheight - top_bottom_buffer
rows = 25
collumns = 25

# frmaes per second
FPS = 60

# color
intro_scr_color = (106, 135, 222)
ingame_scr_color = (0, 0, 0)
grid_colour = (107, 107, 107)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# coordinates
center = [swidth // 2, sheight // 2]


# font
star_font_size = 32
start_font_name = 'arial black'


# player settings
# PLAYER_START_POS = vec(35, 35)
PLAYER_START_POS = vec(11.5, 12.5)
PLAYER_COLOUR = (190, 194, 15)

# ENEMY
enemy1_start_pos = vec(1.5, 20.5)
enemy1_colour = (255, 0, 0)
enemy2_start_pos = vec(1.5, 1.5)
enemy2_colour = (0, 0, 255)
enemy3_start_pos = vec(20.5, 19.5)
enemy3_colour = (0, 255, 0)
# maze
maze_path = "D:/github/PAC-MAN/maze.png"
maze_npy = "D:/github/PAC-MAN/maze.npy"
tiles_txt = "D:/github/PAC-MAN/tiles.txt"
