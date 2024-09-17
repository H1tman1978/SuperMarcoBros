"""
player.py
Handles player character logic (Marco and Luca) in Super Marco Bros.
"""

import pygame
from settings import PLAYER_SPEED, JUMP_HEIGHT, GRAVITY, WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
    """Represents the player character (Marco) in the game."""

    def __init__(self):
        super().__init__()
        # Load player image or create a placeholder
        self.image = pygame.Surface((50, 50))  # Placeholder for the player sprite (50x50 px)
        self.image.fill((255, 0, 0))           # Fill with red color for now (will replace with actual sprite)
        self.rect = self.image.get_rect()

        # Player position and movement attributes
        self.rect.center = (WIDTH // 2, HEIGHT - 100)  # Start near the bottom of the screen
        self.velocity_x = 0  # Speed along the x-axis
        self.velocity_y = 0  # Speed along the y-axis (for jumping/falling)
        self.is_jumping = False
        self.controls_reversed = False
        self.reverse_timer = 0

    def reverse_controls(self):
        """Reverse player controls for 5 seconds."""
        self.controls_reversed = True
        self.reverse_timer = pygame.time.get_ticks() + 5000  # Reverse for 5 seconds

    def handle_input(self):
        """Handle player input for movement and jumping."""
        keys = pygame.key.get_pressed()

        # Reverse controls if the effect is active
        left_key = pygame.K_RIGHT if self.controls_reversed else pygame.K_LEFT
        right_key = pygame.K_LEFT if self.controls_reversed else pygame.K_RIGHT

        # Horizontal movement (Arrow keys and WSAD)
        if keys[left_key] or keys[pygame.K_a]:
            self.velocity_x = -PLAYER_SPEED
        elif keys[right_key] or keys[pygame.K_d]:
            self.velocity_x = PLAYER_SPEED
        else:
            self.velocity_x = 0

        # Jumping (Space or W key)
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and not self.is_jumping:
            self.velocity_y = -JUMP_HEIGHT
            self.is_jumping = True

        # Reset controls after 5 seconds
        if self.controls_reversed and pygame.time.get_ticks() > self.reverse_timer:
            self.controls_reversed = False

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

        # Check for collisions with platforms
        platform_collisions = pygame.sprite.spritecollide(self, platforms, False)
        if platform_collisions:
            # If falling, stop falling and stand on the platform
            if self.velocity_y > 0:
                self.rect.bottom = platform_collisions[0].rect.top
                self.velocity_y = 0
                self.is_jumping = False

    def draw(self, surface):
        """Draw the player character to the screen."""
        surface.blit(self.image, self.rect)
