"""
main.py
Entry point for Super Marco Bros game using PyGame.
"""

import pygame
import sys
from settings import BACKGROUND_IMAGE, WIDTH, HEIGHT, FPS, SKY_BLUE, SPRITESHEETS_LIST
from player import Player
from platform_blocks import Platform
from enemy import Enemy
from item import Item
from sprite_loader import load_sprites_from_xml

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Marco Bros")

# Load background image
background = pygame.image.load(BACKGROUND_IMAGE).convert()

# Calculate the blit position to align the bottom-left of the image with the bottom-left of the screen
background_x = 0  # No shift on the x-axis
background_y = 600 - 1024  # Align bottom of the image with the bottom of the screen

# Load spritesheet images
sprites = {}
for sheet in SPRITESHEETS_LIST:
    image_path = sheet['image']
    xml_path = sheet['xml']

    # Load the sprite sheet image
    print(image_path, xml_path)
    spritesheet_image = pygame.image.load(image_path).convert_alpha()

    # Load sprites from the corresponding XML file
    sprite_data = load_sprites_from_xml(xml_path, spritesheet_image)

    # Store the loaded sprite data in the main sprites dictionary
    sprites.update(sprite_data)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Marco Bros")

# Set up the game clock
clock = pygame.time.Clock()

# Create player instance
player_sprite = sprites['marco_front']
player = Player(player_sprite, 100, 100)

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


def check_collisions():
    """Handle all collisions in the game."""
    # Player-platform collision
    platform_collisions = pygame.sprite.spritecollide(player, platforms, False)
    if platform_collisions:
        if player.velocity_y > 0:  # If the player is falling
            player.rect.bottom = platform_collisions[0].rect.top
            player.velocity_y = 0
            player.is_jumping = False

    # Player-enemy collision
    enemy_collision = pygame.sprite.spritecollide(player, enemies, False)
    if enemy_collision:
        if player.velocity_y > 0:  # Player is falling (jumping on enemy)
            enemy_collision[0].kill()  # Defeat enemy
        else:
            print("Player hit by enemy!")  # Placeholder for player damage

    # Player-item collision (bad shroom)
    item_collision = pygame.sprite.spritecollide(player, items, True)
    if item_collision:
        print("Bad shroom collected!")  # Placeholder for bad shroom effect
        player.reverse_controls()  # Reverse controls for the player


def main():
    """Main game loop."""
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the background first
        screen.blit(background, (background_x, background_y))

        # Update game state (player, enemies, etc.)
        all_sprites.update()

        # Check for collisions
        check_collisions()

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
