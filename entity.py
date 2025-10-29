from chunk import *
from blocks import *
import numpy
import pygame
import textDrawer
from inventory import *

def generateChunk(w):
    blocks = numpy.zeros((CHUNK_SIZE, CHUNK_SIZE), dtype=object)
    for y in range(CHUNK_SIZE):
        for x in range(CHUNK_SIZE):
            blocks[y][x] = grass_block
    return Chunk(blocks, w)


class Entity:
    def __init__(self, world, position, health):
        self.world          = world
        self.position       = position
        self.last_chunk  = self.get_chunkpos(position)
        self.health         = health
        self.maxhealth      = health
        self.world.chunks[self.last_chunk].entities[self] = self
        
    
    def get_chunkpos(self, position):
        return (int(numpy.floor(position[0]/CHUNK_SIZE) if position[0]>=0 else numpy.floor(position[0]/CHUNK_SIZE)),
                int(numpy.floor(position[1]/CHUNK_SIZE) if position[1]>=0 else numpy.floor(position[1]/CHUNK_SIZE)))
    def draw(self, offset):
        pass

    def move(self):
        pass

    def update(self):
        self.move()
        #self.generateChunks(self.last_chunk)

    def change_chunk(self, new_chunk):
        del self.world.chunks[self.last_chunk].entities[self]
        try: self.world.chunks[new_chunk].entities[self] = self
        except:
            self.world.chunks[new_chunk] = generateChunk(self.world)
            self.world.chunks[new_chunk].entities[self] = self
        self.last_chunk = new_chunk

    def generateChunks(self, centerChunk, around=2):
        for x in range(-around+1, around-1):
            for y in range(-around+1, around+1):
                if (self.world.chunks[(centerChunk[0]+x, centerChunk[1]+y)] == None):
                    self.world.chunks[(centerChunk[0]+x, centerChunk[1]+y)] = generateChunk(self.world)
        
    def truePosition(self):
        return (self.position[0]%CHUNK_SIZE), (self.position[1]%CHUNK_SIZE)

'''
    def take_damage(self, dmg):
        self.health-=dmg
        if self.health<=0: self.die()

    def die(self):
        del self.world.chunks[self.get_chunkpos(self.position)].entities[self]
        del self
'''

class Player(Entity):
    def __init__(self, world, position, name, skin):
        super().__init__(world, position, 10)
        self.name = name
        self.skin = pygame.transform.scale(pygame.image.load(f"sprites//{skin}"), (SPRITE_SIZE, SPRITE_SIZE))
        self._lastPressed = False
        self._selection = [0, 0]
        self.spritePosition = [position[0]%CHUNK_SIZE*SPRITE_SIZE, position[1]%CHUNK_SIZE*SPRITE_SIZE]
        self.inventory = Inventory(self)
        self.inventory.slots[0][0] = self.world.itemList.shovel

    def draw(self, offset):
        self.spritePosition[0] += ((self.position[0]%CHUNK_SIZE)*SPRITE_SIZE-self.spritePosition[0])/3
        self.spritePosition[1] += ((self.position[1]%CHUNK_SIZE)*SPRITE_SIZE-self.spritePosition[1])/3
        self.world.window.blit(self.skin, (self.spritePosition[0]+offset[0], self.spritePosition[1]+offset[1]))
        if (self._selection != [0,0]):
            pygame.draw.rect(self.world.window, (255,255,255), (self.spritePosition[0]+self._selection[0]*SPRITE_SIZE+offset[0],
                                                    self.spritePosition[1]+self._selection[1]*SPRITE_SIZE+offset[1],
                                                    SPRITE_SIZE,
                                                    SPRITE_SIZE), 2)

    def move(self):
        self._selection[:] = [0,0]
        keys = pygame.key.get_pressed()
        xdir = keys[pygame.K_d] - keys[pygame.K_a]
        ydir = keys[pygame.K_s] - keys[pygame.K_w]
        if (self._lastPressed and (abs(xdir) or abs(ydir))): return
        self.position[0]+=xdir
        self.position[1]+=ydir
        new_chunk = self.get_chunkpos(self.position)

        if self.last_chunk != new_chunk:
            last = self.last_chunk
            self.change_chunk(new_chunk)
            self.world.console.logs.append(f"<{self.name}> from {last} to {new_chunk}")

        self._lastPressed = abs(xdir) or abs(ydir)
        if (keys[pygame.K_SPACE]):
            self.placeBlock(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT], keys[pygame.K_DOWN]-keys[pygame.K_UP])

    def placeBlock(self, dx, dy):
        self._selection[:] = [dx, dy]
        pos = self.truePosition()
        self.world.chunks[self.last_chunk].blocks[(pos[1]+self._selection[1])%CHUNK_SIZE][(pos[0]+self._selection[0])%CHUNK_SIZE] = duck






