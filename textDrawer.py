import pygame

pygame.init()

FONT = pygame.font.Font("kongtext.ttf", 16)

def textimg(text):
    return FONT.render(text, False, (255,255,255))

spacew = textimg(" ").get_width()

def draw_regular_text(window, text, position):
    window.blit(textimg(text), position)

def draw_boundered_text(window, text, position, bounder):
    list = text.split()
    W = 0
    for count, e in enumerate(list):
        img = textimg(e)
        if W+img.get_width()>abs(position[0]-bounder):
            if count == 0: break
            else:
                W = 0
                position[1]+=img.get_height()
                window.blit(img, (W, position[1]))
                W += img.get_width()+spacew
        else:
            window.blit(img, (W, position[1]))
            W += img.get_width()+spacew
