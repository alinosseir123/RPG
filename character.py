class Character:
    def __init__(
        self,
        name,
        position=(0, 0),
        health=100,
        inventory=None,
    ):
        if not inventory:
            inventory = []
        self.inventory = inventory
        self.name = name
        self.health = health
        self.position = position

    def get_pos(self):
        return self.position

    def __str__(self):
        inventory = (
            ", ".join(map(str, self.inventory))
            if len(self.inventory) > 0
            else "Empty"
        )
        return f"""\
{self.name}:
- {self.health} Health Remaining
- Inventory: {inventory}"""
