import os
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


class Player(object):
    def __inti__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        #this allows you to call more than one card
        return self

    def showHand(self):
        for card in self.hand:
            card.show()







#testing


deck = Deck()
deck.shuffle()
card = deck.drawCard()
card.show()

player = Player("hi")
player.draw(deck)
palyer.showHand()




