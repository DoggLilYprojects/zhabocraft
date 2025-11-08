from chunk import *
#from blocks import *
import numpy
import pygame
import textDrawer
from inventory import *
from random import randint
'''
def generateChunk(w):
    blocks = numpy.zeros((CHUNK_SIZE, CHUNK_SIZE), dtype=object)
    for y in range(CHUNK_SIZE):
        for x in range(CHUNK_SIZE):
            blocks[y][x] = grass_block
    return Chunk(blocks, w)
'''

class Entity:
    def __init__(self, world, position, health):
        self.world          = world
        self.position       = position
        self.last_chunk  = self.get_chunkpos(position)
        self.health         = health
        self.maxhealth      = health
        self.world.get_chunk(self.last_chunk).entities[self] = self
        
    
    def get_chunkpos(self, position):
        return (int(numpy.floor(position[0]/CHUNK_SIZE)),
                int(numpy.floor(position[1]/CHUNK_SIZE)))
    def draw(self, offset):
        pass

    def move(self):
        new_chunk = self.get_chunkpos(self.position)

        if self.last_chunk != new_chunk:
            last = self.last_chunk
            self.change_chunk(new_chunk)
            #self.world.console.logs.append(f"<{self.name}> from {last} to {new_chunk}")

    def update(self):
        self.move()
        #self.generateChunks(self.last_chunk)

    def change_chunk(self, new_chunk):
        del self.world.get_chunk(self.last_chunk).entities[self]

        self.world.get_chunk(new_chunk).entities[self] = self

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
        self.inventory.pickup(self.world.itemList.planks)        

    def draw(self, offset):
        '''
        self.spritePosition[0] += ((self.position[0])*SPRITE_SIZE-self.spritePosition[0])/3 if abs(self.spritePosition[0]-self.position[0])>1 else ((self.position[0])*SPRITE_SIZE-self.spritePosition[0]) 
        self.spritePosition[1] += ((self.position[1])*SPRITE_SIZE-self.spritePosition[1])/3 if abs(self.spritePosition[1]-self.position[1])>1 else ((self.position[1])*SPRITE_SIZE-self.spritePosition[1]) 
        '''
        
        self.world.window.blit(self.skin, (self.position[0]*SPRITE_SIZE%(CHUNK_SIZE*SPRITE_SIZE)+offset[0], self.position[1]*SPRITE_SIZE%(CHUNK_SIZE*SPRITE_SIZE)+offset[1]))
        if (self._selection != [0,0]):
            pygame.draw.rect(self.world.window, (255,255,255), (self.position[0]*SPRITE_SIZE+self._selection[0]*SPRITE_SIZE+offset[0],
                                                    self.position[1]*SPRITE_SIZE+self._selection[1]*SPRITE_SIZE+offset[1],
                                                    SPRITE_SIZE,
                                                    SPRITE_SIZE), 2)
#        print("drawwed", randint(0,9))

    def keyMove(self, keys):
        self._selection[:] = [0,0]
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

    def update(self):
        keys = pygame.key.get_pressed()
        self.keyMove(keys)

        # !!!!!!!!!!!!!!!!!!!!!!! TODO complite this mouse stuff maybe :P
        '''
        mouseX, mouseY  = pygame.mouse.get_pos()
        selectedX       = int(numpy.floor((max(0, mouseX-256))/SPRITE_SIZE))
        selectedY       = int(numpy.floor(mouseY/SPRITE_SIZE)
        '''
        
        self._selection[:] = [keys[pygame.K_RIGHT]-keys[pygame.K_LEFT],keys[pygame.K_DOWN]-keys[pygame.K_UP]]

        if (keys[pygame.K_SPACE]):
            self.inventory.rightClicked(self.position[0]+self._selection[0], self.position[1]+self._selection[1])
#            self.placeBlock(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT], keys[pygame.K_DOWN]-keys[pygame.K_UP])
'''
    def placeBlock(self, dx, dy):
        self._selection[:] = [dx, dy]
        position = self.position[0]+self._selection[0], self.position[1]+self._selection[1]
        self.world.chunks[self.get_chunkpos(position)].blocks[position[1]%CHUNK_SIZE][position[0]%CHUNK_SIZE] = duck
'''

class TestEntity(Entity):
    def __init__(self,world,position,health):
        super().__init__(world, position, health)
        self.sprite = pygame.transform.scale(pygame.image.load("sprites//HE_MEDBED.png"), (SPRITE_SIZE, SPRITE_SIZE))
        self.counter = 0

    def draw(self, offset):
        self.world.window.blit(self.sprite, (self.position[0]*SPRITE_SIZE%(CHUNK_SIZE*SPRITE_SIZE)+offset[0], self.position[1]*SPRITE_SIZE%(CHUNK_SIZE*SPRITE_SIZE)+offset[1]))

    def move(self):
        self.counter+=1
        self.counter%=10
        if self.counter != 0: return
        self.position[0]+=1
        super().move()



