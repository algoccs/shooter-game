# ==============================================================================
# DEPENDENCIAS E IMPORTACIONES
# ==============================================================================
from pygame import *
from config import *
from random import randint

# Inicialización de los módulos de Pygame
init()
font.init()
mixer.init()

# ==============================================================================
# CONFIGURACION DE LA PANTALLA Y RELOJ
# ==============================================================================
screen = display.set_mode((ANCHO, ALTO))
display.set_caption(TITULO)
clock = time.Clock()

# TEXTO Y FUENTES
font_1 = font.Font(FONT_FILE, 30)


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
        bala = Bullet(BULLET_IMG, self.rect.x + 25, self.rect.y, 10, 15, 5)
        bullets.add(bala)


# Clase para los enemigos (Meteoros/Naves enemigas)
class Enemy(GameSprite):
    def update(self):
        global fallos

        self.rect.y += self.speed

        if self.rect.y >= ALTO:  # Cruza el limite inferior
            self.rect.y = -40
            self.speed = randint(1, 5)
            self.rect.x = randint(0, ANCHO - 50)

            fallos += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed


# ==============================================================================
# INSTANCIACION DE OBJETOS
# ==============================================================================
player = Player(PLAYER_IMG, ANCHO // 2, ALTO - 100, 60, 60, 5)
enemies = sprite.Group()  # SET (CONJUNTO) #add
bullets = sprite.Group()  # SET (CONJUNTO) #add

for i in range(5):
    enemy = Enemy(ENEMY_IMG, randint(0, ANCHO - 50), -
                  40, 50, 40, randint(1, 5))
    enemies.add(enemy)


# ==============================================================================
# CICLO PRINCIPAL DEL JUEGO (GAME LOOP)
# ==============================================================================
while run:
    # --- REGISTRO DE EVENTOS ---
    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.shoot()

    points_text = font_1.render(f'PUNTOS: {puntos}', 1, WHITE)
    misses_text = font_1.render(f'FALLOS: {fallos}', 1, WHITE)


    if not finish:
        screen.blit(background, (0, 0))
        # renderizar la fuente
        screen.blit(points_text, (20, 20))
        screen.blit(misses_text, (20, 60))

        # --- LOGICA Y ACTUALIZACIÓN DE POSICIONES ---
        player.update()  # Primero se calcula la nueva posición del jugador
        enemies.update()  # Recalcular la posicion de cada enemigo en el grupo de sprites
        bullets.update()

        # --- RENDERIZADO (DIBUJO EN PANTALLA) ---
        player.reset()  # Dibuja al jugador en la nueva posición
        enemies.draw(screen)  # Dibuja al grupo de sprites
        bullets.draw(screen)

        if fallos == 10:
            finish = True
            screen.fill(BLACK)
            # RENDERIZAR NUESTRA PANTALLA DE DERROTA

    # --- ACTUALIZACION DE LA VENTANA ---
    display.update()
    clock.tick(FPS)


# FINALIZACION DE PYGAME
quit()
