import card
import random

class Deck:

    def __init__(self):
        self.deck = []
        suits = ['spades', 'diamonds', 'hearts', 'clubs']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'T', 'A']
        for suit in suits:
            for value in values:
                self.deck.append(card.Card(suit, value))

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        res = ""
        for card in self.deck:
            res += card.__str__() + ' '
        return res
    
    def pullTopCard(self):
        res = self.deck[0]
        self.deck.remove(res)
        return res