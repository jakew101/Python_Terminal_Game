# Face Card or Nah?
# A card from a full deck of playing cards is placed face up in front of the player. 
# The player guesses if the next card is higher or lower. 
# If correct, the player guesses if the next card is in between or outside of the two face up cards. 
# If correct, the player guesses if the next card is red or black. 
# If correct, the player guesses the suit of the next card. 
# If correct, the player answers the final question: face card or nah?
# If any of these decisions are not correct, the next player goes (rotational).

from pyfiglet import figlet_format
import random

print(figlet_format("Face Card or Nah?", font = "standard"))

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.val_num = values[self.value]

    def __repr__(self):
        return "{value} of {suit}".format(value=self.value, suit=self.suit)

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13}

deck = [Card(suit, value) for suit in suits for value in values]


def draw_cards():
    card_test = [deck.pop(deck.index(random.choice(deck))) for i in range(5)]
    print(card_test[0])
    turn_one = input("Higher or lower? ").lower()
    print(card_test[1])
    if turn_one == "higher":
        if card_test[1].val_num > card_test[0].val_num:
            turn_two = input("Outside or in between? ").lower()
    else:
        print("Nope!")

def draw():
    answer = input("Play? ").lower()
    if answer == "yes":
        draw_cards()
    else:
        print("Okay...")

draw()