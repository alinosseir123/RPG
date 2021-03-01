# Ali Nosseir
# CS30
# Feb 15, 2020
# RPG Game strings to be displayed to the player

# Title to be displayed on the main menu
title = "RPG Game"

# Information to be displayed on the help page
help_message = (
    "Use the arrow keys or WASD\n"
    "to move and navigate the menus.\n"
    "Press enter to select.\n"
    "Press Q at any time to quit."
)

# Message to be displayed when the player wins
win_message = "You Win!\nWould you like to play again?"

# Message to be displayed when the player loses
lose_message = "You Lost. Would you like to play again?"

# Information to be displayed when fighting
# Format: [Enemy name, Enemy health, Player health]
fight_message = (
    "You encounted a {}!\n"
    "It has {} health remaining.\n"
    "You have {} health remaining.\n"
    "\n"
    "What would you like to do?\n"
    "H - Heavy attack. 2x damage, 50% accurary\n"
    "L - Light attack. 1x damage, 100% accuracy\n"
    "\n"
    "Press H or L\n"
)

# Message to be displayed after killing an enemy
# Format: [Enemy name]
kill_message = "You killed the {}!"

# Message to be displayed after dying from an enemy
# Format: [Enemy name]
death_message = "You were killed by the {}."
