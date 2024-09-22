"""
menu.py
Handles the start menu logic for Super Marco Bros.
"""
import os
import sys

import pygame
from settings import CARDINAL, IMAGES_DIR, RED, WIDTH, HEIGHT, BACKGROUND_IMAGE


def show_start_menu(screen):
    """Displays the start menu and returns the selected character (Marco or Luca)"""
    # Load fonts (or use default font)
    font = pygame.font.Font(None, 120)
    small_font = pygame.font.Font(None, 75)

    # Load background image
    background = pygame.image.load(BACKGROUND_IMAGE).convert()

    # Load character images (Marco and Luca)
    marco_image = pygame.image.load(os.path.join(IMAGES_DIR, 'marco.png')).convert_alpha()
    luca_image = pygame.image.load(os.path.join(IMAGES_DIR, 'luca.png')).convert_alpha()

    # Resize character images to fit nicely on the menu
    marco_image = pygame.transform.scale(marco_image, (150, 150))
    luca_image = pygame.transform.scale(luca_image, (150, 150))

    # Set positions for characters on the screen
    marco_rect = marco_image.get_rect(center=(WIDTH // 3, HEIGHT // 2))
    luca_rect = luca_image.get_rect(center=(2 * WIDTH // 3, HEIGHT // 2))

    running = True
    selected_character = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Detect if Marco or Luca is clicked
                if marco_rect.collidepoint(event.pos):
                    selected_character = "Marco"
                    running = False  # Exit the menu
                elif luca_rect.collidepoint(event.pos):
                    selected_character = "Luca"
                    running = False  # Exit the menu

        # Draw the background
        screen.blit(background, (0, 0))

        # Draw the title and text
        title_text = font.render("Super Marco Bros", True, CARDINAL)
        choose_text = small_font.render("Choose your character:", True, CARDINAL)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
        screen.blit(choose_text, (WIDTH // 2 - choose_text.get_width() // 2, 150))

        # Draw the character images (Marco and Luca)
        screen.blit(marco_image, marco_rect)
        screen.blit(luca_image, luca_rect)

        # Update the display
        pygame.display.flip()

    return selected_character  # Return the selected character
