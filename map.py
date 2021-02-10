from copy import deepcopy
from functools import reduce

from items import Heal
from menu import columnify


class Tile:
    view: str
    hard = False
    win = False
    pickup = None
    alt = None

    def __str__(self):
        return self.view


class Player(Tile):
    view = """\
James
James"""


class Wall(Tile):
    hard = True
    view = """\
wall
wall """


class Hut(Tile):
    view = """\
 hut
 hut """


class Grass(Tile):
    view = """\
grass
grass"""


class Goal(Tile):
    win = True
    view = """\
 win
 win """


class Potion(Tile):
    pickup = Heal("Potion", 20)
    view = """\
heal
heal """

    def __init__(self):
        self.alt = Grass()


class Map:
    def __init__(self, get_player_pos):
        self.get_player_pos = get_player_pos

        self.map = [
            [Wall(), Wall(), Wall(), Wall()],
            [Grass(), Grass(), Grass(), Grass()],
            [Potion(), Hut(), Grass(), Grass()],
            [Grass(), Grass(), Grass(), Grass()],
            [Wall(), Wall(), Wall(), Goal()],
        ]

    def __str__(self):
        x, y = self.get_player_pos()
        map_copy = deepcopy(self.map)
        map_copy[y][x] = Player()

        return "\n".join(
            reduce(
                lambda p, v: p + [*columnify(*map(str, v), sep=" ")],
                map_copy,
                [],
            )
        )

    def get_pos(self, x, y):
        return self.map[y][x]

    def set_pos(self, x, y, tile):
        self.map[y][x] = tile

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)
