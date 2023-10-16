import random

import numpy as np


def draw_random(arr, cnt):
    for j in range(cnt):
        r = random.randint(0, 51 - j)
        arr[len(arr) - 1 - j], arr[r] = arr[r], arr[len(arr) - 1 - j]
    print(arr)
    return arr


def translate_to_hand(ca):
    arr = []
    for c in ca:
        color = c // 13  # 0 -> Hearts; 1 -> Diamonds; 2 -> Spades; 3 -> Clubs
        number = c % 13  # 0 --> Ace; 12 --> King
        arr.append([color, number])
    return arr


def analyze_hand(h):
    colors = []
    numbers = []

    for j in range(len(h) - 1):
        numbers.append(h[j][1])
        colors.append(h[j][0])

    numbers = sorted(numbers)

    cnt_pairs = 0
    for j in range(13):
        # TWO PAIR CHECK
        if (numbers.count(j + 1) >= 2 and h[-1][7]) or (h[-1][1] is True):
            h[-1][6] = True
            cnt_pairs = cnt_pairs + 1

        # PAIR CHECK
        if numbers.count(j + 1) >= 2:
            h[-1][7] = True

        # THREE OF A KIND CHECK
        if numbers.count(j + 1) >= 3:
            h[-1][5] = True

        # FOUR OF A KIND CHECK
        if numbers.count(j + 1) == 4:
            h[-1][1] = True

        # FULL HOUSE CHECK
        if len(numbers) == 5:
            if (not h[-1][1]) and h[-1][5] and h[-1][7] and (cnt_pairs == 1):
                h[-1][2] = True
        else:
            if h[-1][5] and h[-1][7]:
                h[-1][2] = True

    # FLUSH CHECK
    for j in range(4):
        if colors.count(j + 1) >= 5:
            h[-1][3] = True

    # STRAIGHT CHECK
    numbers = np.unique(numbers)
    cnt = 0
    for j in range(len(numbers) - 1):
        if numbers[j] == (numbers[j + 1] - 1):
            cnt = cnt + 1
        else:
            cnt = 0

        if cnt >= 4:
            h[-1][4] = True

    # STRAIGHT FLUSH CHECK
    if h[-1][4] and h[-1][3]:
        h[-1][0] = True

    # NO COMBINATION CHECK
    com_cnt = 0
    for j in range(len(h[-1]) - 1):
        if h[-1][j] is True:
            com_cnt = com_cnt + 1
    if com_cnt == 0:
        h[-1][8] = True

    return h


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


def draw_hand_and_analyze(cnt):
    com_bool = [[False, False, False, False, False, False, False, False, False]]
    cards = np.arange(0, 13 * 4, 1)
    cards = draw_random(np.copy(cards), cnt)
    hand = translate_to_hand(cards[-cnt:])
    hand = hand + com_bool.copy()
    analyzed_hand = analyze_hand(hand.copy())
    return analyzed_hand


if __name__ == '__main__':
    card_cnt = 5
    rounds_played = 10
    for i in range(rounds_played):
        one = draw_hand_and_analyze(card_cnt)
        for g in range(len(one[-1])):
            if one[-1][g] is True:
                keys = list(poker_combination_dic.keys())
                poker_combination_dic[keys[g]] = poker_combination_dic[keys[g]] + 1
        # print(one)

    print(poker_combination_dic)
    for key in poker_combination_dic:
        poker_combination_dic[key] = poker_combination_dic[key] / rounds_played * 100
    print(poker_combination_dic)
