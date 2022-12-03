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

#TODO: pop cant be used to pick tiles from certain position as it removes the pick from list.

p1hand = HandParser.parse_hand([0,0,0,0,0,0,0,0,0,0,0,0,0], p1pool)
p2hand = HandParser.parse_hand([0,0,0,0,0,0,0,0,0,0,0,0,0], p2pool)


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
