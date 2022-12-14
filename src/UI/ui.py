from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow,
        QHBoxLayout, QWidget, QPushButton, QVBoxLayout, QGroupBox)
from PyQt5 import QtGui, QtCore

from tile import Tile
from handparser import HandParser

class Window(QWidget):
    def __init__(self,p1pool):
        super().__init__()

        self.createTileSelection(p1pool)
        self.createPlayButton()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.playButton)
        mainLayout.addWidget(self.playerTiles)
        self.setLayout(mainLayout)
        
        self.playButton.clicked.connect(self.startGame)

        self.setWindowTitle("Minefield Mahjong")


    def createTileSelection(self,p1pool):
        self.playerTiles = QGroupBox("Select 13 tiles to play with, then continue")
        layout = QHBoxLayout()
        for l in p1pool:
            icon = QtGui.QIcon(f"src/UI/tiles/{l}.png")
            btn = QPushButton()
            btn.setCheckable(True)
            btn.setChecked(False)
            btn.setIcon(icon)
            size = QtCore.QSize(64,64)
            btn.setIconSize(size)
            btn.resize(64,64)
            btn.setStyleSheet("QPushButton::checked {background-color: red}")
            layout.addWidget(btn)
        self.playerTiles.setLayout(layout)


    def createPlayButton(self):
        self.playButton = QPushButton("Play with selected tiles")


    def startGame(self):
        p1hand = HandParser.parse_hand(selected_tiles, playerpool)
