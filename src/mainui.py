from UI.ui import Window
from PyQt5.QtWidgets import QApplication
from tile import Tile
from handparser import HandParser

wall = Tile.get_tilewall()
p1pool = wall[:34]
del wall[:34]
p2pool = wall[:21]
del wall[:21]

p1pool.sort()

app = QApplication([])
app.setStyle('Fusion')
window = Window(p1pool,p2pool)
window.show()
app.exec_()
