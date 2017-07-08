#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from blackjack import Deck, Player, Value
from counter import count as c
''' Simulate blackjack '''

def main():
    # name variables
    deck, value = Deck(), Value()
    shuffled_deck = deck.shuffle_deck()
    spacer = '--------------------------'

    print (spacer)
    print ("BLACKJACK!!!")
    print (spacer)
    bank = eval(input('how much do you want to play with: '))
    print (spacer)
    P1 = Player('P1', bank)
    dealer = Player('dealer')
    print ('You now have %s to bet' %(P1.bank))
    print (spacer)


    answer = ['Y', 'y', 'n', 'N'] # input bank
    keep_playing = True
    a = 'Y'
    # does user want to play again
    while keep_playing == True:
        if a not in answer: # did not select Y/N
            print ('that answer is not an option...')
            a = input('do you want to keep playing? (Y/N) ') # ask once more
            continue
        else:
            if a == 'N' or a == 'n':
                keep_playing = False
                break # cut to game
        # start game
        if P1.bank == 0:
            P1.bank = int(input('you ran out of money, enter more money: '))
        bet = int(input('enter your bet: '))
        print (P1.add_bet(bet))
        print ()
        # pass cards to dealer & player(s)
        P1.hand.append(deck.deal_card())
        dealer.hand.append(deck.deal_card())
        P1.hand.append(deck.deal_card())
        dealer.hand.append(deck.deal_card())
        # show your hand & dealer's last hand
        print ('your current hand:')
        print (spacer)
        print (P1.show_hand())
        print ('value of the hand is: %s' % (value.actual_value(P1.hand)))
        print (spacer)
        print ('dealer\'s hand: %s'% (dealer.hand[-1]))
        print (spacer)
        print ('card count: %s' % (c(deck.history)))
        bj = False
        if value.actual_value(P1.hand) != 21:
            choose = input('Do you want to hit or stand? (H/S): ')
        else:
            bj = True
        # plauer's turn
        while ((choose == 'H') and not bj) or ((choose == 'h') and not bj):
            P1.hand.append(deck.deal_card())
            print (spacer)
            print ('you drew a %s. Hand value: %s' % (P1.hand[-1], value.actual_value(P1.hand)))
            print (spacer)
            print ('Current Hand:')
            print (P1.show_hand())
            if value.actual_value(P1.hand) == 0:
                print ('You busted')
                break
            print ('card count: %s' % (c(deck.history)))
            choose = input('Do you want to hit or stand? (H/S): ')
        # Dealer's turn
        print ('Dealer\'s turn')
        print (spacer)

        print ('dealer\'s hand: ')
        print (dealer.show_hand())
        print ('dealer\'s current value is: %s' % (value.actual_value(dealer.hand) ))
        while value.actual_value(dealer.hand) < 17 and value.actual_value(P1.hand) != 0: # soft 17
            dealer.hand.append(deck.deal_card())
            print ('dealer drew a %s' % (dealer.hand[-1]))
            print (spacer)
            # did dealer break?
            if value.hand_value(dealer.hand) != 0:
                print ('dealer value: %s' % (value.actual_value(dealer.hand)))
            if value.hand_value(dealer.hand) == 0:
                print ('dealer busted')
                break
        # reveal winner and give earnings
        print ('Your hand value: %s || Dealer\'s hand value: %s' % (value.actual_value(P1.hand), value.actual_value(dealer.hand)))
        if value.actual_value(P1.hand) > value.actual_value(dealer.hand):
            P1.win() # add winnings to bank
            if value.hand_value(dealer.hand) == 0:
                print ('Dealer busted')
            print ('You win!')
            print ('you now have %s dollars total' %(P1.bank))
        elif value.hand_value(P1.hand) == value.hand_value(dealer.hand):
            print ('Tie.')
        else:
            P1.lose() # subtract bet from P1 bank
            print ('Dealer wins')
            print ('you now have %s dollars total' %(P1.bank))
        print ('end of the round')
        print ()
        # clear old hands
        dealer.new_hand()
        P1.new_hand()
        a = input('do you want to keep playing? (Y/N) ')
        bj = False
        if len(deck.history) < 26:
            deck._deck = deck.shuffle_deck()

main()
