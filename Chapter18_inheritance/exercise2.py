import random


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def pop_card(self):
        return self.cards.pop() 

    def sort(self):
        self.cards.sort()

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()
        
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self,num_of_hands,cards_per_hand):
        hand_list=list()
        deck=Deck()
        deck.shuffle()
        for i in range(num_of_hands):
                new_hand=Hand()
                deck.move_cards(new_hand,cards_per_hand)
                hand_list.append(new_hand)
        return hand_list

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.
        returns: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def __str__(self):
        return "Suit: "+str(self.suit)+" rank: "+ str(self.rank)
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

def main():
    deck=Deck()
    
    hand_list=(deck.deal_hands(2,2))
    for hand in hand_list:
        print(hand)

if __name__ == '__main__':
    main()