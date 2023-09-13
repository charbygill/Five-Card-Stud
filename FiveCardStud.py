import random

#Start by making a card class
class Card:
    def __init__(self, face, suite):
        if face < 11:
            if face == 1:
                self.face = ' A'
            else:
                if face == 10:
                    self.face = face
                else:
                    self.face = ' ' + str(face)
        if face == 11:
            self.face = ' J'
        if face == 12:
            self.face = ' Q'
        if face == 13:
            self.face = ' K'
        if suite == 1:
            self.suite = 'D'
        if suite == 2:
            self.suite = 'C'
        if suite == 3:
            self.suite = 'H'
        if suite == 4:
            self.suite = 'S'
        self.face_int = face
        self.suite_int = suite
        self.flagged = False
        self.high_card = False
    def flag(self):
        self.flagged = True
    def set_high_card(self):
        self.high_card = True

class Poker_Table:
    def __init__(self):
        self.hands = []
        self.deck = []
        for x in range (1,5):
            for y in range(1,14):
                self.deck.append(Card(y,x))
        random.shuffle(self.deck)
    def deal(self):
        for x in range(0,5):
            for y in range(0,6):
                if x == 0:
                    self.hands.append(Hand())
                self.hands[y].deal(self.deck[0])
                self.deck.pop(0)
    def print_deck(self, col = 52):
        for x in range(0,len(self.deck)):
            print(self.deck[x].face, self.deck[x].suite, sep='', end=' ')
            if x % col == col - 1:
                print()
        print('\n')
    def print_hands(self):
        for hand in self.hands:
            for card in hand.hand:
                print(card.face, card.suite, sep='', end=' ')
            print()
        print('\n')
    def rank_hands(self):
        hands_clone = self.hands
        for hand in hands_clone:
            sorted_hand = hand.sort()
        
        

class Hand:
    def __init__(self):
        self.hand = []
    def deal(self, card):
        self.hand.append(card)
    def sort(self):
        sorted_hand = self.hand
        n = len(sorted_hand)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if sorted_hand[j].face_int > sorted_hand[j + 1].face_int:
                    swapped = True
                    sorted_hand[j], sorted_hand[j + 1] = sorted_hand[j + 1], sorted_hand[j]
            if not swapped:
                return sorted_hand
    def rank(self):


table = Poker_Table()
table.print_deck(13)
table.deal()
table.print_hands()
table.print_deck()



