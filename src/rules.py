from tile import Tile
import re
from collections import defaultdict

class Rules:
    

    def is_pon(selection):
        if selection[0] == selection[1] == selection[2]:
            return True
        return False
    
    
    def is_chi(selection):
        selection = sorted(selection)
        if selection[0] < selection[1] < selection[2]:
            return True
        return False


    def is_pair(selection):
        if selection[0] == selection[1]:
            return True
        return False


#procedure for finding tenpai hands:
#1. assume the hand is in tenpai
#2. check all suits in hand: only suits which tiles are not divisible by 3 can be waiting a tile
#2.5. there can be max 2 suits waiting: either one waiting for set or pair wait for two different suits.
#3. for the possible waiting suit(s), we will check which tiles are adjanced to the hand. After that, we will check each tile whetever they will complete the hand. If they complete the hand, hand is in Tenpai and we will put the waiting tiles to wait list and return it

    #check how many suits 
    def suit_counter(hand):
        amount = {}
        for tile in hand:
            tile = re.sub(r'\d+', '', tile)
            amount[tile] = amount.setdefault(tile,0) +1
        waiting_suits = []
        for key in amount:
            if amount[key] % 3 != 0:
                waiting_suits.append(key)
        return waiting_suits


    def check_winning_tiles(hand,waiting_suits):
        pass
        # TODO
        #return winning_tiles

    
    #for a valid hand you need 4 sets and a pair
    def check_hand_completeness(hand):
        if len(hand) != 14:
            return False
        # check_winning_tiles-> if in tiles return true


    def suit_splitter(hand):
        splitted_hand = defaultdict(list)
        for tile in hand:
            stripped_tile = re.sub(r'\d+', '', tile)
            splitted_hand[stripped_tile].append(tile)
        return splitted_hand


    def is_tenpai(hand):
        waiting_suits = Rules.suit_counter(hand)
        if len(waiting_suits) > 2:
            return False
        splitted_hand = Rules.suit_splitter(hand)
        for suit in splitted_hand:
            # we don't need to check if waiting suits are finished since they are "waiting"
            if suit not in waiting_suits:
                if suit in Tile.honours:
                    if not Rules.is_pon(splitted_hand[suit]):
                        return False
                else:
                    pass
                    # TODO: figure out good way to detect formations like 111123 or 12222
        return True
