import pygame
import ingame_variables as iv
import numpy as np
import PLAYER as P
import MAP
import sys
import ENEMY as E
pygame.init()
vec = pygame.math.Vector2
M = MAP.Map()


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((iv.swidth, iv.sheight))
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = M.load_map()
        self.coins = M.load_coins()
        self.game = 'playing'
        self.cell_width = iv.mwidth // iv.collumns
        self.cell_height = iv.mheight // iv.rows
        self.load_maze()
        self.player = P.Player(self, iv.PLAYER_START_POS)
        # self.enemy1 = E.Enemy(self, iv.enemy1_start_pos, iv.enemy1_colour, "r")
        self.enemy2 = E.Enemy(self, iv.enemy2_start_pos, iv.enemy1_colour, "b")

    def run(self):
        while self.running:
            if self.game == 'start':
                self.pregame_events()
                self.pregame_update()
                self.pregame_draw()
            elif self.game == 'playing':
                self.ingame_events()
                self.ingame_update()
                self.ingame_draw()
            else:
                self.running = False
            self.clock.tick(iv.FPS)
        pygame.quit()
        sys.exit()

# helper method

    def game_text(self, words, screen, pos, size, color, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        txt_size = text.get_size()
        pos[0] = pos[0] - txt_size[0] // 2
        pos[1] = pos[1] - txt_size[1] // 2
        screen.blit(text, pos)

    def load_maze(self):
        self.background = pygame.image.load(iv.maze_path)
        self.background = pygame.transform.scale(self.background,
                                                 (iv.mwidth, iv.mheight))

#################

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (82, 210, 149),
                               (int(coin.x * self.cell_width) + 25,
                                int(coin.y * self.cell_height) + 25),
                               int(self.cell_width) + 4)

# pregame methods

    def pregame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print("pressed space")
                self.game = 'playing'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("pressed escape")
                self.running = False

    def pregame_update(self):
        pass

    def pregame_draw(self):
        self.screen.fill(iv.intro_scr_color)
        self.game_text('WELCOME PLAYER', self.screen,
                       [iv.center[0], iv.center[1] - 50],
                       iv.star_font_size, (170, 132, 58), iv.start_font_name)
        self.game_text('PRESS SPACE TO PLAY', self.screen,
                       [iv.center[0], iv.center[1] + 40],
                       iv.star_font_size, (170, 132, 100), iv.start_font_name)
        pygame.display.update()
##################

# ingame methods

    def ingame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("pressed escape")
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                    # print("left")
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                    # print("right")
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                    # print("up")
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))
                    # print("down")

    def ingame_update(self):
        self.player.update()
        # self.enemy1.update()
        self.enemy2.update()

    def ingame_draw(self):
        self.screen.fill(iv.BLACK)
        self.screen.blit(self.background,
                         (iv.top_bottom_buffer // 2,
                          iv.top_bottom_buffer // 2))
        self.draw_coins()
        self.game_text('CURRENT SCORE: {}'.format(self.player.current_score),
                       self.screen, [120, 10], 18, iv.WHITE,
                       iv.start_font_name)
        self.game_text('HIGH SCORE: 0', self.screen,
                       [iv.swidth // 2 + 250, 10],
                       18, iv.WHITE, iv.start_font_name)
        self.player.appear()
        # self.enemy1.appear()
        self.enemy2.appear()
        pygame.display.update()
