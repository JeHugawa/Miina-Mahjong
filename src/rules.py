import re
from collections import defaultdict

from tile import Tile
class Rules:

    @classmethod
    def is_pon(cls,selection):
        if selection[0] == selection[1] == selection[2]:
            return True
        return False

    @classmethod
    def is_chi(cls,selection):
        selection = sorted(selection)
        if selection[0] < selection[1] < selection[2]:
            return True
        return False

    @classmethod
    def is_pair(cls,selection):
        if selection[0] == selection[1]:
            return True
        return False


    #check how many suits
    @classmethod
    def suit_counter(cls,hand):
        amount = {}
        for tile in hand:
            tile = re.sub(r'\d+', '', tile)
            amount[tile] = amount.setdefault(tile,0) +1
        waiting_suits = []
        for key in amount:
            if amount[key] % 3 != 0:
                waiting_suits.append(key)
        return waiting_suits

    @classmethod
    def check_winning_tiles(cls, hand,waiting_suits):
        pass
        # TODO
        #return winning_tiles


    #for a valid hand you need 4 sets and a pair
    @classmethod
    def check_hand_completeness(cls,hand):
        if len(hand) != 14:
            return False
        # check_winning_tiles-> if in tiles return true

    @classmethod
    def suit_splitter(cls,hand):
        splitted_hand = defaultdict(list)
        for tile in hand:
            stripped_tile = re.sub(r'\d+', '', tile)
            splitted_hand[stripped_tile].append(tile)
        return splitted_hand


    @classmethod
    def is_tenpai(cls,hand):
        waiting_suits = Rules.suit_counter(hand)
        if len(waiting_suits) > 2:
            return False
        splitted_hand = Rules.suit_splitter(hand)
        for suit in splitted_hand:
            # we don't need to check if waiting suits are finished since they are "waiting"
            if suit not in waiting_suits:
                if suit in Tile.honours and not Rules.is_pon(splitted_hand[suit]):
                    return False
                #else:
                    # TODO
                    # TODO: figure out good way to detect formations like 111123 or 12222
        return True
