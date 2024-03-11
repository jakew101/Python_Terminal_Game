# Face Card or Nah?
# A card from a full deck of playing cards is placed face up in front of the player. 
# The player guesses if the next card is higher or lower. 
# If correct, the player guesses if the next card is in between or outside of the two face up cards. 
# If correct, the player guesses if the next card is red or black. 
# If correct, the player guesses the suit of the next card. 
# If correct, the player answers the final question: face card or nah?
# If any of these decisions are not correct or the player correctly guesses each card attribute correctly, the next player goes. 

from pyfiglet import figlet_format
import random

print(figlet_format("Face Card or Nah?", font = "bulbhead"))

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
    draw = [deck.pop(deck.index(random.choice(deck))) for i in range(6)]
    deck.append(draw)
    return draw

card_draw = draw_cards()


def first_question(card_draw=card_draw):
    first_question = input("Higher or lower? ").lower()
    if first_question == "higher" and card_draw[1].val_num >= card_draw[0].val_num:
        return True
    elif first_question == "lower" and card_draw[1].val_num <= card_draw[0].val_num:
        return True
    return False


def second_question(card_draw=card_draw):
    second_question = input("Between or outside? ").lower()
    if card_draw[0].val_num > card_draw[1].val_num:
        range_card = range(card_draw[0].val_num, ((card_draw[1].val_num) - 1), -1)
    else:
        range_card = range(card_draw[0].val_num, ((card_draw[1].val_num) + 1))
    if second_question == "between" and card_draw[2].val_num in range_card:
        return True
    elif second_question == "outside" and card_draw[2].val_num not in range_card:
        return True
    return False


def third_question(card_draw=card_draw):
    third_question = input("Red or black? ").lower()
    if third_question == card_draw[3].color:
        return True
    return False


def fourth_question(card_draw=card_draw):
    fourth_question = input("Suit? ").lower()
    if fourth_question == card_draw[4].suit.lower():
        return True
    return False


def final_question(card_draw=card_draw):
    final_question = input("Face card or nah? ").lower()
    if final_question == "face card" and card_draw[5].is_face_card:
        return True
    elif final_question == "nah" and not card_draw[5].is_face_card:
        return True
    return False


def start():
    card_draw = draw_cards()
    draw_count = 0
    print(card_draw)
    print(card_draw[0])
    draw_count += 1
    if first_question(card_draw):
        print(card_draw[1])
        draw_count += 1
        if second_question(card_draw):
            draw_count += 1
            print(card_draw[2])
            if third_question(card_draw):
                draw_count += 1
                print(card_draw[3])
                if fourth_question(card_draw):
                    draw_count += 1
                    print(card_draw[4])
                    if final_question(card_draw):
                        print(card_draw[5])
                        print(figlet_format("Congratulations!", font = "slscript"))
                        replay()
    print("Nope!")
    print(card_draw[draw_count])
    replay()


def replay():
    prompt = input("Play again?(Y/N) ").lower()
    if prompt == "y":
        print()
        print(figlet_format("New game", font = "small"))
        start()
    exit()



start()