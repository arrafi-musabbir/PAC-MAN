import pygame
import ingame_variables as iv
import sys

pygame.init()
vec = pygame.math.Vector2


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((iv.swidth, iv.sheight))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game = 'start'

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
        self.game_text('PUSH SPACE BAR', self.screen,
                       [iv.center[0], iv.center[1]-50],
                       iv.star_font_size, (170, 132, 58), iv.start_font_name)
        self.game_text('WELCOME PLAYER', self.screen,
                       [iv.center[0], iv.center[1]+40],
                       iv.star_font_size, (170, 132, 100), iv.start_font_name)
        pygame.display.update()

    def ingame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("pressed escape")
                self.running = False

    def ingame_update(self):
        pass

    def ingame_draw(self):
        self.screen.fill(iv.ingame_scr_color)
        pygame.display.update()
