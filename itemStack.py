

class ItemStack:
    def __init__(self, item=None):
        self.count = 0
        self.durability = 0
        self.item = None
        if item!=None:
            self.setItem(item)

    def setItem(self, item):
        self.item = item
        self.count = item.count
        self.durability = item.durability
    
    def useItem(self, xWorldPos, yWorldPos):
        self.item.use(self)
