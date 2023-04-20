import sys
from settings import *
from tetris import Tetris, Text
import pathlib


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.screen = pygame.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.load(MUSIC)
        pygame.mixer.music.play(-1)

    def load_images(self):
        files = [item for item in pathlib.Path(
            SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        images = [pygame.image.load(file).convert_alpha() for file in files]
        images = [pygame.transform.scale(
            image, (TILE_SIZE, TILE_SIZE)) for image in images]
        print(SPRITE_DIR_PATH)
        return images

    def set_timer(self):
        self.user_event = pygame.USEREVENT + 0
        self.fast_user_event = pygame.USEREVENT + 1
        self.animation_trigger = False
        self.fast_animation_trigger = False
        pygame.time.set_timer(self.user_event, ANIMETION_TIME_INTERVAL)
        pygame.time.set_timer(self.fast_user_event,
                              FAST_ANIMETION_TIME_INTERVAL)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=BACKGROUND_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RESOLUTION))
        self.tetris.draw()
        self.text.draw()
        pygame.display.flip()

    def check_events(self):
        self.animation_trigger = False
        self.fast_animation_trigger = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.animation_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_animation_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
