import card

class Player:

    def __init__(self):
        self.starting_amount = 500
        self.total = 0
        self.hand = []


    def addCard(self, card):
        self.hand.append(card)
        self.total += card.getValue(self)

    def getTotal(self):
        return self.total


    def __str__(self):
        res = ''
        for card in self.hand:
            res += card.__str__() + ', '
        return res[0:(len(res)-2)]