import numpy
import pygame
from items import *
from itemStack import *
from textDrawer import draw_regular_text 

INVENTORY_RATIO = (3, 5)
DRAW_SIZE = 51

class Inventory:    
    def __init__(self, entity):
        self.entity         = entity
        self.window         = self.entity.world.window
        self.slots          = numpy.empty(INVENTORY_RATIO, dtype=object)
        for row in range(self.slots.shape[0]):
            for column in range(self.slots.shape[1]):
                self.slots[row][column] = ItemStack(self.entity.world.itemList.air)
        self.selectedSlot   = 0

    def replace(self, slot1, slot2):
        slot1Item = self.slots[slot1]
        self.getSlot(slot1).setItem(self.slots[slot2].item)
        self.getSlot(slot2).setItem(slot1Item)

    def getSlot(self, slot):
        rows, cols = self.slots.shape
        row = slot // cols
        col = slot % cols
        return self.slots[row][col]

    def useItem(self, xWorldPos, yWorldPos):
        self.slots[0][self.selectedSlot].useItem(xWorldPos, yWorldPos)

    def pickup(self, item):
        for row in range(self.slots.shape[0]):
            for column in range(self.slots.shape[1]):
                slot_index = row * self.slots.shape[1] + column
                itemStack = self.getSlot(slot_index)
                if itemStack.item == self.entity.world.itemList.air:
                    itemStack.setItem(item)
                    return True
                elif itemStack.item.name == item.name:
                    itemStack.count+=1        #think about other situations in this case
                    return True
        return False


    def draw(self):
        for y in range(self.slots.shape[0]):
            for x in range(self.slots.shape[1]):
                pygame.draw.rect(self.window, (255, 255, 255), (x*DRAW_SIZE, y*DRAW_SIZE, DRAW_SIZE, DRAW_SIZE), 2)
                try:
                    itemStack = self.getSlot(y * self.slots.shape[0] + x)
                    self.window.blit(pygame.transform.scale(itemStack.item.sprite, (DRAW_SIZE - 4, DRAW_SIZE - 4)), (x * DRAW_SIZE + 2, y * DRAW_SIZE + 2))
                    if itemStack.count-1:
                        draw_regular_text(self.entity.world.window, str(itemStack.count), (x * DRAW_SIZE + 2, y * DRAW_SIZE + 2))
                except:pass

