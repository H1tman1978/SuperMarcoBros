"""
main.py
Entry point for Super Marco Bros game using PyGame.
"""

import pygame
import sys
from src.settings import WIDTH, HEIGHT, FPS

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Marco Bros")

# Set up the game clock
clock = pygame.time.Clock()


def main():
    """Main game loop."""
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic goes here

        # Drawing code
        screen.fill((135, 206, 250))  # Fill the background with a sky blue color

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
