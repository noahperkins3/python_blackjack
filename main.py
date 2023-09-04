import card
import deck
import player

cash_amount = 500
thresh = 21

running = True
dealer = player.Dealer(deck.Deck())
player = player.Player(deck.Deck())

def checkWin(player, dealer):
    if player.getTotal() > dealer.getTotal() and player.getTotal() < 21:
        return True
    else:
        return False

while running:
    new_deck = deck.Deck()
    new_deck.shuffle()
    dealer.resetDeck(new_deck)
    player.resetDeck(new_deck)
    game_over = False
    print("Welcome to Blackjack!\n\nYour starting amount is $" + str(cash_amount))
    play = input("Would you like to play a hand? ")
    if play[0] == 'y' or play[0] == 'Y':
        bet_amount = int(input("Place your bet: "))
        while bet_amount < 1:
            print("The minimum bet is $1. ")
            bet_amount = int(input("Place your bet: "))
        while bet_amount > cash_amount:
            print("Insufficient funds! ")
            bet_amount = int(input("Place your bet: "))
        # first deal
        for i in range(2):
            player.hit(new_deck.pullTopCard())
            dealer.hit(new_deck.pullTopCard())
        print("You are dealt: " + player.__str__())
        print("The dealer is dealt: " + dealer.__str__())
        if player.getTotal() == thresh:
            if not dealer.getTotal() == thresh:
                print("Your starting hand is a blackjack, you win!")
                cash_amount += bet_amount * 1.5
            else:
                print("You and the dealer were dealt blackjack, tie.")
        else:
            while not game_over:
                hit_or_stay = input("Would you like to hit or stay? ")
                while not hit_or_stay == 'hit' and not hit_or_stay == 'stay':
                    print("That is not a valid option. ")
                    hit_or_stay = input("Would you like to hit or stay? ")
                if hit_or_stay == 'hit':
                    player.hit(new_deck.pullTopCard())
                    print("You are dealt: " + player.getHand()[-1].__str__())
                    print("You now have: " + player.__str__())
                    if player.getTotal() > thresh:
                        print("Your hand value is over 21 and you lose " + str(bet_amount) + " :(")
                        cash_amount -= bet_amount
                        if cash_amount <= 0:
                            print("\nYou've ran out of money. Please restart the program to try again. See you!")
                            running = False
                        game_over = True
                elif hit_or_stay == 'stay':
                    dealer.setHide(False)
                    print("The dealer has: " + dealer.__str__())
                    while dealer.getTotal() <= 16:
                        dealer.hit(new_deck.pullTopCard())
                        print("The dealer hits and is dealt: " + dealer.getHand()[-1].__str__())
                    print("The dealer stays.")
                    if checkWin(player, dealer):
                        print("You win $" + bet_amount + "!")
                    else:
                        print("The dealer wins and you lose " + str(bet_amount) + " :(")
                        if cash_amount <= 0:
                            print("\nYou've ran out of money. Please restart the program to try again. See you!")
                            running = False
                    game_over = True
    else:
        print("You left with $" + str(cash_amount) + " in hand. See you!")
        running = False


 

# player = player.Player()
# deck = deck.Deck()

# deck.shuffle()
# player.hit(deck.pullTopCard())
# player.hit(deck.pullTopCard())


# print(player.__str__())
# print(player.getTotal())
