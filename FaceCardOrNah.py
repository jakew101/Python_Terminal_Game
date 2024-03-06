# Face Card or Nah?
# A card from a full deck of playing cards is placed face up in front of the player. 
# The player guesses if the next card is higher or lower. 
# If correct, the player guesses if the next card is in between or outside of the two face up cards. 
# If correct, the player guesses if the next card is red or black. 
# If correct, the player guesses the suit of the next card. 
# If correct, the player answers the final question to win a point: face card or nah?
# If any of these decisions are not correct, the next player goes (rotational).


import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.val_num = values[value]

    def __repr__(self):
        return "{value} of {suit}".format(value=self.value, suit=self.suit)

suits = ["spades", "clubs", "hearts", "diamonds"]

values = {"ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "jack": 11, "queen": 12, "king": 13}

deck = [Card(suit, value) for suit in suits for value in values]


def draw_cards():
    card_test = [deck.pop(deck.index(random.choice(deck))) for i in range(5)]
    turn_one = input("Higher or lower? ").lower()
    if turn_one == "higher":
        if card_test[0].val_num > 0:
            print("PASS")

draw_cards()