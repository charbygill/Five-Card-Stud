import random

#Start by making a card class
class Card:
    def __init__(self, face, suite):
        if face < 11:
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
        if face == 14:
            self.face = ' A'
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
            for y in range(2,15):
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
        for hand in self.hands:
            sorted_hand = hand.sort()
            temp = []
            flush = 0
            straight = True
            ace = False
            prev_card_int = None
            for card in sorted_hand:
                if card.face_int == 14:
                    ace = True
                
                if flush != 0 and flush != 5:
                    if card.suite_int != flush:
                        flush = 5
                elif flush == 0:
                    flush = card.suite_int

                if prev_card_int == None:
                    prev_card_int = card.face_int
                elif straight:
                    if prev_card_int + 1 == card.face_int or (prev_card_int == 5 and card.face_int == 14):
                        prev_card_int = card.face_int
                    else:
                        straight = False
                
                if len(temp) == 0:
                    temp.append([])
                    temp[0].append(card)
                    hand.kicker = card
                else:
                    inserted = False
                    for x in temp:
                        if x[0].face_int == card.face_int:
                            x.append(card)
                            inserted = True
                    if not inserted:
                        temp.append([])
                        temp[len(temp)-1].append(card)
                        hand.kicker = card
            if len(temp) == 2:
                if len(temp[0]) == 1 or len(temp[0]) == 4:
                    hand.value = 3
                else:
                    hand.value = 4
            elif len(temp) == 3:
                if len(temp[0]) == 3 or len(temp[1]) == 3 or len(temp[2]) == 3:
                    hand.value = 7
                else:
                    hand.value = 8
            elif len(temp) == 4:
                hand.value = 9
            if flush != 5 and straight:
                if ace and prev_card_int == 5:
                    hand.value = 2
                else:
                    hand.value = 1
            elif flush != 5:
                hand.value = 5
            elif straight:
                hand.value = 6
            print(hand.value)

class Hand:
    def __init__(self):
        self.hand = []
        self.value = 10
        self.kicker = None
    def deal(self, card):
        self.hand.append(card)
    def sort(self):
        sorted_hand = []
        for card in self.hand:
            sorted_hand.append(card)
        n = len(sorted_hand)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if sorted_hand[j].face_int > sorted_hand[j + 1].face_int:
                    swapped = True
                    sorted_hand[j], sorted_hand[j + 1] = sorted_hand[j + 1], sorted_hand[j]
            if not swapped:
                return sorted_hand
        return sorted_hand

table = Poker_Table()
table.print_deck(13)
table.deal()
table.print_hands()
table.print_deck()
table.rank_hands()
