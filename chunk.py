import pygame
import numpy
#from blocks import grass_block

CHUNK_SIZE  = 16
SPRITE_SIZE = 48

class Chunk:
    def __init__(self, blocks, world):
        self.blocks   = blocks
        self.world    = world
        self.entities = dict()

    def draw(self, offset):
        for x in range(CHUNK_SIZE):
            for y in range(CHUNK_SIZE):
                self.world.window.blit(self.blocks[y][x].sprite, self.screenPosition(x,y, offset))

        for entity in list(self.entities.values()):
            entity.draw(offset)

    def update(self):
        for entity in list(self.entities.values()):
            entity.update()

    def screenPosition(self, x, y, offset):
        return (x*SPRITE_SIZE+offset[0], y*SPRITE_SIZE+offset[1])
    


class Block:
    def __init__(self, spritepath, durability=10):
        self.spritepath = spritepath
        self.sprite = pygame.transform.scale(pygame.image.load(spritepath), (SPRITE_SIZE, SPRITE_SIZE))
        self.durability = durability


def generateChunk(w, block):
    blocks = numpy.zeros((CHUNK_SIZE, CHUNK_SIZE), dtype=object)
    for y in range(CHUNK_SIZE):
        for x in range(CHUNK_SIZE):
            blocks[y][x] = block
    return Chunk(blocks, w)
