from blackjack import Deck, Player, Value

def main():
    # create a player
    P1 = Player('P1', 200) # start w 200
    P1_bank = P1.bank
    deck = Deck()
    dealer = Player('dealer')
    value = Value()
    # show beginning bank

    # win round
    P1.add_bet(20)
    P1_bank = P1.win()
    print (P1_bank)
    # check if a card in deck is discarded
    print ('deck before drawing: %s' % (len(deck._deck)))
    print ()
    print ('you drew a %s' % (deck.deal_card()))
    print ()
    print ('deck after drawing: %s' % (len(deck._deck)))


    # checking hand
    P1.hand.append(deck.deal_card())
    P1.hand.append(deck.deal_card())
    print ('current hand:')
    print (P1.show_hand())
    P1_hand_value = value.hand_value(P1.hand) + value.ace_present(P1.hand)
    print (P1_hand_value)
    while P1_hand_value < 21 and value.hand_value(P1.hand) != 0:
        P1.hand.append(deck.deal_card())
        print ('you drew %s' % (P1.hand[-1]))
        print ('hand value is now %s' % (P1_hand_value))
    if value.hand_value(P1.hand) == 0:
        print ('You busted')


main()
