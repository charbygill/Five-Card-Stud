import random
import sys

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
    #def input(self):
        
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
            if not hand.value == 0:
                print("---", end=' ')
            if hand.value == 1:
                print("Royal Straight Flush")
            elif hand.value == 2:
                print("Straight Flush")
            elif hand.value == 3:
                print("Four of a Kind")
            elif hand.value == 4:
                print("Full House")
            elif hand.value == 5:
                print("Flush")
            elif hand.value == 6:
                print("Straight")
            elif hand.value == 7:
                print("Three of a Kind")
            elif hand.value == 8:
                print("Two Pair")
            elif hand.value == 9:
                print("Pair")
            elif hand.value == 10:
                print("High Card")
        print('\n')
    def rank_hands(self):
        for hand in self.hands:
            sorted_hand = hand.sort()
            temp = []
            flush = 0
            straight = True
            ace = False
            prev_card_int = None
            for x in range(0,5):
                if sorted_hand[x].face_int == 14:
                    ace = True
                
                if flush != 0 and flush != 5:
                    if sorted_hand[x].suite_int != flush:
                        flush = 5
                elif flush == 0:
                    flush = sorted_hand[x].suite_int

                if prev_card_int == None:
                    prev_card_int = sorted_hand[x].face_int
                elif straight:
                    if prev_card_int + 1 == sorted_hand[x].face_int or (prev_card_int == 5 and sorted_hand[x].face_int == 14):
                        if prev_card_int == 5 and sorted_hand[x].face_int == 14:
                            hand.low_ace = True
                        prev_card_int = sorted_hand[x].face_int
                    else:
                        straight = False
                
                if len(temp) == 0:
                    temp.append([])
                    temp[0].append(sorted_hand[x])
                else:
                    inserted = False
                    for y in temp:
                        if y[0].face_int == sorted_hand[x].face_int:
                            y.append(sorted_hand[x])
                            inserted = True
                    if not inserted:
                        temp.append([])
                        temp[len(temp)-1].append(sorted_hand[x])
            hand.sorted = temp
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
            if hand.value == 0:
                hand.value = 10
    def order_hands(self):
        sorted_hands = []
        for hand in self.hands:
            sorted_hands.append(hand)
        n = len(sorted_hands)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if sorted_hands[j].value > sorted_hands[j + 1].value:
                    swapped = True
                    sorted_hands[j], sorted_hands[j + 1] = sorted_hands[j + 1], sorted_hands[j]
                elif sorted_hands[j].value == sorted_hands[j + 1].value:
                    if self.tiebreak(sorted_hands[j], sorted_hands[j + 1]):
                        swapped = True
                        sorted_hands[j], sorted_hands[j + 1] = sorted_hands[j + 1], sorted_hands[j]
            if not swapped:
                self.hands = sorted_hands
        self.hands = sorted_hands
    def tiebreak(self, hand_1, hand_2):
        if hand_1.groups == None:
            hand_1.group()
        if hand_2.groups == None:
            hand_2.group()
            
        temp_1 = hand_1.groups.copy()
        temp_2 = hand_2.groups.copy()
        
        return self.tiebreak_recursive(temp_1,temp_2,hand_1.low_ace)
    def tiebreak_recursive(self, hand_1, hand_2, low_ace):
        if hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1]) - 1][len(hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1])-1]) - 1].face_int < hand_2[len(hand_1) - 1][len(hand_1[len(hand_1) - 1]) - 1][len(hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1])-1]) - 1].face_int:
            return True
        elif hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1]) - 1][len(hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1])-1]) - 1].face_int == hand_2[len(hand_1) - 1][len(hand_1[len(hand_1) - 1]) - 1][len(hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1])-1]) - 1].face_int:
            if not len(hand_1[len(hand_1) - 1][0]) == 1:
                if len(hand_1[len(hand_1) - 1]) == 1:
                    hand_1.pop(len(hand_1) - 1)
                    hand_2.pop(len(hand_1) - 1)
                else:
                    hand_1[len(hand_1) - 1].pop(len(hand_1[len(hand_1) - 1]))
                    hand_2[len(hand_1) - 1].pop(len(hand_1[len(hand_1) - 1]))
                return self.tiebreak_recursive(hand_1,hand_2)
            else:
                if not low_ace:
                    if hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1]) - 1][len(hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1])-1]) - 2].suite_int < hand_2[len(hand_1) - 1][len(hand_1[len(hand_1) - 1]) - 1][len(hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1])-1]) - 2].suite_int:
                        return True
                else:
                    if hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1]) - 1][len(hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1])-1]) - 2].suite_int < hand_2[len(hand_1) - 1][len(hand_1[len(hand_1) - 1]) - 1][len(hand_1[len(hand_1) - 1][len(hand_1[len(hand_1) - 1])-1]) - 2].suite_int:
                        return True
        return False
            
class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.sorted = None
        self.groups = None
        self.low_ace = False
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
    def group(self):
        temp = []
        if len(self.sorted) == 5:
            temp.append([])
            for card in self.sorted:
                temp[0].append(card)
        else:
            temp.append([])
            temp.append([])
            low = 2;
            for card in self.sorted:
                if len(card) < low:
                    low = len(card)
            if low == 1:
                for card in self.sorted:
                    if len(card) == 1:
                        temp[0].append(card)
                    else:
                        temp[1].append(card)
            else:
                for card in self.sorted:
                    if len(card) == 2:
                        temp[0].append(card)
                    else:
                        temp[1].append(card)
        self.groups = temp
        
table = Poker_Table()
#if len(sys.argv) == 2:
    #table.input()
table.print_deck(13)
table.deal()
table.print_hands()
table.print_deck()
table.rank_hands()
table.order_hands()
table.print_hands()
