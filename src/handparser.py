import copy
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
    @staticmethod
    def parse_hand(selections: list, tiles):
        hand = []
        tiles_copy = copy.deepcopy(tiles)
        for picked_tile in selections: #pylint: disable=not-an-iterable
            try:
                tiles_copy.remove(picked_tile)
            except ValueError:
                return False
            hand.append(picked_tile)
        if len(hand) == 13:
            playerhand = PlayingHand(hand, [], tiles_copy)
            return playerhand
        return False
