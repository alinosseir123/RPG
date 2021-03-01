# Ali Nosseir
# CS30
# Feb 15, 2020
# RPG Game items that can be picked up by the player


class Item:
    """Represnts an item to be picked up"""

    def __init__(self, name):
        """Create an instance of an Item.

        Args:
            name (string): The name of the item
        """
        self.name = name

    def __str__(self):
        """Get a string representation of the item.

        Returns:
            string: Representation of item attributes
        """
        return self.name


class Heal(Item):
    """Represents an item to be picked up that can provide healing"""

    def __init__(self, name, healing):
        """Create an instance of a Heal Item.

        Args:
            name (string): The name of the item
            healing (int): The amount of health the item heals
        """
        super().__init__(name)
        self.healing = healing
