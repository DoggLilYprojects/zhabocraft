import pygame
from chunk import SPRITE_SIZE

class Block:
    def __init__(self, spritepath, durability=10):
        self.spritepath = spritepath
        self.sprite = pygame.transform.scale(pygame.image.load(f"sprites//{spritepath}"), (SPRITE_SIZE, SPRITE_SIZE))
        self.durability = durability
