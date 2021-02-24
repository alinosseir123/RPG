# Ali Nosseir
# CS30
# Feb 23, 2020
# RPG Game menus for player interaction

from itertools import zip_longest

from keypress import keypress
from util import clear


def columnify(*args, sep=" | "):
    """Separate strings into columns.

    Args:
        *args (str): Each string represents a column
        sep (str, optional): Separator between columns. Defaults to " | ".

    Yields:
        string: A row from the table
    """
    # Nested list, where the outer list represents columns
    # and the inner list represents rows
    parts = [x.splitlines() for x in args]

    # List of the maximum line length of each column
    lengths = [max(map(len, x)) for x in parts]

    # Iterate over each row of the table
    for line in zip_longest(*parts, fillvalue=""):
        # Yield the row with each item separated by the separater
        # and padded to the maximum line length of each column
        yield sep.join(
            content.ljust(length) for content, length in zip(line, lengths)
        )


def choose(message, options, caps=False):
    """Prompt the user to select from a list of options.

    Args:
        message (string): Message displayed alongside the options
        options (list[str]): Options to present to the user
        caps (bool, optional): Automatically capitalize. Defaults to False.

    Returns:
        string: Option selected by the user
    """
    # Capitalize options if requested
    fmt_options = [x.capitalize() if caps else x for x in options]

    # Length of each option, minimum of 20
    length = max(20, max(map(len, options)))

    selected = 0
    # Wait for a selection to be made by the user
    while True:
        clear()

        # Print each option
        info = ""
        for i, option in enumerate(fmt_options):
            # Display a border around the currently seleced option
            if i == selected:
                info += "-" * (length + 4) + "\n"
                info += f"| {option.ljust(length)} |\n"
                info += "-" * (length + 4) + "\n"
            else:
                info += "\n"
                info += f"  {option}\n"
                info += "\n"

        # Display the message beside the options
        print("\n".join(columnify(message, info)))

        # Wait for a valid keypress
        key = keypress("", ["w", "s", "enter"])

        # Conditionally handle the keypress and return if an option is selected
        if key == "enter":
            return options[selected]
        if key == "w" and selected > 0:
            selected -= 1
        if key == "s" and selected < len(options) - 1:
            selected += 1


# Map keypresses to position offsets
direction = {
    "w": (0, -1),
    "a": (-1, 0),
    "s": (0, 1),
    "d": (1, 0),
}


def move():
    """Wait for a directional key to be pressed

    Returns:
        str: Directional key pressed. One of W, A, S, D.
    """
    key = keypress("", ["w", "a", "s", "d"])
    return direction[key]
