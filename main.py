from character import Character
from map import Map
from menu import choose, move
from strings import help_message, title, win_message
from util import clear


class Game:
    def __init__(self):
        self.reset()
        self.run_state = {
            "menu": self.menu,
            "help": self.help,
            "moving": self.moving,
            "win": self.win,
            "reset": self.reset,
        }

    def menu(self):
        choice = choose(
            title,
            ["start", "help", "quit"],
            caps=True,
        )

        if choice == "start":
            self.state = "moving"
        elif choice == "help":
            self.state = "help"
        elif choice == "quit":
            self.state = "quit"

    def help(self):
        choose(help_message, ["Go Back"])
        self.state = "menu"

    def moving(self):
        clear()
        print(self.player, "\n")
        print(self.map)
        offset = move()
        pos = self.player.position
        new_pos = (pos[0] + offset[0], pos[1] + offset[1])

        if new_pos[0] < 0 or new_pos[0] >= self.map.width:
            return
        if new_pos[1] < 0 or new_pos[1] >= self.map.height:
            return

        tile = self.map.get_pos(*new_pos)

        if tile.hard:
            return

        if tile.pickup:
            self.player.inventory.append(tile.pickup)
            if tile.alt:
                self.map.set_pos(*new_pos, tile.alt)

        if tile.win:
            self.state = "win"

        self.player.position = new_pos

    def win(self):
        choice = choose(
            win_message,
            ["play again", "quit"],
            caps=True,
        )

        if choice == "play again":
            self.state = "reset"
        elif choice == "quit":
            self.state = "quit"

    def reset(self):
        self.player = Character("James", position=(0, 1))
        self.map = Map(self.player.get_pos)

        self.state = "menu"

    def play(self):
        while self.state != "quit":
            self.run_state[self.state]()


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
