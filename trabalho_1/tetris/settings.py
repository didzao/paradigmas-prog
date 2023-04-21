import pygame

vec = pygame.math.Vector2

FPS = 60
FIELD_COLOR = (224, 248, 207)
BACKGROUND_COLOR = (48, 104, 80)
TEXT_COLOR = FIELD_COLOR
LINES_COLOR = (134, 192, 109)

SPRITE_DIR_PATH = 'trabalho_1/tetris/assets/sprites'
FONT_PATH = 'trabalho_1/tetris/assets/font/Pixeltype.ttf'

MUSIC = 'trabalho_1/tetris/assets/audio/tetris.mp3'
SOUND_EFFECT_LANDING = 'trabalho_1/tetris/assets/audio/landing.wav'
SOUND_EFFECT_FULL_LINE = 'trabalho_1/tetris/assets/audio/fullLine.wav'
SOUND_EFFECT_GAME_OVER = 'trabalho_1/tetris/assets/audio/gameOver.wav'

ANIMETION_TIME_INTERVAL = 200  # milisegundos
FAST_ANIMETION_TIME_INTERVAL = 50

TILE_SIZE = 50
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT, = 10, 20
FIELD_RESOLUTION = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE

FIELD_SCALE_WIDTH, FIELD_SCALE_HEIGHT = 1.7, 1.0
WINDOW_RESOLUTION = WINDOWN_WIDTH, WINDOW_HEIGHT = FIELD_RESOLUTION[0] * \
    FIELD_SCALE_WIDTH, FIELD_RESOLUTION[1] * FIELD_SCALE_HEIGHT

NEXT_POSITION_OFFSET = vec(FIELD_WIDTH * 1.3, FIELD_HEIGHT * 0.45)

INITIAL_POSITION_OFFSET = vec(FIELD_WIDTH // 2 - 1, 0)

MOVE_DIRECTIONS = {'left': vec(-1, 0), 'down': vec(0, 1), 'right': vec(1, 0)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)],
}

IMAGES = {
    0: 'trabalho_1/tetris/assets/sprites/0.png',
    1: 'trabalho_1/tetris/assets/sprites/1.png',
    2: 'trabalho_1/tetris/assets/sprites/2.png',
    3: 'trabalho_1/tetris/assets/sprites/3.png',
    4: 'trabalho_1/tetris/assets/sprites/4.png',
    5: 'trabalho_1/tetris/assets/sprites/5.png',
    6: 'trabalho_1/tetris/assets/sprites/6.png',
}
