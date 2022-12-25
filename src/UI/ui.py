from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow,
        QHBoxLayout, QWidget, QPushButton, QVBoxLayout, QGroupBox,
        QMessageBox)
from PyQt5 import QtGui, QtCore, QtWidgets

from tile import Tile
from handparser import HandParser
from UI.gameview import GameView
from rules import Rules

class Window(QWidget):
    """Luokka vastaa pelin alussa tapahtuvan tiilien valinnan käsittelyssä UIssa.

    Attributes:
        selected_tiles: tiilet jotka pelaaja valitsee interaktiivisesti UIssa.
        playerpool: tiilet, joista pelaaja voi valita.
        mainLayout: layout, millä nivotaan yhteen loput layoutit.
        tämän lisäksi on eri layoutteja, mitkä nivotaan yhteen mainLayoutissa.
        playButton: Pelin aloitusnappi, kun tiilet on valittu.
        playertTiles: ensimmäinen puolisko tiilistä mistä pelaaja voi valita.
        playerTiles: toinen puolisko tiilistä mistä pelaaja voi valita.
    """
    def __init__(self,p1pool):
        super().__init__()

        self.selected_tiles = []
        self.playerpool = p1pool

        self.createTileSelection(p1pool)
        self.createPlayButton()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.playButton)
        self.mainLayout.addWidget(self.playerTiles)
        self.mainLayout.addWidget(self.playerTiles2)
        self.setLayout(self.mainLayout)
        
        self.setWindowTitle("Minefield Mahjong")


    def createTileSelection(self,p1pool):
        """Luo UI komponentit tiilien valintaa varten.

        Args:
            p1pool: pelaajan tiilet, mistä pelaaja voi valita, ja joista napit generoidaan.

        """
        self.playerTiles = QGroupBox("Select 13 tiles to play with, then continue")
        layout = QHBoxLayout()
        layout2 = QHBoxLayout()
        self.playerTiles2 = QGroupBox()
        p1poolfirst = p1pool[:17]
        p1poolsecond = p1pool[17:]
        for l in p1poolfirst:
            icon = QtGui.QIcon(f"src/UI/tiles/{l}.png")
            btn = QPushButton()
            btn.setText(l)
            btn.setCheckable(True)
            btn.setChecked(False)
            btn.setIcon(icon)
            btn.clicked.connect(self.tileStateChanged)
            size = QtCore.QSize(64,64)
            btn.setIconSize(size)
            btn.resize(64,64)
            btn.setStyleSheet("QPushButton::checked {background-color: red}")
            layout.addWidget(btn)
        for l in p1poolsecond:
            icon = QtGui.QIcon(f"src/UI/tiles/{l}.png")
            btn = QPushButton()
            btn.setText(l)
            btn.setCheckable(True)
            btn.setChecked(False)
            btn.setIcon(icon)
            btn.clicked.connect(self.tileStateChanged)
            size = QtCore.QSize(64,64)
            btn.setIconSize(size)
            btn.resize(64,64)
            btn.setStyleSheet("QPushButton::checked {background-color: red}")
            layout2.addWidget(btn)
        self.playerTiles.setLayout(layout)
        self.playerTiles2.setLayout(layout2)
        

    def createPlayButton(self):
        """Luo pelin aloitusnapin, joka aloittaa pelin.
        """
        self.playButton = QPushButton("Play with selected tiles")
        self.playButton.clicked.connect(self.startGame)

    def startGame(self):
        """startGame yrittää aloittaa pelin, ja jos se ei pysty aloittamaan
        peliä (liian lyhyt tai laiton käsi) se tekee virheen
        """
        self.selected_tiles.sort()
        p1hand = HandParser.parse_hand(self.selected_tiles, self.playerpool)
        if type(p1hand) == type(False) or Rules.is_tenpai(self.selected_tiles) == False:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Warning)
            error_box.setText("Invalid starting hand!")
            error_box.exec_()
        else:
            valid_box = QMessageBox()
            valid_box.setIcon(QMessageBox.Information)
            valid_box.setText("Valid starting hand")
            valid_box.exec_()
            game_view = GameView(p1hand)
#https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt/13103617#13103617
            for i in reversed(range(self.mainLayout.count())): 
                self.mainLayout.itemAt(i).widget().setParent(None)
            self.mainLayout.addWidget(game_view)
            

    def tileStateChanged(self):
        """Funktio mitä valitsee tai epävalitsee tiilen, kun pelaaja klikkaa sitä
        """
        if self.sender().isChecked():
            self.selected_tiles.append(self.sender().text())
        else:
            self.selected_tiles.remove(self.sender().text())
