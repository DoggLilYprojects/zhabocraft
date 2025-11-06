import pygame
import numpy
from chunk import CHUNK_SIZE
from blocks import duck

class Item:
    def __init__(self, world, name):
        self.world  = world
        self.name   = name
        self.sprite = pygame.image.load(f"sprites//{name}.png")
    
    def rightClicked(self, xWorldPos, yWorldPos):
        pass

    def leftClicked(self, xWorldPos, yWorldPos):
        pass

    def get_chunkpos(self, position):
        return (int(numpy.floor(position[0]/CHUNK_SIZE)),
                int(numpy.floor(position[1]/CHUNK_SIZE)))

# !!!!!!!!!!!!!!! TODO Breakable Items

'''
    def kill(self):
        self.world.remove(self) 

class BreakableItem(Item):
    def __init__(self, world, name, durability=128):
        super().__init__(world, name)
        self.durability = durability

    def afterUse(self):
        self.durability-=1
        if self.durability <= 0:
            self.kill()
'''

class ShovelItem(Item):
    def __init__(self, world, shovelType):
        super().__init__(world, f"{shovelType} shovel")

    def rightClicked(self, xWorldPos, yWorldPos):
        self.world.chunks[self.get_chunkpos((xWorldPos, yWorldPos))].blocks[yWorldPos%CHUNK_SIZE][xWorldPos%CHUNK_SIZE] = duck
