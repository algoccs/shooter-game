# Importar dependencias
from pygame import *
from config import *
from random import randint


# Pantalla
screen = display.set_mode((ANCHO, ALTO))
display.set_caption(TITULO)
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, x_pos, y_pos, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(
            sprite_img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = speed

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <= ANCHO - self.width:
            self.rect.x += self.speed

    def shoot(self):
        print('Pew Pew!')


class Enemy(GameSprite):
    pass


# OBJETOS
player = Player(PLAYER_IMG, ANCHO // 2, ALTO - 100, 60, 60, 5)

# CICLO DE JUEGO
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    screen.fill(BACK)
    player.reset()
    player.update()

    display.update()
    clock.tick(FPS)
