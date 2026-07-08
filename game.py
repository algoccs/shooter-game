# ==============================================================================
# DEPENDENCIAS E IMPORTACIONES
# ==============================================================================
from pygame import *
from config import *
from random import randint

# Inicialización de los módulos de Pygame
init()

# ==============================================================================
# CONFIGURACION DE LA PANTALLA Y RELOJ
# ==============================================================================
screen = display.set_mode((ANCHO, ALTO))
display.set_caption(TITULO)
clock = time.Clock()

# Fondo
background = transform.scale(image.load(BACKGROUND_IMG), (ANCHO, ALTO))

# ==============================================================================
# CLASES Y ENTIDADES (SPRITES)
# ==============================================================================

# Clase base para todos los objetos gráficos del juego


class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, x_pos, y_pos, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        # Carga la imagen y la escala a las dimensiones deseadas
        self.image = transform.scale(image.load(
            sprite_img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = speed

    def reset(self):
        # Dibuja el sprite en su posición actual en la pantalla
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Clase para el personaje del jugador (Nave)


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        # Movimiento a la izquierda con límites de pantalla
        if keys[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        # Movimiento a la derecha con límites de pantalla
        if keys[K_d] and self.rect.x <= ANCHO - self.width:
            self.rect.x += self.speed

    def shoot(self):
        print('Pew Pew!')

# Clase para los enemigos (Meteoros/Naves enemigas)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= ALTO:
            self.rect.y = -40
            self.speed = randint(1, 5)
            self.rect.x = randint(0, ANCHO - 50)


# ==============================================================================
# INSTANCIACION DE OBJETOS
# ==============================================================================
player = Player(PLAYER_IMG, ANCHO // 2, ALTO - 100, 60, 60, 5)
enemy = Enemy(ENEMY_IMG, randint(0, ANCHO - 50), -40, 50, 40, randint(1, 5))

# ==============================================================================
# CICLO PRINCIPAL DEL JUEGO (GAME LOOP)
# ==============================================================================
while run:
    # --- REGISTRO DE EVENTOS ---
    for e in event.get():
        if e.type == QUIT:
            run = False

    screen.blit(background, (0, 0))
    # --- LOGICA Y ACTUALIZACIÓN DE POSICIONES ---
    player.update()  # Primero se calcula la nueva posición del jugador
    enemy.update()

    # --- RENDERIZADO (DIBUJO EN PANTALLA) ---
    player.reset()     # Dibuja al jugador en la nueva posición
    enemy.reset()     # Dibuja al jugador en la nueva posición

    # --- ACTUALIZACION DE LA VENTANA ---
    display.update()
    clock.tick(FPS)

# FINALIZACION DE PYGAME
quit()
