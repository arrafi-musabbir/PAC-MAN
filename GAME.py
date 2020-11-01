import pygame
import ingame_variables as iv
import PLAYER as P
import MAP
import sys
import ENEMY as E
import smart_enemy as s_e

pygame.init()
vec = pygame.math.Vector2
M = MAP.Map()


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((iv.swidth, iv.sheight))
        self.clock = pygame.time.Clock()
        self.game = 'start'
        self.running = True
        self.tiles = M.read_tiles()
        self.coins = list()
        self.load_coins()
        self.cell_width = iv.mwidth // iv.collumns
        self.cell_height = iv.mheight // iv.rows
        self.load_maze()
        self.player = P.Player(self, iv.PLAYER_START_POS)
        self.enemy1 = s_e.Enemy(
            self, iv.enemy1_start_pos, iv.enemy1_colour, "d")
        self.enemy2 = s_e.Enemy(
            self, iv.enemy2_start_pos, iv.enemy2_colour, "b")
        self.enemy3 = s_e.Enemy(
            self, iv.enemy3_start_pos, iv.enemy3_colour, "d")

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
            elif self.game == 'GameOver':
                self.postgame_events()
                self.postgame_update()
                self.postgame_draw()
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
    def load_coins(self):
        for key in self.tiles:
            if self.tiles[key] == 0:
                self.coins.append(key)

    def draw_coins(self):
        for key in self.coins:
            pygame.draw.circle(self.background, (252, 169, 3),
                               (key[0] * self.cell_width + self.cell_width // 2,
                                key[1] * self.cell_height + self.cell_height // 2),
                               self.cell_width // 4)

    def draw_grid(self):
        for x in range(0, iv.mwidth + 1):
            pygame.draw.line(self.background, iv.WHITE, (x * self.cell_width, 0),
                             (x * self.cell_width, iv.mheight))
        for x in range(0, iv.mheight + 1):
            pygame.draw.line(self.background, iv.WHITE, (0, x * self.cell_height),
                             (iv.mwidth, x * self.cell_height))

    def draw_maze(self):
        for key in self.tiles:
            if self.tiles[key] == 1:
                pygame.draw.rect(self.background, (56, 104, 224), (
                    key[0] * self.cell_width, key[1] * self.cell_height, self.cell_width, self.cell_height))
            else:
                pygame.draw.rect(self.background, (0, 0, 0), (
                    key[0] * self.cell_width, key[1] * self.cell_height, self.cell_width, self.cell_height))
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
                       iv.star_font_size, iv.WHITE, iv.start_font_name)
        self.game_text('PRESS SPACE TO PLAY', self.screen,
                       [iv.center[0], iv.center[1] + 40],
                       iv.star_font_size, iv.WHITE, iv.start_font_name)
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
                if event.key == pygame.K_ESCAPE:
                    # print("pressed escape")
                    self.running = False
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                    # self.enemy2.analogue(vec(-1, 0))
                    # print("left")
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                    # self.enemy2.analogue(vec(1, 0))
                    # print("right")
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                    # self.enemy2.analogue(vec(0, -1))
                    # print("up")
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))
                    # self.enemy2.analogue(vec(0, 1))

    def ingame_update(self):
        self.player.update()
        # self.enemy1.update()
        # self.enemy2.update()
        # self.enemy3.update()
        # pass

    def ingame_draw(self):
        self.screen.fill(iv.BLACK)
        self.screen.blit(self.background,
                         (iv.top_bottom_buffer // 2,
                          iv.top_bottom_buffer // 2))

        self.draw_maze()
        # self.draw_grid()
        self.draw_coins()
        self.game_text('CURRENT SCORE: {}'.format(self.player.current_score),
                       self.screen, [120, 10], 18, iv.WHITE,
                       iv.start_font_name)
        # self.game_text('HIGH SCORE: 0', self.screen,
        #                [iv.swidth // 2 + 250, 10],
        #                18, iv.WHITE, iv.start_font_name)
        self.player.appear()
        self.enemy1.appear()
        self.enemy2.appear()
        self.enemy3.appear()
        pygame.display.update()

    def postgame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("pressed escape")
                self.running = False

    def postgame_draw(self):
        self.screen.fill(iv.intro_scr_color)
        self.game_text('GAME OVER', self.screen,
                       [iv.swidth // 2, iv.mwidth // 2 + 50],
                       30, iv.WHITE, iv.start_font_name)
        self.game_text('SCORE: {}'.format(self.player.current_score), self.screen,
                       [iv.swidth // 2, iv.mwidth // 2 - 50],
                       30, iv.WHITE, iv.start_font_name)
        pygame.display.update()

    def postgame_update(self):
        pass
