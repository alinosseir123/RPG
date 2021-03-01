# Ali Nosseir
# CS30
# Feb 15, 2020
# RPG Game main game logic

from functools import partial

from character import Character
from items import Heal
from keypress import keypress
from map import Map
from menu import choose, move
from strings import (
    death_message,
    fight_message,
    help_message,
    kill_message,
    lose_message,
    title,
    win_message,
)
from util import clear


class Game:
    """Game logic and state"""

    def __init__(self):
        """Create an instance of the game.

        Call the play method to begin the gameplay loop.
        """
        # Reset all game state data
        self.reset()

        # Map gameplay states to the corresponding methods
        self.run_state = {
            "menu": self.menu,
            "help": self.help,
            "moving": self.moving,
            "fighting": self.fighting,
            "win": partial(self.end, win=True),
            "lose": partial(self.end, win=False),
            "reset": self.reset,
        }

    def menu(self):
        """Display the main menu.

        Presents options to the player to start, get help with controls,
        or exit the game.
        """
        # Wait for the player to choose an option
        choice = choose(
            title,
            ["start", "help", "quit"],
            caps=True,
        )

        # Conditionally sets the state based on the player's input
        if choice == "start":
            self.state = "moving"
        elif choice == "help":
            self.state = "help"
        elif choice == "quit":
            self.state = "quit"

    def help(self):
        """Display a help message with controls for the game."""
        # Wait for the player to go back to the main screen
        choose(help_message, ["Go Back"])
        self.state = "menu"

    def moving(self):
        """Display the map and wait for a directional key to be pressed."""
        # Clear the screen
        clear()

        # Display current information about the player
        print(self.player, "\n")

        # Dispaly the map
        print(self.map)

        # Wait for the player to choose a direction
        offset = move()
        pos = self.player.position

        # Create a temporary variable with the new position of the player
        # after their movement
        new_pos = (pos[0] + offset[0], pos[1] + offset[1])

        # Verify the movement is valid
        if new_pos[0] < 0 or new_pos[0] >= self.map.width:
            return
        if new_pos[1] < 0 or new_pos[1] >= self.map.height:
            return

        # Get information about the tile the player is now on
        tile = self.map.get_pos(new_pos)

        # Prevent player entering an impassable tile
        if tile.hard:
            return

        # Pick up an item from the tile
        if tile.pickup:
            self.player.inventory.append(tile.pickup)

            # Replace the picked up item with its after-pickup tile
            if tile.alt:
                self.map.set_pos(new_pos, tile.alt)

        # Fight an enemy from the tile
        if tile.enemy:
            self.target = tile.enemy
            self.state = "fighting"

            # Prepare after-kill tile
            if tile.alt:
                self.target_alt = tile.alt

        # Set the state to win if the tile is a win tile
        if tile.win and self.player.has_won():
            self.state = "win"

        # Save the new position to the game state
        self.player.position = new_pos

    def fighting(self):
        """Display combat information and choose an attack"""
        # Clear the screen
        clear()

        # Display information and wait for player to choose an attack
        choice = keypress(
            fight_message.format(
                self.target.name, self.target.health, self.player.health
            ),
            ["h", "l"],
        )

        if choice == "h":
            # Deduct heavy attack damage from enemy health
            self.target.health -= self.player.heavy_attack()

        elif choice == "l":
            # Deduct light attack damage from enemy health
            self.target.health -= self.player.light_attack()

        # Deduct enemy attack damage from player health
        self.player.health -= self.target.attack()

        if self.player.health <= 0 or self.target.health <= 0:

            target_name = self.target.name

            # If enemy is killed display information and go back to map
            if self.target.health <= 0:
                print(kill_message.format(target_name))

                # Add a kill to the player
                self.player.kills += 1

                # Reset target to none
                self.target = None

                # Replace the enemy tile with its after-pickup tile
                if self.target_alt:
                    self.map.set_pos(self.player.position, self.target_alt)

                self.state = "moving"

            # If player is killed display information and loss message
            if self.player.health <= 0:
                print(death_message.format(target_name))

                self.state = "lose"

            keypress("Press any key to continue")

    def end(self, win):
        """Display a win message.

        Presents options for the player to start again or quit.
        """

        if not win:
            for i, item in enumerate(self.player.inventory):
                if isinstance(item, Heal):
                    del self.player.inventory[i]
                    print("Your health potion revived you")
                    keypress("Press any key to continue")
                    if self.target:
                        self.state = "fighting"
                    else:
                        self.state = "moving"
                    self.player.health += 50
                    return

        # Wait for the player to choose an option
        choice = choose(
            win_message if win else lose_message,
            ["play again", "quit"],
            caps=True,
        )

        # Conditionally sets the state based on the player's input
        if choice == "play again":
            self.state = "reset"
        elif choice == "quit":
            self.state = "quit"

    def reset(self):
        """Reset the game state for replayability."""
        # Creates a new player instance at the default position
        self.player = Character("Player", position=(0, 1))
        self.player_won = False

        # Creates the map instance and provides a function to get the player's
        # position so the map stays updated
        self.map = Map(self.player.get_pos)

        # Set the active fighting target to none
        self.target = None
        self.target_alt = None

        self.state = "menu"

    def play(self):
        """Start the main gameplay loop"""
        # Call respective gameplay methods based on the game state
        while self.state != "quit":
            self.run_state[self.state]()


def main():
    """Create game instance and start main loop"""
    game = Game()
    game.play()


main()
