import random

#Start by making a card class
class Card:
    def __init__(self, face, suite):
        if face < 11:
            if face == 1:
                self.face = 'A'
            else:
                self.face = face
        if face == 11:
            self.face = 'J'
        if face == 12:
            self.face = 'Q'
        if face == 13:
            self.face = 'K'
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

class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
    def deal(self, card):
        self.hand.append(card)
    def value(self, value):
        self.value = value;

deck = []
for x in range (1,5):
    for y in range(1,14):
        deck.append(Card(y,x))
        
random.shuffle(deck)

for x in range(0,52):
    print(deck[x].face, deck[x].suite, sep='', end=' ')
    if x % 13 == 12:
        print()
        
print('\n')

hands = []

for x in range(0,5):
    for y in range(0,6):
        if x == 0:
            hands.append(Hand())
        hands[y].deal(deck[0])
        deck.pop(0)
        
for hand in hands:
    for card in hand.hand:
        print(card.face, card.suite, sep='', end=' ')
    print()
    
print('\n')

for x in range(0,22):
    print(deck[x].face, deck[x].suite, sep='', end=' ')
print()
