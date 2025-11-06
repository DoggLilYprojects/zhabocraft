from items import *

shovel=None

def init(world):
    global shovel

    shovel = ShovelItem(world, "Wooden")

