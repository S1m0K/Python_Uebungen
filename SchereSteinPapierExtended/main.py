import random

from HandSign import HandSign

scissors = HandSign("Scissors", 0)
paper = HandSign("Paper", 1)
rock = HandSign("Rock", 2)
lizard = HandSign("Lizard", 3)
spock = HandSign("Spock", 4)

possibilities = [scissors, paper, rock, lizard, spock]
user_in = input("enter r(rock), p(paper), l(lizard), s(scissors) or sp(spock):")
comp_hand = possibilities[random.randint(0, 4)]
user_hand = None

if len(user_in) == 2:
    user_hand = possibilities[4]

for possibility in possibilities:
    if possibility.name.startswith(user_in.upper()):
        user_hand = possibility
        break

print("PC choice: " + comp_hand.name)
print("your choice: " + user_hand.name)
if user_hand.play(comp_hand) == 1:
    print("WIN")
elif user_hand.play(comp_hand) == 0:
    print("DRAW")
else:
    print("LOSE")
