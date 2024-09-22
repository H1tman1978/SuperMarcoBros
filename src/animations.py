"""
animations.py
Stores all animation frames for various objects included in the game.
"""
import pygame

from main import sprites

luca_animations = {
    'idle': [
        sprites.get('luca_stand'),
        sprites.get('luca_front'),
        sprites.get('luca_stand'),
        sprites.get('luca_duck'),
        sprites.get('luca_front')
    ],
    'jump': [sprites.get('luca_jump')],  # Single frame for jump
    'walk_right': [
        sprites.get('luca_walk01'),
        sprites.get('luca_walk02'),
        sprites.get('luca_walk03'),
        sprites.get('luca_walk04'),
        sprites.get('luca_walk05'),
        sprites.get('luca_walk06'),
        sprites.get('luca_walk07'),
        sprites.get('luca_walk08'),
        sprites.get('luca_walk09'),
        sprites.get('luca_walk10'),
        sprites.get('luca_walk11')
    ],
    # Flip walk_right frames to get walk_left frames
    'walk_left': [pygame.transform.flip(frame, True, False) for frame in [
        sprites.get('luca_walk01'),
        sprites.get('luca_walk02'),
        sprites.get('luca_walk03'),
        sprites.get('luca_walk04'),
        sprites.get('luca_walk05'),
        sprites.get('luca_walk06'),
        sprites.get('luca_walk07'),
        sprites.get('luca_walk08'),
        sprites.get('luca_walk09'),
        sprites.get('luca_walk10'),
        sprites.get('luca_walk11')
    ]]
}

# Enemy Animations (Slime)
enemy_animations = {
    'walk_right': [
        sprites.get('slimeWalk1'),
        sprites.get('slimeWalk2')
    ],
    'walk_left': [pygame.transform.flip(frame, True, False) for frame in [
        sprites.get('slimeWalk1'),
        sprites.get('slimeWalk2')
    ]]
}
