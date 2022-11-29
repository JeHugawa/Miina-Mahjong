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
#There's other implementations but its better to implement it with selecting tiles instead of their relative position.

p1hand = HandParser.parse_hand([0,0,0,0,0,0,0,0,0,0,0,0,0], p1pool)
p2hand = HandParser.parse_hand([0,0,0,0,0,0,0,0,0,0,0,0,0], p2pool)


#todo: currently the program doesnt work if you give illegal discard
while True:
    print("player1 turn")
    PlayingHand.print_hand(p1hand)
    discard = input("choose tile from pool to discard:")
    PlayingHand.discard(p1hand,discard)
    PlayingHand.print_hand(p1hand)
    print("_________________________________________________")
    print("player2 turn")
    PlayingHand.print_hand(p2hand)
    discard = input("choose tile from pool to discard:")
    PlayingHand.discard(p2hand,discard)
    PlayingHand.print_hand(p2hand)
    if len(p2hand.tilepool) == 4:
        print("Draw")
        break
