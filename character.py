# Ali Nosseir
# CS30
# Feb 15, 2020
# RPG Game class representing a character in the game

from random import random


class Character:
    """Represents a player in the game"""

    kills = 0

    def __init__(
        self,
        name,
        position=(0, 0),
        health=100,
        damage=15,
        kills_to_win=3,
        inventory=None,
    ):
        """Create an instance of a Character.

        Args:
            name (string): The name of the character
            position (tuple, optional): x y coordinates. Defaults to (0, 0).
            health (int, optional): Character health. Defaults to 100.
            damage (int, optional): Character attack damage. Defaults to 15.
            kills_to_win (int, optional): Kilss required to win. Defaults to 3.
            inventory (list[Item], optional): Character inventory. Default [].
        """
        # Workaround for mutable default values
        if not inventory:
            inventory = []

        self.inventory = inventory
        self.name = name
        self.health = health
        self.damage = damage
        self.kills_to_win = kills_to_win
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
- Inventory: {inventory}
- {self.kills} / {self.kills_to_win} Kills to Win"""

    def light_attack(self):
        """Get the damage of a light attack

        Returns:
            int: Damage
        """
        # Deal 1x damage
        return self.damage

    def heavy_attack(self):
        """Get the damage of a heavy attack

        Returns:
            int: Damage
        """
        # 50% chance of missing
        if random() < 0.5:
            return 0

        # Deal 2x damage
        return self.damage * 2

    def has_won(self):
        """Return true if the character has enough kills to win

        Returns:
            boolean: True if the character won, false otherwise
        """
        return self.kills >= self.kills_to_win


class Enemy:
    """Represents an enemy in the game"""

    def __init__(self, name, damage=20, health=40):
        """Create an instance of an enemy

        Args:
            name (string): The name of the enemy
            damage (int, optional): Enemy attack damage. Defaults to 10.
            health (int, optional): Enemy health. Defaults to 30.
        """
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self):
        """Get the damage of an attack

        Returns:
            int: Damage
        """
        return self.damage
