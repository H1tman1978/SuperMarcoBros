"""
main.py
Entry point for Super Marco Bros game using PyGame.
"""

import pygame
import sys
from settings import BACKGROUND_IMAGE, WIDTH, HEIGHT, FPS, SKY_BLUE, SPRITESHEETS_LIST
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
background_y = HEIGHT - background.get_height()  # Align bottom of the image with the bottom of the screen

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

# Set up the game clock
clock = pygame.time.Clock()

# Placeholder for sprite groups
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Placeholder for future object creation based on level map


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
