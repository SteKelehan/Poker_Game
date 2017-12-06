import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # This will print the card!
    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades" , "Harts", "Clubs", "Dimands"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()


    def shuffle(self):
        #decriment from end of list to start
        for i in range(len(self.cards)-1, 0, -1):
            #pick a random number between the first and the current index your on
            r = random.randint(0,i)
            #swaps the r (random index) with the current index
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    #this will allow you to pick the top card
    def drawCard(self):
        return self.cards.pop()

# Player has a stack and cards
class Player(object):
    def __init__(self, name, stack):
        self.name = name
        self.hand = []
        self.stack = stack
        self.position = position 

    def stacklevel(self, amount):
        self.stack = self.stack + amount 
        return self.stack 

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        #this allows you to call more than one card
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def Position(self, pos):
        self.position = pos

    def showPosisiotn(self):
        return self.position
        

        


# In a hand there is:
# Players, Deal, Button and blinds, Pot, Ceck, Bet, Fold, Burn, Flop, Burn, Turn, Burn, River, Winner


class Rules(object):
    def __inti__(self):
        pass

#make a list of players!

class Hand(object):
    def __inti__(self, Plaeyers):
        self.Players = Players
        self.handId = handId
        self.button = False
        self.BB = False
        self.SM = SM
        self.pot = pot
        self.flop = flop
        self.burn = burn
        self.turn = turn
        self.river = rover
        self.winner = winner
        self.slip = slip
        self.sidepot = sidepot

    def handinc(self):
        self.handId += 1
        return self.handId

    




    
class Table(object):
    def __init__ (self):
        pass







#testing


deck = Deck()
deck.shuffle()
card = deck.drawCard()
card.show()

player = Player("Ste", 2000)
player.draw(deck)
player.showHand()
print(player.stacklevel(100))




