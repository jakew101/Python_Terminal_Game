# Face Card or Nah?
# A card from a full deck of playing cards is placed face up in front of the player. 
# The player guesses if the next card is higher or lower. 
# If correct, the player guesses if the next card is in between or outside of the two face up cards. 
# If correct, the player guesses if the next card is red or black. 
# If correct, the player guesses the suit of the next card. 
# If correct, the player answers the final question to win a point: face card or nah?
# If any of these decisions are not correct, the next player goes (rotational)


import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{value} of {suit}".format(value=self.value, suit=self.suit)

suits = ["spades", "clubs", "hearts", "diamonds"]

values = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]

deck = [Card(suit, value) for suit in suits for value in values]
print(deck)