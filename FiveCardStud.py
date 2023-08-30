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

deck = []
for x in range (1,5):
    for y in range(1,14):
        deck.append(Card(y,x))
        
random.shuffle(deck)

for x in range(0,52):
    print(deck[x].face, deck[x].suite, sep='', end=' ')
    if x % 7 == 6:
        print()
