class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Heal(Item):
    def __init__(self, name, healing):
        super().__init__(name)
        self.healing = healing
