"""
settings.py
Holds game-wide configuration settings for Super Marco Bros.
"""
import os

# Game window settings
WIDTH = 800     # Width of the game window
HEIGHT = 600    # Height of the game window
FPS = 60        # Frames per second (controls game speed)

# Player settings
PLAYER_SPEED = 5   # Speed of Marco and Luca
JUMP_HEIGHT = 15   # Jump height of Marco and Luca

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CARDINAL = (196, 40, 71)

# Game settings
GRAVITY = 0.8   # Gravity affects player jump and fall

# Asset directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'assets', 'images')
SOUNDS_DIR = os.path.join(BASE_DIR, 'assets', 'sounds')
SPRITESHEETS_DIR = os.path.join(BASE_DIR, 'assets', 'spritesheets')
PLAYER_SPRITESHEET_DIR = os.path.join(SPRITESHEETS_DIR, 'players')
ENEMIES_SPRITESHEET_DIR = os.path.join(SPRITESHEETS_DIR, 'enemies')
PLATFORMS_SPRITESHEET_DIR = os.path.join(SPRITESHEETS_DIR, 'platforms')
ITEMS_SPRITESHEET_DIR = os.path.join(SPRITESHEETS_DIR, 'items')
LUCA_PLAYER_SPRITESHEET_DIR = os.path.join(PLAYER_SPRITESHEET_DIR, 'luca')
MARCO_PLAYER_SPRITESHEET_DIR = os.path.join(PLAYER_SPRITESHEET_DIR, 'marco')

SPRITESHEETS_LIST = [
    {
        'image': os.path.join(LUCA_PLAYER_SPRITESHEET_DIR, 'luca_spritesheet.png'),
        'xml': os.path.join(LUCA_PLAYER_SPRITESHEET_DIR, 'luca_spritesheet.xml'),
    },
    {
        'image': os.path.join(MARCO_PLAYER_SPRITESHEET_DIR, 'marco_spritesheet.png'),
        'xml': os.path.join(MARCO_PLAYER_SPRITESHEET_DIR, 'marco_spritesheet.xml'),
    },
    {
        'image': os.path.join(ENEMIES_SPRITESHEET_DIR, 'enemies_spritesheet.png'),
        'xml': os.path.join(ENEMIES_SPRITESHEET_DIR, 'enemies_spritesheet.xml'),
    },
    {
        'image': os.path.join(PLATFORMS_SPRITESHEET_DIR, 'platforms_spritesheet.png'),
        'xml': os.path.join(PLATFORMS_SPRITESHEET_DIR, 'platforms_spritesheet.xml'),
    },
    {
        'image': os.path.join(ITEMS_SPRITESHEET_DIR, 'items_spritesheet.png'),
        'xml': os.path.join(ITEMS_SPRITESHEET_DIR, 'items_spritesheet.xml'),
    }
]

BACKGROUND_IMAGE = os.path.join(IMAGES_DIR, 'background.jpg')

# Sound settings
MUSIC_VOLUME = 0.5   # Volume level for music
SFX_VOLUME = 0.8     # Volume level for sound effects
MAIN_MENU_MUSIC = os.path.join(SOUNDS_DIR, 'prologue.mp3')
IN_GAME_MUSIC = os.path.join(SOUNDS_DIR, 'Rising.mp3')
GAME_OVER_SOUND = os.path.join(SOUNDS_DIR, 'vgdeathsound.mp3')

