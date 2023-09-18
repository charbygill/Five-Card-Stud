import random
import sys

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

class Poker_Table:
    def __init__(self):
        self.hands = []
        self.deck = []
        self.duplicate = None
        for x in range (1,5):
            for y in range(2,15):
                self.deck.append(Card(y,x))
        random.shuffle(self.deck)
    def input_hands(self):
        with open(sys.argv[1], 'r') as my_file:
            lines = my_file.readlines()
            for line in lines:
                self.hands.append(Hand())
                line = line.strip()
                cards = line.split(",")
                for card in cards:
                    str = card.replace(" ", "")
                    new_card = self.input_card(str[-2],str[-1])
                    self.hands[-1].deal(new_card)
                    found = False
                    for search_card in self.deck:
                        if search_card.face_int == new_card.face_int and search_card.suite_int == new_card.suite_int:
                            self.deck.pop(self.deck.index(search_card))
                            found = True
                    if not found:
                        self.duplicate = new_card
    def input_card(self, face, suite):
        if face == "A":
            face_int = 14
        elif face == "K":
            face_int = 13
        elif face == "Q":
            face_int = 12
        elif face == "J":
            face_int = 11
        elif face == "0":
            face_int = 10
        else:
            face_int = int(face)
        if suite == 'D':
            suite_int = 1
        elif suite == 'C':
            suite_int = 2
        elif suite == 'H':
            suite_int = 3
        else:
            suite_int = 4
        return Card(face_int, suite_int)
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
                print("---", hand.value_str)
        print('\n')
    def rank_hands(self):
        for hand in self.hands:
            sorted_hand = hand.sort()
            temp = []
            flush = 0
            straight = True
            prev_card_int = None
            for x in range(0,5):
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
                        if not x == 4:
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
                    hand.value_str = "Four of a Kind"
                else:
                    hand.value = 4
                    hand.value_str = "Full House"
            elif len(temp) == 3:
                if len(temp[0]) == 3 or len(temp[1]) == 3 or len(temp[2]) == 3:
                    hand.value = 7
                    hand.value_str = "Three of a Kind"
                else:
                    hand.value = 8
                    hand.value_str = "Two Pair"
            elif len(temp) == 4:
                hand.value = 9
                hand.value_str = "Pair"
            if flush != 5 and straight:
                if hand.low_ace and prev_card_int == 5:
                    hand.value = 2
                    hand.value_str = "Straight Flush"
                else:
                    hand.value = 1
                    hand.value_str = "Royal Straight Flush"
            elif flush != 5:
                hand.value = 5
                hand.value_str = "Flush"
            elif straight:
                hand.value = 6
                hand.value_str = "Straight"
            if hand.value == 0:
                hand.value = 10
                hand.value_str = "High Card"
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
        
        return self.tiebreak_recursive(temp_1,temp_2,hand_1,hand_2)
    def tiebreak_recursive(self, hand_1, hand_2, ref_1, ref_2):
        if hand_1[-1][-1][-1].face_int < hand_2[-1][-1][-1].face_int:
            return True
        elif hand_1[-1][-1][-1].face_int == hand_2[-1][-1][-1].face_int:
            if not len(hand_1[-1][0]) == 1:
                if len(hand_1[-1]) == 1:
                    hand_1.pop(len(hand_1) - 1)
                    hand_2.pop(len(hand_1) - 1)
                else:
                    hand_1[len(hand_1) - 1].pop(len(hand_1[len(hand_1) - 1]) - 1)
                    hand_2[len(hand_1) - 1].pop(len(hand_1[len(hand_1) - 1]) - 1)
                return self.tiebreak_recursive(hand_1,hand_2)
            else:
                if not (ref_1.low_ace and ref_2.low_ace):
                    if hand_1[-1][-1][-1].suite_int < hand_2[-1][-1][-1].suite_int:
                        return True
                else:
                    if hand_1[-1][-2][-1].suite_int < hand_2[-1][-2][-1].suite_int:
                        return True
        return False
            
class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.value_str = None
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
print("*** P O K E R  H A N D  A N A L Y Z E R ***")
if len(sys.argv) == 2:
    print("*** USING TEST DECK OF CARDS ***")
    table.input_hands()
else:
    print("*** USING RANDOMIZED DECK OF CARDS ***")
    print("*** Shuffled 52 card deck:")
    table.print_deck(13)
    table.deal()
print("*** Here are the six hands...")
table.print_hands()
if not table.duplicate:
    print("*** Here is what remains in the deck...")
    table.print_deck()
    print("--- WINNING HAND ORDER ---")
    table.rank_hands()
    table.order_hands()
    table.print_hands()
else:
    print("*** ERROR - DUPLICATED CARD FOUND IN DECK ***")
    print("*** DUPLICATE: ",table.duplicate.face,table.duplicate.suite," ***", sep="")
