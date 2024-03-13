# Face Card or Nah?
# Six cards from a full deck of playing cards are drawn. 
# The first card is placed face up in front of the player. 
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

discard_pile = []

def draw_cards():
    draw = [deck.pop(deck.index(random.choice(deck))) for i in range(6)]
    discard_pile.extend(draw)
    return draw


def shuffle_deck():
    for card in deck.copy():
        discard_pile.append(deck.pop(deck.index(card)))
    for card in discard_pile.copy():
        deck.append(discard_pile.pop(discard_pile.index(card)))
    random.shuffle(deck)
    print("Shuffling.........")
    print()
    return deck


def first_question(card_draw):
    print(card_draw[0])
    first_question = input("Higher or lower? (higher/lower) ").lower()
    if first_question == "higher" and card_draw[1].val_num >= card_draw[0].val_num:
        return True
    elif first_question == "lower" and card_draw[1].val_num <= card_draw[0].val_num:
        return True
    return False


def second_question(card_draw):
    print(card_draw[1])
    second_question = input("In between or outside? (in/out) ").lower()
    if card_draw[0].val_num > card_draw[1].val_num:
        range_card = range(card_draw[0].val_num, ((card_draw[1].val_num) - 1), -1)
    else:
        range_card = range(card_draw[0].val_num, ((card_draw[1].val_num) + 1))
    if second_question == "in" and card_draw[2].val_num in range_card:
        return True
    elif second_question == "out" and card_draw[2].val_num not in range_card:
        return True
    return False


def third_question(card_draw):
    print(card_draw[2])
    third_question = input("Red or black? (red/black) ").lower()
    if third_question == card_draw[3].color:
        return True
    return False


def fourth_question(card_draw):
    print(card_draw[3])
    fourth_question = input("Suit? (clubs/hearts/diamonds/spades) ").lower()
    if fourth_question == card_draw[4].suit.lower():
        return True
    return False


def final_question(card_draw):
    print(card_draw[4])
    final_question = input("Face card or nah? (facecard/nah) ").lower()
    if final_question == "facecard" and card_draw[5].is_face_card:
        print(card_draw[5])
        return True
    elif final_question == "nah" and not card_draw[5].is_face_card:
        print(card_draw[5])
        return True
    return False


def start():
    if len(deck) == 4:
        shuffle_deck()
    draw_count = 1
    card_draw = draw_cards()
    print(card_draw)
    if first_question(card_draw):
        draw_count += 1
        if second_question(card_draw):
            draw_count += 1
            if third_question(card_draw):
                draw_count += 1
                if fourth_question(card_draw):
                    draw_count += 1
                    if final_question(card_draw):
                        print(figlet_format("Congratulations!", font = "slscript"))
                        replay()
    print("Nope!")
    print(card_draw[draw_count])
    replay()


def replay():
    prompt = input("Play again? (Y/N) ").lower()
    if prompt == "y":
        print()
        print(figlet_format("New game", font = "small"))
        start()
    exit()


start()