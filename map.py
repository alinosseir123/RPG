# Ali Nosseir
# CS30
# Feb 23, 2020
# RPG Game map and tiles to be used on the map

from copy import deepcopy
from functools import reduce

from colorama import Back

from items import Heal
from menu import columnify


class Tile:
    # The string for displaying the tile
    view: str
    # True if a player can't cross the tile
    hard = False
    # True if going on the tile should trigger a win
    win = False
    # The item to pick up when going on the tile
    pickup = None
    # The tile to replace with when an item is picked up
    alt = None

    def __str__(self):
        """Get a string representation of the tile

        Returns:
            string: The view of the tile
        """
        return self.view


class Player(Tile):
    view = f"""\
{Back.YELLOW}
{Back.YELLOW}     """


class Wall(Tile):
    hard = True
    view = f"""\
{Back.WHITE}
{Back.WHITE}     """


class Rock(Tile):
    hard = True
    view = f"""\
{Back.BLACK}
{Back.BLACK}     """


class Grass(Tile):
    view = f"""\
{Back.GREEN}
{Back.GREEN}     """


class Goal(Tile):
    win = True
    view = f"""\
{Back.CYAN}
{Back.CYAN}     """


class Potion(Tile):
    pickup = Heal("Potion", 20)
    view = f"""\
{Back.GREEN}  {Back.MAGENTA} {Back.GREEN}
{Back.GREEN} {Back.MAGENTA}   {Back.GREEN} """

    def __init__(self):
        self.alt = Grass()


class Map:
    def __init__(self, get_player_pos):
        """Create an instance of a Map

        Args:
            get_player_pos (function): Callback to get the latest player pos
        """
        self.get_player_pos = get_player_pos

        self.map = [
            [Wall(), Wall(), Wall(), Wall(), Wall()],
            [Grass(), Grass(), Grass(), Grass(), Grass()],
            [Potion(), Rock(), Grass(), Grass(), Grass()],
            [Grass(), Grass(), Grass(), Grass(), Grass()],
            [Grass(), Grass(), Grass(), Grass(), Grass()],
            [Wall(), Wall(), Wall(), Goal(), Wall()],
        ]

    def __str__(self):
        """Get a string representation of the map

        Returns:
            string: Map laid out as a table
        """
        x, y = self.get_player_pos()
        map_copy = deepcopy(self.map)
        map_copy[y][x] = Player()

        return "\n".join(
            reduce(
                lambda p, v: p + [*columnify(*map(str, v), sep="")],
                map_copy,
                [],
            )
            + [Back.RESET]
        )

    def get_pos(self, x, y):
        """Get the tile at the given coordinates

        Args:
            x (int): x-coordinate
            y (int): y-coordinate

        Returns:
            Tile: Data at the given coordinates
        """
        return self.map[y][x]

    def set_pos(self, x, y, tile):
        """Set the tite at the given coordinates

        Args:
            x (int): x-coordinate
            y (int): y-coordinate
            tile (Tile): Data to be set at the given coordinates
        """
        self.map[y][x] = tile

    @property
    def width(self):
        """Get the width of the map

        Returns:
            int: width
        """
        return len(self.map[0])

    @property
    def height(self):
        """Get the height of the map

        Returns:
            int: height
        """
        return len(self.map)
