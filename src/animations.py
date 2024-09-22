"""
animations.py
Stores all animation frames for various objects included in the game.
"""
import pygame

from sprite_loader import sprites

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

marco_animations = {
    'idle': [
        sprites.get('marco_stand'),
        sprites.get('marco_front'),
        sprites.get('marco_stand'),
        sprites.get('marco_duck'),
        sprites.get('marco_front')
    ],
    'jump': [sprites.get('marco_jump')],  # Single frame for jump
    'walk_right': [
        sprites.get('marco_walk01'),
        sprites.get('marco_walk02'),
        sprites.get('marco_walk03'),
        sprites.get('marco_walk04'),
        sprites.get('marco_walk05'),
        sprites.get('marco_walk06'),
        sprites.get('marco_walk07'),
        sprites.get('marco_walk08'),
        sprites.get('marco_walk09'),
        sprites.get('marco_walk10'),
        sprites.get('marco_walk11')
    ],
    # Flip walk_right frames to get walk_left frames
    'walk_left': [pygame.transform.flip(frame, True, False) for frame in [
        sprites.get('marco_walk01'),
        sprites.get('marco_walk02'),
        sprites.get('marco_walk03'),
        sprites.get('marco_walk04'),
        sprites.get('marco_walk05'),
        sprites.get('marco_walk06'),
        sprites.get('marco_walk07'),
        sprites.get('marco_walk08'),
        sprites.get('marco_walk09'),
        sprites.get('marco_walk10'),
        sprites.get('marco_walk11')
    ]]
}


# Enemy Animations (Slime)
slime_enemy_animations = {
    'idle': [sprites.get('slimeWalk1')],
    'walk_right': [
        sprites.get('slimeWalk1'),
        sprites.get('slimeWalk2')
    ],
    'walk_left': [pygame.transform.flip(frame, True, False) for frame in [
        sprites.get('slimeWalk1'),
        sprites.get('slimeWalk2')
    ]]
}
