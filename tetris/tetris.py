from settings import *
import math
from tetromino import Tetromino
import pygame.freetype as ft


class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)

    def draw(self):
        self.font.render_to(self.app.screen, (WINDOWN_WIDTH * 0.6, WINDOW_HEIGHT * 0.02),
                            text='TETRIS', fgcolor='white', size=TILE_SIZE * 3)

        self.font.render_to(self.app.screen, (WINDOWN_WIDTH * 0.7, WINDOW_HEIGHT * 0.22),
                            text='NEXT', fgcolor='white', size=TILE_SIZE * 2)

        self.font.render_to(self.app.screen, (WINDOWN_WIDTH * 0.7, WINDOW_HEIGHT * 0.67),
                            text='SCORE', fgcolor='white', size=TILE_SIZE * 2)

        self.font.render_to(self.app.screen, (WINDOWN_WIDTH * 0.7, WINDOW_HEIGHT * 0.8),
                            text=f'{self.app.tetris.score}', fgcolor='white', size=TILE_SIZE * 2.5)


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pygame.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current=False)
        self.speed_up = False

        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {0: 0, 1: 100, 2: 200, 3: 3000, 4: 400}

    def get_score(self):
        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0

    def check_full_lines(self):  # certo
        row = FIELD_HEIGHT - 1
        for y in range(FIELD_HEIGHT - 1, -1, -1):
            for x in range(FIELD_WIDTH):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].position = vec(x, y)

            if sum(map(bool, self.field_array[y])) < FIELD_WIDTH:
                row -= 1
            else:
                for x in range(FIELD_WIDTH):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

                self.full_lines += 1

    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.position.x), int(block.position.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]

    def is_game_over(self):
        if self.tetromino.blocks[0].position.y == INITIAL_POSITION_OFFSET[1]:
            pygame.time.wait(300)
            return True

    def check_tetromino_landing(self):
        if self.tetromino.landing:
            if self.is_game_over():
                self.__init__(self.app)
            else:
                self.speed_up = False
                self.put_tetromino_blocks_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)

    def control(self, pressed_key):
        if pressed_key == pygame.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pygame.K_RIGHT:
            self.tetromino.move(direction='right')
        elif pressed_key == pygame.K_UP:
            self.tetromino.rotate()
        elif pressed_key == pygame.K_DOWN:
            self.speed_up = True

    def draw_grid(self):
        for x in range(FIELD_WIDTH):
            for y in range(FIELD_HEIGHT):
                pygame.draw.rect(self.app.screen, 'black', (x *
                                 TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        trigger = [self.app.animation_trigger,
                   self.app.fast_animation_trigger][self.speed_up]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_tetromino_landing()
            self.get_score()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
