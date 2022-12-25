import copy

class PlayingHand:
    """Luokka, jolla hallitaan pelaajan käden tietoja.

    Attributes:
        hand: pelaajan valitsemat tiilet.
        discards: pelaajan poisheittämät tiilet
        tilepool: tiilet mistä pelaaja voi heittää tiiliä pois
    """
    def __init__(self, hand: list, discards: list, tilepool: list):
        """Luokan konstruktori, joka luo uuden pelaajan käden.

        Args:
            hand: pelaajan valitsemat tiilet.
            discards: pelaajan poisheittämät tiilet
            tilepool: tiilet mistä pelaaja voi heittää tiiliä pois
        """
        self.hand = hand
        self.discards = discards
        self.tilepool = tilepool

    def __eq__(self, other):
        """Luokan vertailija, jolla voi verrata kahta luokan instanssia keskenään.

        Returns:
            Totuusarvo joka kertoo onko kaksi luokan oliota samoja
        """
        self_values = (self.hand, self.discards, self.tilepool)
        other_values =  (other.hand, other.discards, other.tilepool)
        return self_values == other_values

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
        """Poistaa tiilen pelaajan kädestä ja siirtää sen poisheitettyihin.

        Args:
            discard: tiili minkä pelaaja haluaa heittää pois
        """
        self.tilepool.remove(discard)
        self.discards.append(discard)


class HandParser:
    """apuluokka, millä muodostetaan pelaajan käsiä
    """
    @staticmethod
    def parse_hand(selections: list, tiles):
        """yritetään muodostaa pelaajan käsi annetuista tiilistä

        Args:
            selections: pelaajan valitsemat tiilet
            tiles: tiilet, mistä pelaaja voi valita pelin alussa

        Returns:
            yrittää palauttaa laillisen PlayingHand luokan olion, palauttaa False jos epäonnistuu
        """
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
