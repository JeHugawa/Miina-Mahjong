import re
from collections import defaultdict
import copy

from tile import Tile
class Rules:

    @classmethod
    def is_pon(cls,selection):
        """Tarkistaa onko annettu setti pon (3 samaa)
        Args:
            selection: lista jossa on 3 tiiltä
        """
        if selection[0] == selection[1] == selection[2]:
            return True
        return False

    @classmethod
    def is_chi(cls,selection):
        """tarkistaa onko annettu setti chi (kolmen suora)
        Args:
            selection: lista jossa on 3 tiiltä
        """
        selection = sorted(selection)
        if selection[0] < selection[1] < selection[2]:
            if (int(re.sub(r'\D', '', selection[0])) ==
               (int(re.sub(r'\D','',selection[1]))-1)):
                if (int(re.sub(r'\D', '', selection[1])) ==
                   (int(re.sub(r'\D', '', selection[2]))-1)):
                    return True
        return False

    @classmethod
    def suit_counter(cls,hand):
        """Laskee montako eri maata on odottamassa tiiltä. Maa odottaa tiiltä jos siinä ei ole 3 jaollinen.
        Args:
            hand: pelaajan käsi
        Returns:
            Palauttaa listan missä on kaikki eri maat mitä pelaaja odottaa
        """
        amount = {}
        for tile in hand:
            tile = re.sub(r'\d+', '', tile)
            amount[tile] = amount.setdefault(tile,0) +1
        waiting_suits = []
        for suit, tile_count in amount.items():
            if tile_count % 3 != 0:
                waiting_suits.append(suit)
        return waiting_suits

    @classmethod
    def check_winning_tiles(cls,waiting_suits):
        """Palauttaa mahdolliset voittotiilet
        Args:
            waiting suits: dict missä on maa ja sen tiilet
        Returns:
            tiilet joilla pelaaja voi voittaa.
        """
        winning_tiles = []
        for suit in waiting_suits:
            if suit in Tile.honours:
                winning_tiles.append(suit)
            else:
                #disabling pylint here, using exec isnt style issue per say
                exec("suit_tiles = Tile." + suit,globals()) #pylint: disable=exec-used
                for tile in suit_tiles: #pylint: disable=undefined-variable
                    tiles_to_check = waiting_suits[suit]
                    if Rules.check_suit_for_completeness(tiles_to_check + [tile]):
                        winning_tiles.append(tile)
        return winning_tiles


    @staticmethod
    def return_winning_tiles(hand):
        """wrapperifunktio UIta varten, joka palauttaa voittotiilet.
        Args:
            pelaajan kädessä olevat tiilet
        Returns:
            tiilet joilla pelaaja voi voittaa.
        """
        waiting_suits = Rules.suit_counter(hand)
        splitted_hand = Rules.suit_splitter(hand)
        waiting_hand = copy.deepcopy(splitted_hand)
        for suit in splitted_hand:
            if suit not in waiting_suits:
                del waiting_hand[suit]
        return Rules.check_winning_tiles(waiting_hand)

    @classmethod
    def suit_splitter(cls,hand):
        """Funktio jakaa käden maihin.
        Args:
            Pelaajan käsi
        Returns:
            Dictionary, missä avaimena on maa ja avaimen takana on maassa olevat tiilet.
        """
        splitted_hand = defaultdict(list)
        for tile in hand:
            stripped_tile = re.sub(r'\d+', '', tile)
            splitted_hand[stripped_tile].append(tile)
        return splitted_hand

    @staticmethod
    def is_tenpai(hand):
        """tarkistaa onko käsi yhden päässä voitossa (tenpai)
        Args:
            hand: pelaajan käsi
        Returns:
            Palauttaa True jos pelaajan käsi on tenpai, palauttaa False jos ei ole
        """
        if len(hand) != 13:
            return False
        waiting_suits = Rules.suit_counter(hand)
        if len(waiting_suits) > 2:
            return False
        splitted_hand = Rules.suit_splitter(hand)
        for suit in splitted_hand:
            # we don't need to check if waiting suits are finished since they are "waiting"
            if suit not in waiting_suits:
                if suit in Tile.honours and not Rules.is_pon(splitted_hand[suit]):
                    return False
                if not Rules.check_suit_for_completeness(splitted_hand[suit]):
                    return False
        waiting_suit_tiles = defaultdict(list)
        for suit in waiting_suits:
            for tile in splitted_hand[suit]:
                waiting_suit_tiles[suit].append(tile)
        return Rules.check_waiting_suits(waiting_suit_tiles)

    @classmethod
    def check_suit_for_completeness(cls, suit):
        """Tarkistaa onko annettu maa laillinen
        Args:
            suit: lista, missä on annetun maan tiilet
        Returns:
            palauttaa False jos maa ei ole laillinen, True jos on
        """
        if not suit:
            return True
        first_three = [suit[0], suit[1], suit[2]]
        if Rules.is_pon(first_three):
            return Rules.check_suit_for_completeness(suit[3:])
        first_three = [suit[0]]
        #tiles are sorted, so next tile that is not the same as current tile will be
        #next in sequence
        for tile in suit[1:]:
            if tile != first_three[-1]:
                first_three.append(tile)
            if len(first_three) == 3:
                break
        try:
            if Rules.is_chi(first_three):
                chiless_suit = suit
                for tile in first_three:
                    chiless_suit.remove(tile)
                return Rules.check_suit_for_completeness(chiless_suit)
        except IndexError:
            return False
        return False

    @classmethod
    def check_waiting_suits(cls, waiting_suits):
        """Funktio tarkistaa sellaisen annetut maat, mikä odottaa tiiliä
        Args:
            waiting_suits: dictionary missä on maat ja niiden tiilet
        returns:
            palauttaa True jos laillisia, False jos ei ole
        """
        keys = []
        for key in waiting_suits:
            keys.append(key)
        if len(waiting_suits) == 1:
            only_suit = waiting_suits[keys[0]]
            if len(only_suit) == 1:
                return True
            if len(only_suit) == 2:
                if only_suit[0] < only_suit[1]:
                    return True
                if (int(re.sub(r'\D', '', only_suit[0])) < (int(re.sub(r'\D', '', only_suit[0]))+1)
                    <  int(re.sub(r'\D', '', only_suit[1]))):
                    return True
            if len(only_suit) == 4:
                if only_suit[0] == [1]:
                    if only_suit[2] == only_suit[3]:
                        return False
            return False
        if len(waiting_suits[keys[0]]) == 2 and len(waiting_suits[keys[1]]) == 2:
            for suit in waiting_suits:
                if not waiting_suits[suit][0] == waiting_suits[suit][1]:
                    if not waiting_suits[suit][0] < waiting_suits[suit][1]:
                        if not (int(re.sub(r'\D', '', waiting_suits[suit][0]))
                                 < (int(re.sub(r'\D', '', waiting_suits[suit][0]))+1)
                                 <  int(re.sub(r'\D', '', waiting_suits[suit][1]))):
                            return False
            return True
        return True
