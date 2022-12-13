from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow,
        QHBoxLayout, QWidget, QPushButton, QVBoxLayout, QGroupBox)
from PyQt5 import QtGui, QtCore

class Window(QWidget):
    def __init__(self,p1pool):
        super().__init__()

        self.createTileSelection(p1pool)
        self.createPlayButton()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.playButton)
        mainLayout.addWidget(self.playerTiles)
        self.setLayout(mainLayout)

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
            btn.resize(1000,1000)
            btn.setStyleSheet("QPushButton::checked {background-color: red}")
            layout.addWidget(btn)
        self.playerTiles.setLayout(layout)


    def createPlayButton(self):
        self.playButton = QPushButton("Play with selected tiles")
