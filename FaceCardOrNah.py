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
        self.color = "red" if self.suit == "Hearts" or self.suit == "Diamonds" else "black"
        self.is_face_card = True if self.val_num in range(11, 14) else False

    def __repr__(self):
        return "{value} of {suit}".format(value=self.value, suit=self.suit)

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13}

deck = [Card(suit, value) for suit in suits for value in values]

def draw_cards():
    return [deck.pop(deck.index(random.choice(deck))) for i in range(6)]

card_draw = draw_cards()

def first_question():
    first_question = input("Higher or lower? ").lower()
    if first_question == "higher" and card_draw[1].val_num >= card_draw[0].val_num:
        return True
    elif first_question == "lower" and card_draw[1].val_num <= card_draw[0].val_num:
        return True
    return False

# Revisit logic if first card is greater than the second card
def second_question():
    second_question = input("In between or outside? ").lower()
    if second_question == "in between" and card_draw[2].val_num in range(card_draw[0].val_num, (card_draw[1].val_num)):
        return True
    elif second_question == "outside" and card_draw[2].val_num not in range(card_draw[0].val_num, (card_draw[1].val_num)):
        return True
    return False

def third_question():
    third_question = input("Red or black? ").lower()
    if third_question == card_draw[3].color:
        return True
    return False

def fourth_question():
    fourth_question = input("Suit? ").lower()
    if fourth_question == card_draw[4].suit.lower():
        return True
    return False

def final_question():
    final_question = input("Face card or nah? ").lower()
    if final_question == "face card" and card_draw[5].is_face_card:
        return True
    elif final_question == "nah" and not card_draw[5].is_face_card:
        return True
    return False

def start():
    # printing card_draw for testing - remove later
    print(card_draw)
    print(card_draw[0])
    if first_question():
        print(card_draw[1])
        if second_question():
            print(card_draw[2])
            if third_question():
                print(card_draw[3])
                if fourth_question():
                    print(card_draw[4])
                    if final_question():
                        print(card_draw[5])
                        print("PASS")
    else:
        print("FAIL")

start()

# print(card_draw)
# for i in range(card_draw[0].val_num, card_draw[1].val_num):
#     print(i)