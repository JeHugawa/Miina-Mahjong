import random
# Refer to docs for rundown of tiles
class Tile:

    def get_tilewall():
        suits = Tile.pin + Tile.sou + Tile.man + Tile.winds + Tile.dragons
        wall = [tile for tile in suits for x in range(4)]
        random.shuffle(wall)
        return wall
    
   
    pin = ['p1','p2','p3','p4','p5','p6','p7','p8','p9']
    sou = ['s1','s2','s3','s4','s5','s6','s7','s8','s9']
    man = ['m1','m2','m3','m4','m5','m6','m7','m8','m9']

    winds = ['east','south','west','north']
    dragons = ['green','red','white'] 
