#lass for parsing hand
class PlayingHand:
    def __init__(self, hand: list, discards: list, tilepool: list):
        self.hand = hand
        self.discards = discards
        self.tilepool = tilepool

    def print_hand(playerhand):
        print("Players hand")
        print(playerhand.hand)
        print("________________")
        print("Remaining tiles")
        print(playerhand.tilepool)
        print("_________________")
        print("Discard pool")
        print(playerhand.discards)

    def discard(playerhand,discard):
        playerhand.tilepool.remove(discard)
        playerhand.discards.append(discard)


class HandParser:
    def parse_hand(selections,tiles):
        hand = []
        for x in selections:
#TODO: Remove usage of pop and pick tiles instead of positions
            hand.append(tiles.pop(x))
        playerhand = PlayingHand(hand, [], tiles)
        return playerhand
