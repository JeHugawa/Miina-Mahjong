import unittest
from collections import defaultdict

from rules import Rules
from tile import Tile


class TestRules(unittest.TestCase):

    def test_is_pon_returns_true(self):
        result = Rules.is_pon(["m1","m1","m1"])
        self.assertEqual(result, True)

    def test_is_pon_returns_false(self):
        result = Rules.is_pon(["m1","m2","m3"])
        self.assertEqual(result, False)

    def test_is_chi_returns_true(self):
        result = Rules.is_chi(["m1","m2","m3"])
        self.assertEqual(result, True)

    def test_is_chi_returns_false(self):
        result = Rules.is_chi(["m1","m2","m2"])
        self.assertEqual(result, False)

    def test_is_chi_returns_false_2(self):
        result = Rules.is_chi(["s1","s2","s4"])

    def test_suit_counter(self):
        hand = ["north","north", "south","south","south", "p1","p2","p3","p4","p5","s1","s2","s3"]
        result = Rules.suit_counter(hand)
        self.assertEqual(result, ["north","p"])

    def test_suit_splitter(self):
        example_splitted_hand = defaultdict(list)
        example_splitted_hand["north"] = ["north","north"]
        example_splitted_hand["south"] = ["south","south"]
        example_splitted_hand["s"] = ["s1","s2","s3"]
        example_splitted_hand["m"] = ["m5","m6","m8"]
        example_splitted_hand["p"] = ["p7","p7","p7"]
        hand = ["north","north","south","south","s1","s2","s3","p7","p7","p7","m5","m6","m8"]
        self.assertEqual(Rules.suit_splitter(hand), example_splitted_hand)

    #hardest scenario to detect because there is pon between chi
    def test_check_suit_for_completeness_when_true(self):
        suit = ["s1","s2","s2","s2","s2","s3"]
        result = Rules.check_suit_for_completeness(suit)
        self.assertEqual(result, True)

    def test_check_suit_for_completeness_when_true_wih_pons(self):
        suit = ["p1","p1","p1","p7","p7","p7"]
        result = Rules.check_suit_for_completeness(suit)
        self.assertEqual(result, True)

    def test_check_suit_for_completeness_fail_1(self):
        suit = ["s1","s2","s2","s2","s3","s4"]
        result = Rules.check_suit_for_completeness(suit)
        self.assertEqual(result, False)

    def test_check_suit_for_completeness_fail_2(self):
        suit = ["m1","m2","m4","m5","m6","m7"]
        result = Rules.check_suit_for_completeness(suit)
        self.assertEqual(result, False)

    def test_check_suit_for_completeness_fail_3(self):
        suit = ["p1","p1","p1","p1","p2","p4"]
        result = Rules.check_suit_for_completeness(suit)
        self.assertEqual(result, False)

    def test_is_tenpai_true(self):
        hand = ["s1","s2","s3","s4","s4","s4","north","north","north","p1","p1","white","white"]
        result = Rules.is_tenpai(hand)
        self.assertEqual(result, True)

    def test_is_tenpai_false_hand_too_short(self):
        hand = ["s1","s2","s3","s4","s4","s4","north","north","north","p1","p1"]
        result = Rules.is_tenpai(hand)
        self.assertEqual(result, False)

    def test_is_tenpai_false_unvalid_pon(self):
        hand = ["s1","s2","s3","s4","s4","s5","north","north","north","p1","p1","white","white"]
        result = Rules.is_tenpai(hand)
        self.assertEqual(result, False)

    def test_check_winning_tiles(self):
        example_waiting_suits = defaultdict(list)
        example_waiting_suits["s"] = ["s1","s3"]
        self.assertEqual(Rules.check_winning_tiles(example_waiting_suits), ["s2"])

    def test_check_winning_tiles_with_winds(self):
        example_waiting_suits = defaultdict(list)
        example_waiting_suits["north"] = ["north"]
        self.assertEqual(Rules.check_winning_tiles(example_waiting_suits), ["north"])

    def test_check_winning_tiles_with_dragons(self):
        example_waiting_suits = defaultdict(list)
        example_waiting_suits["white"] = ["white", "white"]
        example_waiting_suits["green"] = ["green", "green"]
        self.assertEqual(Rules.check_winning_tiles(example_waiting_suits), ["white","green"])

    def test_return_winning_tiles(self):
        hand = ["s1","s2","s3","s4","s4","s4","north","north","north","p1","p1","white","white"]
        self.assertEqual(Rules.return_winning_tiles(hand), ["p1","white"])

    def test_suit_counter(self):
        hand = ["s1","s2","s3","s4","s4","s4","north","north","north","p1","p1","white","white"]
        self.assertEqual(Rules.suit_counter(hand), ["p","white"])
