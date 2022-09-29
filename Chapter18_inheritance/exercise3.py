"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division
from audioop import reverse

from exercise2 import Hand, Deck, Card


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        return self.ranks


    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
    
    def has_two_pairs(self):
        rank_list=list()
        for item in self.ranks.values():
            rank_list.append(item)
        rank_list.sort(reverse=True)
        if rank_list[0] >=2 and rank_list [1] >= 2:
            return True
        else:
            return False

    def has_full_house(self):
        rank_list=list()
        for item in self.ranks.values():
            rank_list.append(item)
        rank_list.sort(reverse=True)
        print(rank_list)
        if rank_list[0] >=3 and rank_list [1] >= 2:
            return True
        else:
            return False



    def has_three_of_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
 
  
    def has_four_of_kind(self):
        self.rank_hist()    
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straight_five(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

        rank_list=list()
        for item in self.ranks.values():
            rank_list.append(item)
        rank_list.sort(reverse=True)
        print(rank_list)
        print("-----")
        print(self.suits)
        print("-----")
        if rank_list[0] >=2 and rank_list [1] >= 2:
            return True
        else:
            return False

      

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print('')
        print("Has pair: "+str(hand.has_pair()))
        print("Has two pairs: "+str(hand.has_two_pairs()))
        print("Has three of a kind: "+str(hand.has_three_of_kind()))
        # straight
        
        print("Has flush: "+str(hand.has_flush()))
        print("Has straight five: "+str(hand.has_straight_five()))
        
        
      #  print("Has flsuh: "+str(hand.has_flush()))
      #  print("Has pair: "+str(hand.has_pair()))
    # straight flush

        print('')
