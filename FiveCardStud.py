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

class Table:
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
    def print_deck(self):
        for x in range(0,len(self.deck)):
            print(self.deck[x].face, self.deck[x].suite, sep='', end=' ')
            if x % 13 == 12:
                print()
        print('\n')
    def print_hands(self):
        for hand in self.hands:
            for card in hand.hand:
                print(card.face, card.suite, sep='', end=' ')
            print()
        print('\n')
        

class Hand:
    def __init__(self):
        self.hand = []
    def deal(self, card):
        self.hand.append(card)


table = Table()
table.print_deck()
table.deal()
table.print_hands()
table.print_deck()



