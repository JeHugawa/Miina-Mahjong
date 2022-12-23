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

    #check how many suits are waiting
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

    @staticmethod
    def is_tenpai(hand):
        waiting_suits = Rules.suit_counter(hand)
        if len(waiting_suits) > 2:
            return False
        splitted_hand = Rules.suit_splitter(hand)
        for suit in splitted_hand:
            # we don't need to check if waiting suits are finished since they are "waiting"
            if suit not in waiting_suits:
                if suit in Tile.honours and not Rules.is_pon(splitted_hand[suit]):
                    return False
                if not Rules.checkSuitForCompleteness(splitted_hand[suit]):
                    return False
        waiting_suit_tiles = defaultdict(list)
        for suit in waiting_suits:
            for tile in splitted_hand[suit]:
                waiting_suit_tiles[suit].append(tile)
        return Rules.checkWaitingSuits(waiting_suit_tiles)

    @classmethod
    def checkSuitForCompleteness(cls, suit):
        if not suit:
            return True
        first_three = [suit[0], suit[1], suit[2]]
        if Rules.is_pon(first_three):
            return Rules.checkSuitForCompleteness(suit[3:])
        first_three = [suit[0]]
        #tiles are sorted, so next tile that is not the same as current tile will be next in sequence
        for tile in suit[1:]:
            if tile != first_three[-1]:
                first_three.append(tile)
            if len(first_three) == 3:
                break
        try:
            if Rules.is_chi(first_three):
                return Rules.checkSuitForCompleteness(suit[3:])
        except IndexError:
            return False
        return False

    @classmethod
    def checkWaitingSuits(cls, waiting_suits):
        keys = []
        for key in waiting_suits:
            keys.append(key)
        if len(waiting_suits) == 1:
            only_suit = waiting_suits[keys[0]]
            if len(only_suit) == 1:
                return True
            elif len(only_suit) == 2:
                if only_suit[0] < only_suit[1]:
                    return True
                elif int(re.sub('\D', '', only_suit[0])) < (int(re.sub('\D', '', only_suit[0]))+1) <  int(re.sub('\D', '', only_suit[1])):
                    return True
            return False
        if len(waiting_suits[keys[0]]) == 2 and len(waiting_suits[keys[1]]) == 2:
            for suit in waiting_suits:
                if not waiting_suits[suit][0] == waiting_suits[suit][1]:
                    if not waiting_suits[suit][0] < waiting_suits[suit][1]:
                        if not int(re.sub('\D', '', waiting_suits[suit][0])) < (int(re.sub('\D', '', waiting_suits[suit][0]))+1) <  int(re.sub('\D', '', waiting_suits[suit][1])):
                            return False
            return True
        # Todo: currently code assumes the waiting suits dont have other components than the waiting tiles, or that the tiles are correct anyway
        return True
