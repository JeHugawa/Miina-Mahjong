import random

class Tile:
    """Tiilimuurin rakentamisesta vastaava luokka.
    luokasta saa myös tarvittaessa tiedon erityyppisistä tiilistä
    """
    @classmethod
    def get_tilewall(cls):
        """Generoi aloitusmuurin ja palauttaa sen

        Returns:
            lista, missä on jokaista tiiltä 4 kappaletta, sattumanvaraisesti sekoitettuna
        """
        suits = Tile.p + Tile.s + Tile.m + Tile.winds + Tile.dragons
        wall = [tile for tile in suits for x in range(4)]
        random.shuffle(wall)
        return wall


    p = ['p1','p2','p3','p4','p5','p6','p7','p8','p9']
    s = ['s1','s2','s3','s4','s5','s6','s7','s8','s9']
    m = ['m1','m2','m3','m4','m5','m6','m7','m8','m9']

    winds = ['east','south','west','north']
    dragons = ['green','red','white']

    terminals = ['p1','p9','s1','s9','m1','m9']
    honours = ['east','south','west','north','green','red','white']
