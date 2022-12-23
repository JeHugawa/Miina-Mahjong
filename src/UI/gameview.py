from PyQt5 import *
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                            QHBoxLayout, QGroupBox)

from tile import Tile
from handparser import PlayingHand

class GameView(QWidget):
    def __init__(self, p1PlayingHand):
        super().__init__()
        
        self.createPlayerHand(p1PlayingHand)
        self.createPlayerTilePool(p1PlayingHand.tilepool)
        self.createDiscardPool()

        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(QPushButton())
        mainLayout.addWidget(self.discards)
        mainLayout.addWidget(self.playerHand)
        mainLayout.addWidget(self.playerTilePool)
        self.setLayout(mainLayout)


    def createPlayerHand(self, player_hand):
        self.playerHand = QGroupBox("Player Hand")
        layout = QHBoxLayout()
        p1_hand = player_hand.hand
        for tile in p1_hand:
            icon = QtGui.QIcon(f"src/UI/tiles/{tile}.png")
            button = QPushButton()
            button.setEnabled(False)
            button.setIcon(icon)
            size = QtCore.QSize(64,64)
            button.setIconSize(size)
            button.resize(64,64)
            layout.addWidget(button)
        self.playerHand.setLayout(layout)


    def createPlayerTilePool(self, tilepool):
        self.playerTilePool = QGroupBox("Avaible discards")
        layout = QHBoxLayout()
        print(tilepool)
        for tile in tilepool:
            icon = QtGui.QIcon(f"src/UI/tiles/{tile}.png")
            button = QPushButton()
            button.setIcon(icon)
            size = QtCore.QSize(64,64)
            button.setIconSize(size)
            button.resize(64,64)
            layout.addWidget(button)
            button.clicked.connect(self.discardTile)
        self.playerTilePool.setLayout(layout)


    def discardTile(self):
        discard = self.sender()
        discard.setEnabled(False)
        self.discards_layout.addWidget(discard)

    def createDiscardPool(self):
        self.discards = QGroupBox("Discarded tiles")
        self.discards_layout = QHBoxLayout()
        self.discards.setLayout(self.discards_layout)
