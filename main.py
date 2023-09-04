import deck
import player

thresh = 21

def checkWin(new_player, new_dealer):
    if new_player.getTotal() > new_dealer.getTotal() and new_player.getTotal() <= 21:
        return True
    else:
        return False

def play():
    cash_amount = 500
    running = True
    while running:
        new_deck = deck.Deck()
        new_deck.shuffle()
        new_dealer = player.Dealer(new_deck)
        new_player = player.Player(new_deck)
        game_over = False
        print("\nYour starting amount is $" + str(cash_amount))
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
                new_player.hit(new_deck.pullTopCard())
                new_dealer.hit(new_deck.pullTopCard())
            print("You are dealt: " + new_player.__str__())
            print("The new_dealer is dealt: " + new_dealer.__str__())
            if new_player.getTotal() == thresh:
                if not new_dealer.getTotal() == thresh:
                    print("Your starting hand is a blackjack, you win!")
                    cash_amount += bet_amount * 1.5
                else:
                    print("You and the dealer were dealt blackjack - tie.")
            else:
                while not game_over:
                    hit_or_stay = input("Would you like to hit or stay? ")
                    while not hit_or_stay == 'hit' and not hit_or_stay == 'stay':
                        print("That is not a valid option. ")
                        hit_or_stay = input("Would you like to hit or stay? ")
                    if hit_or_stay == 'hit':
                        new_player.hit(new_deck.pullTopCard())
                        print("You are dealt: " + new_player.getHand()[-1].__str__())
                        print("You now have: " + new_player.__str__())
                        if new_player.getTotal() > thresh:
                            print("Your hand value is over 21 and you lose " + str(bet_amount) + " :(")
                            cash_amount -= bet_amount
                            if cash_amount <= 0:
                                print("\nYou've ran out of money. Please restart the program to try again. See you!")
                                running = False
                            game_over = True
                    elif hit_or_stay == 'stay':
                        new_dealer.setHide(False)
                        print("The dealer has: " + new_dealer.__str__())
                        while new_dealer.getTotal() <= 16:
                            new_dealer.hit(new_deck.pullTopCard())
                            print("The dealer hits and is dealt: " + new_dealer.getHand()[-1].__str__())
                        print("The dealer stays.")
                        if new_dealer.getTotal() > 21:
                            print("The dealer busts, you win $" + str(bet_amount) + " :)")
                            cash_amount += bet_amount
                        elif new_player.getTotal() > new_dealer.getTotal():
                            print("You win $" + str(bet_amount) + "!")
                            cash_amount += bet_amount
                        elif new_player.getTotal() < new_dealer.getTotal():
                            print("The dealer wins and you lose $" + str(bet_amount) + " :(")
                            cash_amount -= bet_amount
                            if cash_amount <= 0:
                                print("\nYou've ran out of money. Please restart the program to try again. See you!")
                                running = False
                        elif new_dealer.getTotal() == new_player.getTotal():
                            print("You tie. Your bet has been returned.")
                        game_over = True
        else:
            print("You left with $" + str(cash_amount) + " in hand. See you!")
            running = False

if __name__ == '__main__':
    print("Welcome to blackjack!")
    play()