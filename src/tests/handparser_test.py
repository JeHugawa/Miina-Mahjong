import unittest
from handparser import HandParser, PlayingHand
from tile import Tile


class TestHandParser(unittest.TestCase):
    
    def test_parse_hand_returns_right_value(self):
        selections = ["m1","m2","m3","p1","p2","p3","s1","s2","s3","north","north","south","south"]
        wall = ['m2', 'west', 'm3', 'east', 'm2', 'p8', 'p4', 's9', 'p7', 'm3', 'm9', 'm3', 's6', 'green', 'm1', 'north', 's3', 's2', 'red', 'p2', 'p3', 'm4', 'p1', 'p2', 'south', 'p6', 's1', 'p4', 'green', 'south', 'm3', 'p5', 'm1', 'north']
        test_hand = HandParser.parse_hand(selections, wall)
        wall_without_hand = wall
        for tile in selections:
            wall_without_hand.remove(tile)
        self.assertEqual(test_hand, PlayingHand(selections,[],wall_without_hand))

    def test_parse_hand_Value_Error(self):
        wall = ['m2', 'west', 'm3', 'east', 'm2', 'p8', 'p4', 's9', 'p7', 'm3', 'm9', 'm3', 's6', 'green', 'm1', 'north', 's3', 's2', 'red', 'p2', 'p3', 'm4', 'p1', 'p2', 'south', 'p6', 's1', 'p4', 'green', 'south', 'm3', 'p5', 'm1', 'north']
        test_hand = HandParser.parse_hand(["p1","white"],wall)
        self.assertEqual(test_hand, False)

    def test_parse_hand_too_short_hand(self):
        selections = ["m2","m3","p1","p2","p3","s1","s2","s3","north","north","south","south"]
        wall = ['m2', 'west', 'm3', 'east', 'm2', 'p8', 'p4', 's9', 'p7', 'm3', 'm9', 'm3', 's6', 'green', 'm1', 'north', 's3', 's2', 'red', 'p2', 'p3', 'm4', 'p1', 'p2', 'south', 'p6', 's1', 'p4', 'green', 'south', 'm3', 'p5', 'm1', 'north']
        test_hand = HandParser.parse_hand(selections, wall)
        wall_without_hand = wall
        for tile in selections:
            wall_without_hand.remove(tile)
        self.assertEqual(test_hand, False)

    def test_discard(self):
        selections = ["m1","m2","m3","p1","p2","p3","s1","s2","s3","north","north","south","south"]
        wall = ["m1","m2","m3","p1","p2","p3","s1","s2","s3","north","north","south","south","west","west"]
        test_hand = HandParser.parse_hand(selections, wall)
        test_hand.discard("west")
        self.assertEqual(test_hand, PlayingHand(selections,["west"],["west"]))
