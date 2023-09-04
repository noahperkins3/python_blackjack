
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getValue(self, player):
        match self.value:
            case '1':
                return 1
            case '2':
                return 2
            case '3':
                return 3
            case '4':
                return 4
            case '5':
                return 5
            case '6':
                return 6
            case '7':
                return 7
            case '8':
                return 8
            case '9':
                return 9
            case 'J':
                return 10
            case 'Q':
                return 10
            case 'K':
                return 10
            case 'T':
                return 10
            case 'A':
                if player.total + 11 < 21:
                    return 11
                else:
                    return 1
                
    
    def getSuit(self):
        return self.suit
    
    def __str__(self):
        res = str(self.value)
        if self.suit == 'diamonds':
            return res + u'\u2666'
        if self.suit == 'spades':
            return res + u'\u2660'
        if self.suit == 'clubs':
            return res + u'\u2663'
        if self.suit == 'hearts':
            return res + u'\u2660'
        else:
            return 'invalid card!'