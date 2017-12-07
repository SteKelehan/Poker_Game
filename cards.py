import random
from collections import Counter
# pair/ two pair/ three of a kind/ 4 of a kind 



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
        self.position = 0
        self.turn = False
        self.call = False
        self.fold = False
        self.bet = False
        self.allin = False
        self.check = False
        self.button = False
        self.inpos = 3


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
            return self.hand

    def Position(self, pos):
        self.position = pos

    def showPosisiotn(self):
        return self.position
    
    def blindpos(self):
        return self.inpos
        
    

    
        


        

        


# In a hand there is:
# Players, Deal, Button and blinds, Pot, Ceck, Bet, Fold, Burn, Flop, Burn, Turn, Burn, River, Winner
class Rules(object):
    def __inti__(self):
        pass
        
    def hands(self):
        pass

    
    def consective_numbers(self,numbers_sorted):
        cur_max = 0
        max_ = 0
        cur_index = 0
        index = 0
        for number in numbers_sorted:
            if number == len(numbers_sorted):
                return max_, index
            else:
                if number == 0:
                    prev = number
                else:
                    if prev + 1 == number:
                        cur_max += 1
                    if cur_max > max_:
                        max_ = cur_max
                        index = number - cur_max
                        cur_max = 0


    # Hands combos with only one posibility - High card (all diff), Pair, Two Pair, 4 of a kind
    # Hand combos with more - Tree of a kind(two 3 of kind)
                            # - Straight(1234567) -> pick the highest 5
                            # - Flush -> pick the highest values 
                            # - Full house -> 2 3 of a kind -> higher 3 of a kind is the 3 other is 2
                            # - Straight Flush -> pick the highest 
    def Ranks(self, hand, board):
        total = hand + board
        numbers = []
        suits = []
        numbers_sorted = []
        for t in total:
            numbers.append(total.val)
            suits.append(total.suit)
        #this returns a list of tuples with 1st element -> val and second how many times it shows up
        most_common_number = [number for number in Counter(numbers).most_common(2)]
        most_common_suit = [suit for suit in Counter(suits).most_common(1)]
        #this is a list o 
        numbers_sorted = numbers.sort()
        # Gets no. of sequence and where they start
        number_sequence = []

        cons_numbs = consective_(numbers_sorted)
        
        suit_frequ = most_common_suit[0][1]
        suit_val = most_common_suit[0][0]
        num_frequ = most_common_number[0][1]
        num_val = most_common_number[0][0]
        num_frequ2 = most_common_number[1][1]
        num_val2 = most_common_number[1][0]
        


        # startements to work out best hand - start from best to worst, frst hand found return it!
        #Royal Flush
        if suit_frequ > 4 and cons_numbs[1] > 4:
            for x in range(cons_numbs[2], cons_numbs[2] + 5):
                pass

        #Straight Flush
        #4 ofa kind
        #Full House
        #Flush
        #Straight
        #3 of a Kind
        #2 pair
        #Pair
        #High Card

    def Handnames(self, rank):
        if rank == 0:
            return 'High Card'
        elif rank == 1:
            return 'One Pair'
        elif rank == 2:
            return 'Two Pair'
        elif rank == 3:
            return 'Three of a Kind'
        elif rank == 4:
            return 'Straight'
        elif rank == 5:
            return 'Flush'
        elif rank == 6:
            return 'Full House'
        elif rank == 7:
            return 'Four of a kind'
        elif rank == 8:
            return 'Straight Flush'
        else:
            return 'Role Flush'

    def handval(self):
        pass

    def betterhand(self, hand1, hand2):
        pass

    

        


#make a list of players!

class Hand(object):
    def __inti__(self, Plaeyers):
        self.Players = Players
        self.handId = 0
        self.button = 0
        self.BB = 1
        self.SM = 2
        self.pot = pot
        self.flop = flop
        self.burn = burn
        self.turn = turn
        self.river = rover
        self.winner = winner
        self.split = split
        self.sidepot = sidepot

    # this should call the player rotaion, and pot renule etc.
    def handinc(self):
        self.handId += 1
        return self.handId

    # This sets up the players in a seating positon and gives them the dealer, BB and SM    
    def Playerposition(self):
        for player in Players:
            Players[player].position = player
        Players[0].blindpos = 0
        Players[0].button = True
        Players[1].blindpos = 1
        Players[2].blindpos = 2

    # This rotates the dealer, BB and SB
    def buttonrotaion(self):
        index = 0
        for player in Players:
            if Players[player].button == True:
                Players[player].button == False
                Players[player].blindpos = 3
                index = player + 1
                break
        for x in range(0,3):
            if index > len(Players):
                Players[0] = x
            else:
                Players[index] = x

    def Pot(self):
        print("Pot: ", self.pot)

    def winner(self):
        pass
        


        
                     
        





  
class Table(object):
    def __init__ (self):
        pass







#testing


print('-------GAME PLAY!!--------')

print('Creating players')
player1 = Player("Ste", 2000)
player2 = Player("Adam", 2000)
player3 = Player("Richie", 2000)
player4 = Player("Keith", 2000)
player5 = Player("Luke", 2000)
player6 = Player("Alex", 2000)

Players = [player1, player2, player3, player4, player5, player6]

Blinds = [10,20]

deck = Deck()
deck.shuffle()

hand = Hand()
hand.Playerposition()





hand.handId()








