from random import randint
from enum import Enum

class Number(Enum):
    ACE      = ('Ace', 11)
    TWO      = ('Two', 2)
    THREE    = ('Three', 3)
    FOUR     = ('Four', 4)
    FIVE     = ('Five', 5)
    SIX      = ('Six', 6)
    SEVEN    = ('Seven', 7)
    EIGHT    = ('Eight', 8)
    NINE     = ('Nine', 9)
    TEN      = ('Ten', 10)
    JACK     = ('Jack', 10)
    QUEEN    = ('Queen', 10)
    KING     = ('King', 10)

    def __init__(self, numberName, numberValue):
        self.numberName = numberName
        self.numberValue = numberValue

class Suit(Enum):
    SPADES   = 'Spades'
    CLUBS    = 'Clubs'
    DIAMONDS = 'Diamonds'
    HEARTS   = 'Hearts'

class Card(object):

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return self.number.numberName + ' of ' + self.suit.value

    @property
    def value(self):
        return self.number.numberValue

    def isAce(self):
        if self.number == Number.ACE:
            return True
        return False

class Deck(object):

    def __init__(self):
        self.deck = []
        self.__populateDeck()
        self.__shuffleDeck()

    def __populateDeck(self):
        for suit in Suit:
            for numb in Number:
                self.deck.append(Card(numb,suit))
    
    def __shuffleDeck(self):
        for i in range(1000):
            pos1 = randint(0,len(self.deck)-1)
            pos2 = randint(0,len(self.deck)-1)
            temp = self.deck[pos1]
            self.deck[pos1] = self.deck[pos2]
            self.deck[pos2] = temp

    def __str__(self):
        cardStr = ''
        for card in self.deck:
            cardStr += card.__str__() + '\n'
        if len(cardStr) == 0:
            cardStr = 'Deck is empty'
        return cardStr

    def drawCard(self):
        card = self.deck.pop()
        if len(self.deck) == 0:
            self.__populateDeck()
            self.__shuffleDeck()
        return card
    
class Hand(object):

    def __init__(self, deck):
        self.deck = deck
        self.hand = []

    def drawCard(self):
        self.hand.append(deck.drawCard())

    def __str__(self):
        cardStr = ''
        for card in self.hand:
            cardStr += card.__str__() + '\n'
        if len(cardStr) == 0:
            cardStr = 'Hand is empty'
        return cardStr

    def clearHand(self):
        self.hand = []
    
    @property
    def score(self):
        handScore = 0
        for card in self.hand:
            handScore += card.value

        for i in range(self.getNumbOfAces()):
            if handScore > 21:
                handScore -= 10

        return handScore
        
    def getNumbOfAces(self):
        numbOfAces = 0
        for card in self.hand:
            if card.isAce():
                numbOfAces += 1
        return numbOfAces
