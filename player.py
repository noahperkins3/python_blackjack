
class Player:

    def __init__(self, deck):
        self.deck = deck
        self.total = 0
        self.hand = []

    def firstDeal(self):
        for i in range(2):
            self.hand.append(self.deck.pullTopCard())

    def hit(self, card):
        self.hand.append(card)
        self.total += card.getValue(self)

    def resetDeck(self, deck):
        self.deck = deck
        self.hand = []
        self.total = 0

    def __str__(self):
        res = ''
        for card in self.hand:
            res += card.__str__() + ', '
        return res[0:(len(res)-2)]
    
class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.starting_amount = 500
        self.total = 0
        self.hand = []
        self.hide = True

    def firstDeal(self):
        for i in range(2):
            self.hand.append(self.deck.pullTopCard())

    def hit(self, card):
        self.hand.append(card)
        self.total += card.getValue(self)

    # def setHide(self, hide):
    #     self.hide = hide

    def resetDeck(self, deck):
        self.deck = deck
        self.hand = []
        self.total = 0

    def __str__(self):
        res = ''
        if self.hide:
            res += self.hand[0].__str__() + ", Unknown"
        else:
            for card in self.hand:
                res += card.__str__() + ', '
            res = res[0:(len(res)-2)]
        return res