import pygame

from src.settings import HEIGHT, WIDTH


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        """Apply the camera offset to a sprite or entity."""
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        """Update the camera position to follow the player."""
        x = -target.rect.centerx + int(WIDTH / 2)  # Keep player in center of screen (horizontally)
        y = -target.rect.centery + int(HEIGHT / 2)  # Adjust this if you want vertical scrolling as well

        # Limit scrolling to the map bounds
        x = min(0, x)  # Prevent scrolling too far left
        x = max(-(self.width - WIDTH), x)  # Prevent scrolling too far right
        y = min(0, y)  # Prevent scrolling too far up
        y = max(-(self.height - HEIGHT), y)  # Prevent scrolling too far down

        self.camera = pygame.Rect(x, y, self.width, self.height)
