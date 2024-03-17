
# Michel Eirene I. Catienza, IT101 M3 FINAL PROJECT
# Game Objects

#=====#=====#=====#=====#=====#=====#=====#=====#=====#

import pygame
from enum import Enum
import random

class Suits(Enum):
  Clubs = 0
  Spades = 1
  Hearts = 2
  Diamonds = 3

class Card:
    suit = None
    value = None
    image = None

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load('images/' + self.suit.name + '/'+ self.suit.name + '_card_' + str(self.value) + '.png')
        self.image = pygame.transform.scale(self.image, (int(238*0.8), int(332*0.8)))

class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for suit in Suits:
            for value in range(1,14):
                self.cards.append(Card(suit,value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def length(self):
        return len(self.cards)

class Pile:
    cards = None

    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None

    def popAll(self):
        return self.cards

    def clear(self):
        self.cards = []

    def isCop(self):
        if len(self.cards) > 1:
            return self.cards[-1].value == self.cards[-2].value
            return False

class Player:
    hand = None
    flipKey = None
    copKey = None
    name = None

    def __init__(self, name, flipKey, copKey):
        self.hand = []
        self.flipKey = flipKey
        self.copKey = copKey
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.deal())

    def play(self):
        return self.hand.pop(0)