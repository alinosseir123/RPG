# Ali Nosseir
# CS30
# Feb 23, 2020
# RPG Game class representing a character in the game


class Character:
    def __init__(
        self,
        name,
        position=(0, 0),
        health=100,
        inventory=None,
    ):
        """Create an instance of a Character.

        Args:
            name (string): The name of the character
            position (tuple, optional): x y coordinates. Defaults to (0, 0).
            health (int, optional): Character health. Defaults to 100.
            inventory (list[Item], optional): Character inventory. Default [].
        """
        # Workaround for mutable default values
        if not inventory:
            inventory = []

        self.inventory = inventory
        self.name = name
        self.health = health
        self.position = position

    def get_pos(self):
        """Get the character's position.

        Returns:
            tuple: Character position
        """
        return self.position

    def __str__(self):
        """Get a string representation of the character.

        Returns:
            string: Formatted information about the character
        """
        inventory = (
            ", ".join(map(str, self.inventory))
            if len(self.inventory) > 0
            else "Empty"
        )
        return f"""\
{self.name}:
- {self.health} Health Remaining
- Inventory: {inventory}"""
