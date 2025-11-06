from textDrawer import *
import pygame

class Console:
    def __init__(self, world):
        self.world = world
        self.WIDTH, self.HEIGHT = world.window.get_size()
        self.logs = []

    def draw(self, offset):
        s = pygame.Surface((self.WIDTH, self.HEIGHT))
        s.set_alpha(200)
        s.fill((0,0,0))
        self.world.window.blit(s, (0,0))
        position = list(offset)
        maxY = 0
        img = textimg(" --- Values --- ")                       # VALUES
        '''
        self.world.window.blit(img, tuple(position))
        position[1]+=img.get_height()+2
        for name, value in self.elements:
            img = textimg(name + ": " + str(value()))
            self.world.window.blit(img, tuple(position))
            position[1]+=img.get_height()+2
            maxY = max(maxY, img.get_width())
            
        position[:] = [maxY+4, self.HEIGHT-img.get_height()-2]  # LOGS
        '''
        pygame.draw.line(self.world.window, (255,255,255), (maxY+2, 0),
                (maxY+2, self.HEIGHT), 2)
        for log in reversed(self.logs):
            draw_regular_text(self.world.window, log, position)
            position[1]-=img.get_height()
            if position[1]<0: break


