from textDrawer import *
import pygame

class Console:
    def __init__(self, window, elements):
        self.elements = elements
        self.window = window
        self.WIDTH, self.HEIGHT = window.get_size()
        self.logs = []

    def draw(self):
        s = pygame.Surface((self.WIDTH, self.HEIGHT))
        s.set_alpha(200)
        s.fill((0,0,0))
        self.window.blit(s, (0,0))
        position = [0,0]
        img = textimg(" --- Values --- ")                       # VALUES
        self.window.blit(img, tuple(position))
        position[1]+=img.get_height()+2
        maxY = 0
        for name, value in self.elements:
            img = textimg(name + ": " + str(value()))
            self.window.blit(img, tuple(position))
            position[1]+=img.get_height()+2
            maxY = max(maxY, img.get_width())
            
        position[:] = [maxY+4, self.HEIGHT-img.get_height()-2]  # LOGS
        pygame.draw.line(self.window, (255,255,255), (maxY+2, 0),
                (maxY+2, self.HEIGHT), 2)
        for log in reversed(self.logs):
            draw_regular_text(self.window, log, position)
            position[1]-=img.get_height()
            if position[1]<0: break


