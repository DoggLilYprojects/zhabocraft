import numpy
import pygame
from items import *

INVENTORY_RATIO = (3, 5)
DRAW_SIZE = 51

class Inventory:
    def __init__(self, entity):
        self.entity         = entity
        self.window         = self.entity.world.window
        self.slots          = numpy.empty(INVENTORY_RATIO, dtype=object)
        self.slots[:]       = None
        self.selectedSlot   = 0

    def replace(self, slot1, slot2):
        self.slots[slot1], self.slots[slot2] = self.slots[slot2], self.slots[slot1]

    def rightClicked(self, mouseX, mouseY):
        self.slots[0][self.selectedSlot].rightClicked(mouseX, mouseY)

    def leftClikced(self, mouseX, mouseY):
        self.slots[0][self.selectedSlot].leftClicked(mouseX, mouseY)
    
    def remove(self, obj):
        for y in range(self.slots.shape[0]):
            for x in range(self.slots.shape[1]):
                if self.slots[y][x] == obj:
                    self.slots[y][x] = None

    def pickup(self, item):
        isItemStackable = isinstance(item, StackableItem)
        for row in range(self.slots.shape[0]):
            for column in range(self.slots.shape[1]):
                slotItem = self.slots[row][column]
                if slotItem == None:
                    self.slots[row][column]=item
                    return True
                if slotItem.name == item.name and isItemStackable and isinstance(slotItem, StackableItem):
                    slotItem.count+=item.count
                    return True

        return False

    def draw(self):
        for y in range(self.slots.shape[0]):
            for x in range(self.slots.shape[1]):
                pygame.draw.rect(self.window, (255, 255, 255), (x*DRAW_SIZE, y*DRAW_SIZE, DRAW_SIZE, DRAW_SIZE), 2)
                if self.slots[y][x] != None:
                    self.window.blit(pygame.transform.scale(self.slots[y][x].sprite, (DRAW_SIZE, DRAW_SIZE)), (x*DRAW_SIZE, y*DRAW_SIZE))
