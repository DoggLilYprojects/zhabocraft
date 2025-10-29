import numpy
from console import *
import itemList


class World:
    def __init__(self, window):
        self.chunks     = dict()
        self.window     = window
        self.console    = Console(window, [])
        self.itemList   = itemList

    def draw(self, position, offset):
        
        '''
        position = self.get_chunkpos(position)
        inChunkPos = position[0]%CHUNK_SIZE, position[1]%CHUNK_SIZE

        offset = (CHUNK_SIZE/2*SPRITE_SIZE-inChunkPos[0]*SPRITE_SIZE,
                CHUNK_SIZE/2*SPRITE_SIZE-inChunkPos[1]*SPRITE_SIZE)
       
        i = CHUNK_SIZE*SPRITE_SIZE
        '''

        self.chunks[position].draw(offset)
        '''
        self.chunks[(position[0]+1, position[1]  )].draw((offset[0]+i, offset[1]  ), window)
        self.chunks[(position[0]  , position[1]+1)].draw((offset[0]  , offset[1]+i), window)
        self.chunks[(position[0]+1, position[1]+1)].draw((offset[0]+i, offset[1]+i), window)
        self.chunks[(position[0]-1, position[1]  )].draw((offset[0]-i, offset[1]  ), window)
        self.chunks[(position[0]  , position[1]-1)].draw((offset[0]  , offset[1]-i), window)
        self.chunks[(position[0]-1, position[1]-1)].draw((offset[0]-i, offset[1]-i), window)
        self.chunks[(position[0]+1, position[1]-1)].draw((offset[0]+i, offset[1]-i), window)
        self.chunks[(position[0]-1, position[1]+1)].draw((offset[0]-i, offset[1]+i), window)
        '''

    '''
    def get_chunkpos(self, position):
        return (int(numpy.floor(position[0]/CHUNK_SIZE) if position[0]>=0 else numpy.ceil(position[0]/CHUNK_SIZE)),
                int(numpy.floor(position[1]/CHUNK_SIZE) if position[1]>=0 else numpy.ceil(position[1]/CHUNK_SIZE)))
    '''

    def update(self, position):
        self.chunks[position].update()
