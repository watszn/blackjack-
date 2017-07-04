import random
# creating variables
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_cards = ['Jack', 'Queen', 'King', 'Ace']
reg_cards = [str(x) for x in range (2, 11)]
classic_deck = [{suit: card} for suit in suits for card in face_cards] + [{suit: card} for suit in suits for card in reg_cards]

class Value:
    def __init__(self):
        self.card_bank = {'A': 1,
                          '2': 2,
                          '3': 3,
                          '4': 4,
                          '5': 5,
                          '6': 6,
                          '7': 7,
                          '8': 8,
                          '9': 9,
                          '10': 10,
                          'A': 11,
                          'J': 10,
                          'Q': 10,
                          'K': 10}

    def hand_value(self, hand = []):
        value = 0
        for card in hand:
            if card[0].isdigit() or card[0:2].isdigit(): # not face card
                if not card[0:2].isdigit(): # 10
                    value += int(card[0])
                else:
                    value += int(card[0:2])
            elif card[0].isalpha(): # face card
                if card[0] != 'A':
                    value += 10
                else: # Ace
                    value += 1
        if int(value) < 22:
            return int(value)
        else:
            return 0 # bust

    def ace_present(self, hand):
        ace = 0
        for card in hand:
            if card[0] == 'A':
                ace += 1
        if ace != 0:
            return 10
        else:
            return 0

    def actual_value(self, hand):
        ''' gives actual card value using ace_present and hand_value '''
        if self.hand_value(hand) == 0:
            return 0 # bust
        elif self.hand_value(hand) + self.ace_present(hand) > 21:
            return self.hand_value(hand)
        else:
            return self.hand_value(hand) + self.ace_present(hand)

class Player: # abstract base class (abc)
    ''' describes player's bank, bet, wins, and losses '''
    def __init__(self, name = 'J doe', bank = 0):
        self.name = name
        self.bet = 0
        self.bank = bank
        self.hand = []

    def show_hand(self, ):
        for card in self.hand:
            print (card)
        return ' '

    def add_bank(self, add):
        self.bank += add

    def add_bet(self, bet):
        if int(bet) > int(self.bank):
            print ('this bet is higher than what you have, you have %s available' %(self.bank))
            bet = int(input('enter new bet: '))
            return self.add_bet(bet)
        else:
            self.bet = bet
            return ('you bet %s dollars' % (self.bet))

    def win(self): # return bank w winnings
        self.bank = self.bank + self.bet
        return self.bank

    def lose(self):
        self.bank = self.bank - self.bet
        if self.bank <= 0:
            print ('you lost %d dollars, you now have %d avalaible' %(self.bet, self.bank))
            self.bank = 0
            return self.bank
        else:
            return self.bank

    def new_hand(self):
        self.hand = []
        return self.hand


class Deck:
    ''' deck characteristics... includes dealing card, shuffling, collecting cards '''
    def __init__(self, deck = ['%s of %s' %(rank, suit) for card in classic_deck for suit, rank in card.items()] ):
        self._deck = deck
        self.history = []

    def show_deck(self):
        return self._deck

    def shuffle_deck(self):
        self._deck = random.sample(self._deck, len(self._deck))
        return self._deck

    def deal_card(self):
        card = self._deck[0]
        self.history.append(self._deck[0]) # add to discard pile
        self._deck = self._deck[1:] # update deck
        return card

    def collect_cards(self):
        for card in self.history:
            self._deck.append(card)
        print ('all discard pile added back to the deck: ')
        return self._deck
