import random

import numpy as np


def draw_random(arr, cnt):
    for j in range(cnt):
        r = random.randint(0, 51 - j)
        arr[len(arr) - 1 - j], arr[r] = arr[r], arr[len(arr) - 1 - j]
    return arr


def translate_to_hand(ca):
    arr = []
    for c in ca:
        color = c // 13  # 0 -> Hearts; 1 -> Diamonds; 2 -> Spades; 3 -> Clubs
        number = c % 13  # 0 --> Ace; 12 --> King
        arr.append([color, number])
    return arr


def sort_hand(ca):
    chaos = False
    while not chaos:
        chaos = True
        for j in range(len(ca) - 1):
            if ca[j][1] > ca[j + 1][1]:
                ca[j][1], ca[j + 1][1] = ca[j + 1][1], ca[j][1]
                chaos = False
    return ca


def analyze_hand(h):
    for j in range(len(h) - 2):  # -1 cause of list 0 to 4 and -1 cause of last is list of booleans
        # FLUSH CHECK
        if (h[j][0] != h[j + 1][0]) and (h[-1][3] is True):
            h[-1][3] = False

        # STRAIGHT CHECK
        if not ((h[j][1] == (h[j + 1][1] + 1)) or (h[j][1] == (h[j + 1][1] - 1))) and (h[-1][4] is True):
            h[-1][4] = False

        # STRAIGHT FLUSH CHECK
        if not (h[-1][4] and h[-1][3]):
            h[-1][0] = False

    numbers = []
    cnt_pairs = 0
    for j in range(len(h) - 1):
        numbers.append(h[j][1])
    for j in range(13):
        if numbers.count(j + 1) >= 2 and h[-1][7]:
            h[-1][6] = True
            cnt_pairs = cnt_pairs + 1
        if numbers.count(j + 1) >= 2:
            h[-1][7] = True
        if numbers.count(j + 1) >= 3:
            h[-1][5] = True
        if numbers.count(j + 1) == 4:
            h[-1][1] = True
        if (not h[-1][1]) and h[-1][5] and h[-1][7] and (cnt_pairs == 1):
            h[-1][2] = True
    return h


poker_combination_dic = {
    "Straight flush": 0,
    "Four of a kind": 0,
    "Full house": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a kind": 0,
    "Two pair": 0,
    "One pair": 0,
    "High card": 0
}


def draw_hand_and_analyze(cnt):
    com_bool = [[True, False, False, True, True, False, False, False, True]]
    cards = np.arange(0, 13 * 4, 1)
    cards = draw_random(np.copy(cards), cnt)
    hand = translate_to_hand(cards[-cnt:])
    sorted_hand = sort_hand(hand.copy())
    hand = sorted_hand + com_bool.copy()
    analyzed_hand = analyze_hand(hand.copy())
    return analyzed_hand


if __name__ == '__main__':
    card_cnt = 5
    rounds_played = 1
    for i in range(rounds_played):
        one = draw_hand_and_analyze(card_cnt)
        for g in range(len(one[-1])):
            if one[-1][g] is True:
                if g == 0:
                    poker_combination_dic["Straight flush"] = poker_combination_dic["Straight flush"] + 1
                elif g == 1:
                    poker_combination_dic["Four of a kind"] = poker_combination_dic["Four of a kind"] + 1
                elif g == 2:
                    poker_combination_dic["Full house"] = poker_combination_dic["Full house"] + 1
                elif g == 3:
                    poker_combination_dic["Flush"] = poker_combination_dic["Flush"] + 1
                elif g == 4:
                    poker_combination_dic["Straight"] = poker_combination_dic["Straight"] + 1
                elif g == 5:
                    poker_combination_dic["Three of a kind"] = poker_combination_dic["Three of a kind"] + 1
                elif g == 6:
                    poker_combination_dic["Two pair"] = poker_combination_dic["Two pair"] + 1
                elif g == 7:
                    poker_combination_dic["One pair"] = poker_combination_dic["One pair"] + 1
                elif g == 8:
                    poker_combination_dic["High card"] = poker_combination_dic["High card"] + 1
        print(one)

    print(poker_combination_dic)
    for key in poker_combination_dic:
        poker_combination_dic[key] = poker_combination_dic[key] / rounds_played * 100
    print(poker_combination_dic)
