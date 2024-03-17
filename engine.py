
# Michel Eirene I. Catienza, IT101 M3 FINAL PROJECT
# Game logic

#=====#=====#=====#=====#=====#=====#=====#=====#=====#

# MODULES
from enum import Enum
import pygame
from models import *

# ENGINE
class GameState(Enum):
    PLAYING = 0
    COPPING = 1
    ENDED = 2

class CopEngine:
  deck = None
  player1 = None
  player2 = None
  pile = None
  state = None
  currentPlayer = None
  result = None

  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle()
    self.player1 = Player("Player 1", pygame.K_a, pygame.K_s)
    self.player2 = Player("Player 2", pygame.K_k,pygame.K_l)
    self.pile = Pile()
    self.deal()
    self.currentPlayer = self.player1
    self.state = GameState.PLAYING

  def deal(self):
    half = self.deck.length() // 2
    for i in range(0, half):
      self.player1.draw(self.deck)
      self.player2.draw(self.deck)

  def switchPlayer(self):
    if self.currentPlayer == self.player1:
      self.currentPlayer = self.player2
    else:
      self.currentPlayer = self.player1

  def winRound(self, player):
    self.state = GameState.COPPING
    player.hand.extend(self.pile.popAll())
    self.pile.clear()


  def play(self, key):
    if key == None:
        return

    if self.state == GameState.ENDED:
        return

    if key == self.currentPlayer.flipKey and len(self.currentPlayer.hand) > 0:
        self.pile.add(self.currentPlayer.play())
        self.switchPlayer()

    copCaller = None
    nonCopCaller = None
    isCop = self.pile.isCop()

    if (key == self.player1.copKey and len(self.player1.hand) > 0):
        copCaller = self.player1
        nonCopCaller = self.player2
    elif (key == self.player2.copKey and len(self.player2.hand) > 0):
        copCaller = self.player2
        nonCopCaller = self.player1

    if isCop and copCaller:
        self.winRound(copCaller)
        self.result = {
            "winner": copCaller,
            "isCop": True,
            "copCaller": copCaller
        }
        self.winRound(copCaller)

    elif not isCop and copCaller:
        self.result= {
            "winner": nonCopCaller,
            "isCop": False,
            "copCaller": copCaller
        }
        self.winRound(nonCopCaller)
        self.state = GameState.COPPING

    if len(self.player1.hand) == 0:
        self.result = {
            "winner": self.player2,
        }
        self.state = GameState.ENDED
    elif len(self.player2.hand) == 0:
        self.result = {
            "winner": self.player1,
        }
        self.state = GameState.ENDED
