import numpy
from console import *
import itemList
import items
from chunk import CHUNK_SIZE, SPRITE_SIZE, generateChunk
import blockList

class World:
    def __init__(self, window):
        self.chunks     = dict()
        self.window     = window
        self.console    = Console(self)
        self.blockList  = blockList
        items.world     = self
        self.itemList   = itemList

    def draw(self, position, drawOffset):
        chunkPosition = self.get_chunkpos(position)

        inChunkPos = position[0]%CHUNK_SIZE, position[1]%CHUNK_SIZE
        globalChunkOffset = ((-inChunkPos[0]+CHUNK_SIZE/2)*SPRITE_SIZE, (-inChunkPos[1]+CHUNK_SIZE/2)*SPRITE_SIZE)
        
        inChunkPos = list(inChunkPos)

        inChunkPos[0]-=int(numpy.ceil(CHUNK_SIZE/2))
        inChunkPos[1]-=int(numpy.ceil(CHUNK_SIZE/2))
        
        try: inChunkPos[0]/=abs(inChunkPos[0])
        except:pass
        try: inChunkPos[1]/=abs(inChunkPos[1])
        except:pass
        
        '''
            
            There is sooooooo much lines omg

        '''

        self.get_chunk(chunkPosition).draw((int(drawOffset[0]+globalChunkOffset[0]), int(drawOffset[1]+globalChunkOffset[1])))
        if (inChunkPos[0]): self.get_chunk((chunkPosition[0]+int(inChunkPos[0]), chunkPosition[1])).draw((drawOffset[0]+globalChunkOffset[0]+inChunkPos[0]*(CHUNK_SIZE*SPRITE_SIZE), drawOffset[1]+globalChunkOffset[1]))
        if (inChunkPos[1]): self.get_chunk((chunkPosition[0], chunkPosition[1]+int(inChunkPos[1]))).draw((drawOffset[0]+globalChunkOffset[0], drawOffset[1]+globalChunkOffset[1]+inChunkPos[1]*(CHUNK_SIZE*SPRITE_SIZE)))
        if (inChunkPos[0] and inChunkPos[1]): self.get_chunk((chunkPosition[0]+int(inChunkPos[0]), chunkPosition[1]+int(inChunkPos[1]))).draw((drawOffset[0]+globalChunkOffset[0]+inChunkPos[0]*(CHUNK_SIZE*SPRITE_SIZE), drawOffset[1]+globalChunkOffset[1]+inChunkPos[1]*(CHUNK_SIZE*SPRITE_SIZE)))
#        self.chunks[chunkPosition].draw(drawOffset)
#        self.console.draw(drawOffset)

    
    def get_chunk(self, position):
        chunk = None
        try:
            chunk = self.chunks[tuple(position)]
        except:
            self.chunks[tuple(position)] = generateChunk(self, self.blockList.grass)
            chunk = self.chunks[tuple(position)]
        return chunk

    def get_chunkpos(self, position):
        return (int(numpy.floor(position[0]/CHUNK_SIZE)),
                int(numpy.floor(position[1]/CHUNK_SIZE)))


    def update(self, position):
        self.chunks[position].update()
