# ==============================================================================
# CONFIGURACION GENERAL DEL JUEGO
# ==============================================================================

# --- CONSTANTES DE PANTALLA ---
ALTO = 480
ANCHO = 640
TITULO = 'Proyecto Shooter'

# --- COLORES (Formato RGB) ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACK = (136, 3, 252)

# --- RUTAS DE RECURSOS (IMAGENES) ---
PLAYER_IMG = 'src/ship.png'
ENEMY_IMG = 'src/enemy.png'
BACKGROUND_IMG = 'src/background.jpg'
BULLET_IMG = PLAYER_IMG  # Buscar una imagen para las balas
DEFEAT_IMG = 'src/defeat.jpg'
VICTORY_IMG = 'src/victory.jpg'

# ARCHIVOS DE FUENTES
FONT_FILE = 'src/font_1.ttf'

# --- RUTAS DE RECURSOS (SONIDOS) ---
# (Puedes agregar tus pistas de audio aquí más adelante)

# --- PARAMETROS INICIALES DE PARTIDA ---
vidas = 5
fallos = 0
puntos = 0
FPS = 60

# --- BANDERAS DE ESTADO (CONTROL DEL JUEGO) ---
run = True
finish = False
