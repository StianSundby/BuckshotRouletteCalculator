class Item:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

class Items:
    def __init__(self):
        self.adrenaline = Item("Adrenaline", 0)
        self.beerCan = Item("Beer Can", 1)
        self.burnerPhone = Item("Burner Phone", 0)
        self.cigarettePack = Item("Cigarette Pack", 0)
        self.expiredMedicine = Item("Expired Medicine", 0)
        self.foldingSaw = Item("Folding Saw", 0)
        self.handcuffs = Item("Handcuffs", 0)
        self.inverter = Item("Inverter", 0)
        self.magnifyingGlass = Item("Magnifying Glass", 0)

    def use_item(self, item: Item):
        if item.quantity > 0:
            item.quantity -= 1
            return True
        else:
            return False