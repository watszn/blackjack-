from blackjack import Deck, Player, Value
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
        bet = int(input('enter your bet: '))
        print (P1.add_bet(bet))
        print ()
        # pass cards to dealer & player(s)
        P1.hand.append(deck.deal_card())
        dealer.hand.append(deck.deal_card())
        P1.hand.append(deck.deal_card())
        dealer.hand.append(deck.deal_card())
        # show your hand & dealer's last hand
        print ('your current hand: %s' % (P1.hand))
        print ('value of the hand is: %s' % (value.hand_value(P1.hand)))
        print (spacer)
        print ('dealer\'s hand: %s'% (dealer.hand[-1]))
        print (spacer)

        choose = input('Do you want to hit or stand? (H/S): ')
        # plauer's turn
        while (choose == 'H') or (choose == 'h'):
            P1.hand.append(deck.deal_card())
            print (spacer)
            print ('you drew a %s. Hand value: %s' % (P1.hand[-1],  value.hand_value(P1.hand)))
            print (spacer)
            print ('Current Hand:')
            print (P1.show_hand())
            if value.hand_value(P1.hand) > 21:
                print ('You busted')
                print (P1.lose())
                break
            choose = input('Do you want to hit or stand? (H/S): ')
        # Dealer's turn
        print ('Dealer\'s turn')
        print (spacer)

        print ('current value is: %s' % ( int(value.hand_value(dealer.hand))))
        while int(value.hand_value(dealer.hand)) <= 17:
            print ('dealer value: %s' % (int(value.hand_value(dealer.hand))))
            dealer.hand.append(deck.deal_card())
        # reveal winner and give earnings
        print ('Your hand value: %s || Dealer\'s hand value: %s' % (value.hand_value(P1.hand), value.hand_value(dealer.hand)))
        if value.hand_value(P1.hand) > value.hand_value(dealer.hand):
            print ('You win!')
            print ('you now have %s dollars total' %(P1.win()))
        else:
            print ('Dealer wins')
            print ('you now have %s dollars total' %(P1.lose()))
        print ('end of the round')
        print ()
        # clear old hands
        dealer.new_hand()
        P1.new_hand()
        a = input('do you want to keep playing? (Y/N) ')

main()
