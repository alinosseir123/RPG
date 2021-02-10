from os import system
from sys import platform


def clear():
    system("cls" if platform == "win32" else "clear")
