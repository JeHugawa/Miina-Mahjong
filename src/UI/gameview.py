from PyQt5 import *
from PyQt5.QtWidgets import QWidget

from tile import Tile
from handparser import PlayingHand

class GameView(QWidget):
    def __init__(self, p1PlayingHand):
        super().__init__()
