'''
Card counting strategy is based on Hi-Lo
'''
def count(deck):
    count = 0
    for card in deck:
        if card[0].isalpha():
            print ('%s +1' % (card))
            count -= 1
        else:
            num = int(card[0])
            if num == 1:
                print ('%s +1' % (card))
                count -= 1
            elif num != 1 and num < 7:
                print ('%s -1' % (card))
                count += 1

    return count
