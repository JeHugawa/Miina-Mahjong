from tile import Tile
from handparser import HandParser


wall = Tile.get_tilewall()
print(wall)
print("\n")
p1pool = wall[:34]
del wall[:34]
p2pool = wall[:34]
del wall[:34]

p1pool.sort()
p2pool.sort()

p1_selected_tiles = []
while len(p1_selected_tiles) < 13:
    print("tiles remaining")
    print(p1pool)
    selected_tile = input("select a tile:")
    p1_selected_tiles.append(selected_tile)

p2_selected_tiles = []
while len(p2_selected_tiles) < 13:
    print("tiles remaining")
    print(p2pool)
    selected_tile = input("select a tile:")
    p2_selected_tiles.append(selected_tile)

p1hand = HandParser.parse_hand(p1_selected_tiles, p1pool)
p2hand = HandParser.parse_hand(p2_selected_tiles, p2pool)


#todo: currently the program doesnt work if you give illegal discard
while True:
    print("player1 turn")
    p1hand.print_hand()
    discard = input("choose tile from pool to discard:")
    p1hand.discard(discard)
    p1hand.print_hand()
    print("_________________________________________________")
    print("player2 turn")
    p2hand.print_hand()
    discard = input("choose tile from pool to discard:")
    p2hand.discard(discard)
    p2hand.print_hand()
    if len(p2hand.tilepool) == 4:
        print("Draw")
        break
