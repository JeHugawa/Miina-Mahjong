#lass for parsing hand
class PlayingHand:
    def __init__(self, hand: list, discards: list, tilepool: list):
        self.hand = hand
        self.discards = discards
        self.tilepool = tilepool

    def print_hand(self):
        print("Players hand")
        print(self.hand)
        print("________________")
        print("Remaining tiles")
        print(self.tilepool)
        print("_________________")
        print("Discard pool")
        print(self.discards)

    def discard(self,discard):
        self.tilepool.remove(discard)
        self.discards.append(discard)


class HandParser:
    @classmethod
    def parse_hand(cls,selections: list, tiles):
        hand = []
        for picked_tile in selections: #pylint: disable=not-an-iterable
            try:
                tiles.remove(picked_tile)
            except ValueError:
                return False
            hand.append(picked_tile)
        playerhand = PlayingHand(hand, [], tiles)
        return playerhand
