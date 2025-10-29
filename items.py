import pygame

class Item:
    def __init__(self, name):
        self.name = name
        self.sprite = pygame.image.load(f"sprites//{name}.png")
    
    def rightClicked(self):
        pass

    def leftClicked(self):
        pass

    def kill(self):
        del self

class BreakableItem(Item):
    def __init__(self, name, durability=128):
        super().__init__(name)
        self.durability = durability

    def afterUse(self):
        self.durability-=1
        if self.durability <= 0:
            self.kill()

class ShovelItem(BreakableItem):
    def __init__(self, shovelType, durability=128):
        super().__init__(f"{shovelType} shovel", durability)

    def rightClicked(self):

        afterUse()
