from PyQt5 import *
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                            QHBoxLayout, QGroupBox,QMessageBox)
import random

from tile import Tile
from handparser import PlayingHand
from rules import Rules

class GameView(QWidget):
    """Luokka vastaa pelin kulusta kun peli on aloitettu tiilien valitsemisen jälkeen

    Attributes:
    """
    def __init__(self, p1PlayingHand,p2pool):
        super().__init__()
        
        self.createPlayerHand(p1PlayingHand)
        self.createPlayerTilePool(p1PlayingHand.tilepool)
        self.createDiscardPool()
        self.winningTiles = Rules.return_winning_tiles(p1PlayingHand.hand)
        self.p2pool = p2pool
        self.createAIDiscards()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.aiDiscards)
        mainLayout.addWidget(self.discards)
        mainLayout.addWidget(self.playerHand)
        mainLayout.addWidget(self.playerTilePool)
        self.setLayout(mainLayout)


    def createPlayerHand(self, player_hand):
        """Generoi pelaajan käden UIhin hänen valinnoistaan

        Args:
            player_hand: pelaajan valitsemat tiilet joiden perusteella ne lisätään UIhin
        """
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
        """Generoi UIhin pelaajan jäljellä olevat tiilet, mistä hän voi heittää pois tiiliä.

        Args:
            tilepool: pelaajan jäljellä olevat tiilet
        """
        self.playerTilePool = QGroupBox("Avaible discards")
        layout = QHBoxLayout()
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
        """Funktio mitä kutsutaan kun pelaaja heittää pois tiilen
        """
        discard = self.sender()
        discard.setEnabled(False)
        self.discards_layout.addWidget(discard)
        
        enemyDiscard = random.choice(self.p2pool)
        self.p2pool.remove(enemyDiscard)
        icon = QtGui.QIcon(f"src/UI/tiles/{enemyDiscard}.png")
        button = QPushButton()
        button.setIcon(icon)
        button.setEnabled(False)
        button.setIconSize(QtCore.QSize(64,64))
        button.resize(64,64)
        self.aiDiscards_layout.addWidget(button)
        if enemyDiscard in self.winningTiles:
            winning_box = QMessageBox()
            winning_box.setIcon(QMessageBox.Information)
            winning_box.setText("Congrats! you win with " + enemyDiscard)
            winning_box.exec_()
            exit()


    def createDiscardPool(self):
        """Luo UIhin poisheitetyille tiilille oman alueen UIssa
        """
        self.discards = QGroupBox("Discarded tiles")
        self.discards_layout = QHBoxLayout()
        self.discards.setLayout(self.discards_layout)

    def createAIDiscards(self):
        self.aiDiscards = QGroupBox("Opponents Dicards")
        self.aiDiscards_layout = QHBoxLayout()
        self.aiDiscards.setLayout(self.aiDiscards_layout)
