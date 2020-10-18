from pygame.math import Vector2 as vec
import numpy as np

# screen width and height
swidth, sheight = 850, 850
top_bottom_buffer = 50
mwidth, mheight = swidth - top_bottom_buffer, sheight - top_bottom_buffer
rows = mwidth
collumns = mheight

# frmaes per second
FPS = 60

# color
intro_scr_color = (55, 60, 0)
ingame_scr_color = (20, 55, 25)
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
PLAYER_START_POS = vec((mheight // 2) - 25, (mwidth // 2) - 25)
PLAYER_COLOUR = (190, 194, 15)

# ENEMY
enemy1_start_pos = vec(35, 35)
enemy1_colour = (255, 0, 0)
enemy2_start_pos = vec(35, 35)
# maze
maze_path = "D:/github/PAC-MAN/maze.png"
maze_npy = "PAC-MAN/maze.npy"

# write maze to a txt
