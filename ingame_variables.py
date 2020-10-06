from pygame.math import Vector2 as vec

# screen width and height
swidth, sheight = 690, 962
top_bottom_buffer = 50
mwidth, mheight = swidth - top_bottom_buffer, sheight - top_bottom_buffer
rows = 38
collumns = 40

# frmaes per second
FPS = 60

# color
intro_scr_color = (55, 60, 0)
ingame_scr_color = (20, 55, 25)
grid_colour = (107, 107, 107)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# coordinates
center = [swidth // 2, sheight // 2]


# font
star_font_size = 32
start_font_name = 'arial black'


# player settings
PLAYER_START_POS = vec(1, 9.5)
PLAYER_COLOUR = (190, 194, 15)
