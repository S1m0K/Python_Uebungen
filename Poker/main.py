import random
import numpy as np

from PokerMethods import PokerMethods

poker_combination_dic = {
    "Straight flush": 0,
    "Four of a kind": 0,
    "Full house": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a kind": 0,
    "Two pairs": 0,
    "One pair": 0,
    "No Combination": 0
}


if __name__ == '__main__':
    card_cnt = 5
    rounds_played = 1000000
    for i in range(rounds_played):
        one = PokerMethods.draw_hand_and_analyze(card_cnt)
        for g in range(len(one[-1])):
            if one[-1][g] is True:
                keys = list(poker_combination_dic.keys())
                poker_combination_dic[keys[g]] = poker_combination_dic[keys[g]] + 1
        # print(one)

    print(poker_combination_dic)
    for key in poker_combination_dic:
        poker_combination_dic[key] = poker_combination_dic[key] / rounds_played * 100
    print(poker_combination_dic)
