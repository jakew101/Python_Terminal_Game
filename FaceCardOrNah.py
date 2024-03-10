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
    return [deck.pop(deck.index(random.choice(deck))) for i in range(6)]

card_draw = draw_cards()

def first_question():
    first = input("Higher or lower? ").lower()
    if first == "higher" and card_draw[1].val_num >= card_draw[0].val_num:
        return True
    elif first == "lower" and card_draw[1].val_num <= card_draw[0].val_num:
        return True
    return False

def second_question():
    return input("In between or outside? ").lower()

def third_question():
    return input("Red or black? ").lower()

def fourth_question():
    return input("Suit? ").lower()

def final_question():
    return input("Face card or nah? ").lower()

def start():
    print(card_draw)
    if first_question():
        if second_question():
            if third_question():
                if fourth_question():
                    if final_question():
                        print("PASS")
    else:
        print("FAIL")

start()