"""
main.py
Entry point for Super Marco Bros game using PyGame.
"""

import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, SKY_BLUE
from player import Player
from platform import Platform
from enemy import Enemy
from item import Item

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Marco Bros")

# Set up the game clock
clock = pygame.time.Clock()

# Create player instance
player = Player()

# Create platforms
platforms = pygame.sprite.Group()
platform1 = Platform(100, HEIGHT - 100, 200, 20)
platform2 = Platform(400, HEIGHT - 200, 200, 20)
platform3 = Platform(600, HEIGHT - 150, 200, 20)
platforms.add(platform1, platform2, platform3)

# Create enemies
enemies = pygame.sprite.Group()
enemy1 = Enemy(200, HEIGHT - 100, 50, 50, 2)
enemy2 = Enemy(500, HEIGHT - 150, 50, 50, 2)
enemies.add(enemy1, enemy2)

# Create items (bad shroom)
items = pygame.sprite.Group()
bad_shroom = Item(300, HEIGHT - 300, 30, 30)
items.add(bad_shroom)

# Sprite group for easier management
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(platforms)
all_sprites.add(enemies)
all_sprites.add(items)


def main():
    """Main game loop."""
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state (player, enemies, etc.)
        all_sprites.update()

        # Drawing code
        screen.fill(SKY_BLUE)  # Fill the background with sky blue color

        # Draw all sprites (player, etc.)
        all_sprites.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
