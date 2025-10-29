import pygame
import numpy
from entity import Player
from blocks import grass_block
from chunk import *
from world import *
from console import *

pygame.init()

w,h = 1024, 768
window = pygame.display.set_mode((w,h))
pygame.display.set_caption("ZhaboCraft")

clock = pygame.time.Clock()


def generateChunk(w):
    blocks = numpy.zeros((CHUNK_SIZE, CHUNK_SIZE), dtype=object)
    for y in range(CHUNK_SIZE):
        for x in range(CHUNK_SIZE):
            blocks[y][x] = grass_block
    return Chunk(blocks, w)

WORLD = World(window)
WORLD.chunks[(0,0)] = generateChunk(WORLD)
PLAYER = Player(WORLD, [0,0], "HE_MEDBED", "HE_MEDBED.png")

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    WORLD.update(PLAYER.last_chunk)
    WORLD.draw(PLAYER.last_chunk, (256, 0))
    PLAYER.inventory.draw()
    pygame.display.update()
