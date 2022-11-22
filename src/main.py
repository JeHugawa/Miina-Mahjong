from tile import Tile
from handparser import HandParser, PlayingHand


wall = Tile.get_tilewall()
print(wall)
print("\n")
p1pool = wall[:34]
del wall[:34]
p2pool = wall[:34]
del wall[:34]

p1pool.sort()
p2pool.sort()
print(p1pool)

#TODO: pop cant be used to pick tiles from certain position as it removes the pick from list. there's other implementations but its better to implement it with selecting tiles instead of their relative position
p1hand = HandParser.parsehand([0,0,0,0,0,0,0,0,0,0,0,0,0], p1pool)
p2hand = HandParser.parsehand([0,0,0,0,0,0,0,0,0,0,0,0,0], p2pool)

PlayingHand.printhand(p1hand)
