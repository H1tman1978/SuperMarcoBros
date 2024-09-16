"""
player.py
Handles player character logic (Marco and Luca) in Super Marco Bros.
"""

import pygame
from src.settings import PLAYER_SPEED, JUMP_HEIGHT, GRAVITY, WIDTH, HEIGHT, SKY_BLUE


class Player(pygame.sprite.Sprite):
    """Represents the player character (Marco) in the game."""

    def __init__(self):
        super().__init__()
        # Load player image or create a placeholder
        self.image = pygame.Surface((50, 50))  # Placeholder for the player sprite (50x50 px)
        self.image.fill((255, 0, 0))  # Fill with red color for now (will replace with actual sprite)
        self.rect = self.image.get_rect()

        # Player position and movement attributes
        self.rect.center = (WIDTH // 2, HEIGHT - 100)  # Start near the bottom of the screen
        self.velocity_x = 0  # Speed along the x-axis
        self.velocity_y = 0  # Speed along the y-axis (for jumping/falling)
        self.is_jumping = False

    def handle_input(self):
        """Handle player input for movement and jumping."""
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_LEFT]:
            self.velocity_x = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = PLAYER_SPEED
        else:
            self.velocity_x = 0

        # Jumping
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = -JUMP_HEIGHT
            self.is_jumping = True

    def apply_gravity(self):
        """Apply gravity to the player to simulate falling and jumping behavior."""
        self.velocity_y += GRAVITY
        if self.rect.bottom >= HEIGHT - 50:  # Simulate ground collision
            self.rect.bottom = HEIGHT - 50
            self.velocity_y = 0
            self.is_jumping = False

    def update(self):
        """Update the player's position and apply movement logic."""
        self.handle_input()  # Process user input
        self.rect.x += self.velocity_x  # Move left/right
        self.rect.y += self.velocity_y  # Move up/down (jumping/falling)

        # Keep the player within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        # Apply gravity
        self.apply_gravity()

    def draw(self, surface):
        """Draw the player character to the screen."""
        surface.blit(self.image, self.rect)

