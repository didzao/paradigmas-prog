from settings import *
import random


class Block (pygame.sprite.Sprite):
    def __init__(self, tetromino, position):
        self.tetromino = tetromino
        self.position = vec(position) + INITIAL_POSITION_OFFSET
        self.next_position = vec(position) + NEXT_POSITION_OFFSET
        self.alive = True

        super().__init__(tetromino.tetris.sprite_group)
        self.image = tetromino.image
        self.rect = self.image.get_rect()

        self.sfx_image = self.image.copy()
        self.sfx_image.set_alpha(110)
        self.sfx_speed = random.uniform(0.2, 0.6)
        self.sfx_cycles = random.randrange(6, 8)
        self.cycle_counter = 0

    def sfx_end_time(self):
        if self.tetromino.tetris.app.animation_trigger:
            self.cycle_counter += 1
            if self.cycle_counter > self.sfx_cycles:
                self.cycle_counter = 0
                return True

    def sfx_run(self):
        self.image = self.sfx_image
        self.image = pygame.transform.scale(self.image, (0, 0))

    def is_alive(self):
        if not self.alive:
            if not self.sfx_end_time():
                self.sfx_run()
            else:
                self.kill()

    def rotate(self, pivot_position):
        translated = self.position - pivot_position
        rotated = translated.rotate(90)
        return rotated + pivot_position

    def set_rect_position(self):
        position = [self.next_position, self.position][self.tetromino.current]
        self.rect.topleft = position * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_rect_position()

    def is_collide(self, position):
        x, y = int(position.x), int(position.y)
        if 0 <= x < FIELD_WIDTH and y < FIELD_HEIGHT and (
                y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True


class Tetromino:
    def __init__(self, tetris, current=True):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.image = random.choice(tetris.app.images)
        self.blocks = [Block(self, position)
                       for position in TETROMINOES[self.shape]]
        self.landing = False
        self.current = current

    def rotate(self):
        pivot_position = self.blocks[0].position
        new_block_positions = [block.rotate(
            pivot_position) for block in self.blocks]

        if not self.is_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.position = new_block_positions[i]

    def is_collide(self, block_positions):
        return any(map(Block.is_collide, self.blocks, block_positions))

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.position +
                               move_direction for block in self.blocks]
        is_collide = self.is_collide(new_block_positions)

        if not is_collide:
            for block in self.blocks:
                block.position += move_direction
        elif direction == 'down':
            self.landing = True

    def update(self):
        self.move(direction='down')
