from blackjack import Deck, Player

def main():
    # create a player
    P1 = Player('P1', 200) # start w 200
    P1_bank = P1.bank
    deck = Deck()
    dealer = Player('dealer')
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


    

main()
