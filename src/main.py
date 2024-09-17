"""
main.py
Entry point for Super Marco Bros game using PyGame.
"""

import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, SKY_BLUE
from player import Player

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Marco Bros")

# Set up the game clock
clock = pygame.time.Clock()

# Create player instance
player = Player()

# Sprite group for easier management (if more objects are added later)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


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
