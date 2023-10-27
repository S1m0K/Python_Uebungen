import unittest
import copy
from PokerMethods import PokerMethods


class PokerTests(unittest.TestCase):
    # "Straight flush :0, Four of a kind :1, Full house :2, Flush :3, Straight :4, Three of a kind :5,
    # Two pair :6, One pair :7, High card :8"
    com_bool = [[False, False, False, False, False, False, False, False, False]]

    def test_straight_flush(self):
        hand = [[2, 4], [2, 5], [2, 2], [2, 3], [2, 6]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(True, ah[-1][0])
                and self.assertEqual(True, ah[-1][1])
                and self.assertEqual(True, ah[-1][2])
                and self.assertEqual(False, ah[-1][3])
                and self.assertEqual(False, ah[-1][4])
                and self.assertEqual(False, ah[-1][5])
                and self.assertEqual(False, ah[-1][6])
                and self.assertEqual(False, ah[-1][7])
                and self.assertEqual(False, ah[-1][8]))

    def test_four_of_a_kind(self):
        hand = [[1, 8], [3, 8], [2, 8], [2, 9], [0, 8]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(False, ah[-1][0])
                and self.assertEqual(True, ah[-1][1])
                and self.assertEqual(False, ah[-1][2])
                and self.assertEqual(False, ah[-1][3])
                and self.assertEqual(False, ah[-1][4])
                and self.assertEqual(True, ah[-1][5])
                and self.assertEqual(True, ah[-1][6])
                and self.assertEqual(True, ah[-1][7])
                and self.assertEqual(False, ah[-1][8]))

    def test_full_house(self):
        hand = [[1, 11], [1, 9], [3, 11], [0, 11], [2, 9]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(False, ah[-1][0])
                and self.assertEqual(False, ah[-1][1])
                and self.assertEqual(True, ah[-1][2])
                and self.assertEqual(False, ah[-1][3])
                and self.assertEqual(False, ah[-1][4])
                and self.assertEqual(True, ah[-1][5])
                and self.assertEqual(True, ah[-1][6])
                and self.assertEqual(True, ah[-1][7])
                and self.assertEqual(False, ah[-1][8]))

    def test_flush(self):
        hand = [[1, 8], [1, 11], [1, 0], [1, 12], [1, 2]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(False, ah[-1][0])
                and self.assertEqual(False, ah[-1][1])
                and self.assertEqual(False, ah[-1][2])
                and self.assertEqual(True, ah[-1][3])
                and self.assertEqual(False, ah[-1][4])
                and self.assertEqual(False, ah[-1][5])
                and self.assertEqual(False, ah[-1][6])
                and self.assertEqual(False, ah[-1][7])
                and self.assertEqual(False, ah[-1][8]))

    def test_straight(self):
        hand = [[2, 8], [3, 11], [1, 9], [3, 7], [3, 10]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(False, ah[-1][0])
                and self.assertEqual(False, ah[-1][1])
                and self.assertEqual(False, ah[-1][2])
                and self.assertEqual(False, ah[-1][3])
                and self.assertEqual(True, ah[-1][4])
                and self.assertEqual(False, ah[-1][5])
                and self.assertEqual(False, ah[-1][6])
                and self.assertEqual(False, ah[-1][7])
                and self.assertEqual(False, ah[-1][8]))

    def test_three_of_a_kind(self):
        hand = [[2, 0], [1, 0], [1, 9], [3, 0], [3, 10]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(False, ah[-1][0])
                and self.assertEqual(False, ah[-1][1])
                and self.assertEqual(False, ah[-1][2])
                and self.assertEqual(False, ah[-1][3])
                and self.assertEqual(False, ah[-1][4])
                and self.assertEqual(True, ah[-1][5])
                and self.assertEqual(False, ah[-1][6])
                and self.assertEqual(True, ah[-1][7])
                and self.assertEqual(False, ah[-1][8]))

    def test_double_pair(self):
        hand = [[2, 6], [1, 6], [1, 9], [3, 9], [3, 10]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(False, ah[-1][0])
                and self.assertEqual(False, ah[-1][1])
                and self.assertEqual(False, ah[-1][2])
                and self.assertEqual(False, ah[-1][3])
                and self.assertEqual(False, ah[-1][4])
                and self.assertEqual(False, ah[-1][5])
                and self.assertEqual(True, ah[-1][6])
                and self.assertEqual(True, ah[-1][7])
                and self.assertEqual(False, ah[-1][8]))

    def test_pair(self):
        hand = [[2, 0], [1, 7], [1, 9], [3, 7], [3, 10]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(False, ah[-1][0])
                and self.assertEqual(False, ah[-1][1])
                and self.assertEqual(False, ah[-1][2])
                and self.assertEqual(False, ah[-1][3])
                and self.assertEqual(False, ah[-1][4])
                and self.assertEqual(False, ah[-1][5])
                and self.assertEqual(False, ah[-1][6])
                and self.assertEqual(True, ah[-1][7])
                and self.assertEqual(False, ah[-1][8]))

    def test_no_comb(self):
        hand = [[2, 0], [1, 2], [1, 9], [3, 12], [3, 10]]
        hand = hand + copy.deepcopy(self.com_bool)
        ah = PokerMethods.analyze_hand(hand.copy())
        return (self.assertEqual(False, ah[-1][0])
                and self.assertEqual(False, ah[-1][1])
                and self.assertEqual(False, ah[-1][2])
                and self.assertEqual(False, ah[-1][3])
                and self.assertEqual(False, ah[-1][4])
                and self.assertEqual(False, ah[-1][5])
                and self.assertEqual(False, ah[-1][6])
                and self.assertEqual(False, ah[-1][7])
                and self.assertEqual(True, ah[-1][8]))


if __name__ == '__main__':
    unittest.main()
