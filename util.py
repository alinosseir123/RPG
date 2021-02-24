# Ali Nosseir
# CS30
# Feb 23, 2020
# RPG Game addition utility functions

from os import system
from sys import platform


def clear():
    """Clear the console"""
    system("cls" if platform == "win32" else "clear")
