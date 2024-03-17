
# Michel Eirene I. Catienza, IT101 M3 FINAL PROJECT
# COP THE CARD - A 2 Player Reaction Game
# If you see the "menu.py" file, that was scrapped

#=====#=====#=====#=====#=====#=====#=====#=====#=====#

# MODULES
import pygame
from models import *
from engine import *

pygame.init()
clock = pygame.time.Clock()
gameEngine = CopEngine()

# GAME WINDOW & NAME
borders = (1024, 768)
window = pygame.display.set_mode(borders)
pygame.display.set_caption("COP THE CARD! - a game by Michel Eirene Catienza")

# IMAGES & ASSETS
cardBack = pygame.image.load('images/Backs/back_0.png')
cardBack = pygame.transform.scale(cardBack, (int(138*0.8), int(232*0.8)))

p1 = pygame.image.load('images/player.png')
p1 = pygame.transform.scale(p1, (int(163*0.8), int(157*0.8)))

p2 = pygame.image.load('images/player.png')
p2 = pygame.transform.scale(p1, (int(163*0.8), int(157*0.8)))
p2 = pygame.transform.flip(p2, True, False)

trophy = pygame.image.load('images/gold_trophy.png')
trophy = pygame.transform.scale(trophy, ((173*0.8), int(157*0.8)))

# RENDERING
def renderGame(window):
    window.fill((129,156,141))
    font = pygame.font.Font('NanoPlus.ttf',60)
    titleFont = pygame.font.Font('NanoSquare.ttf', 170)

    window.blit(cardBack, (135, 430))
    window.blit(cardBack, (775, 430))
    window.blit(p1, (-10, 575))
    window.blit(p2, (900, 575))

    titleS = titleFont.render("COP THE CARD!", True, (66, 66, 66))
    window.blit(titleS, (242, -55))
    title = titleFont.render("COP THE CARD!", True, (161, 196, 178))
    window.blit(title, (237, -58))

    text = font.render(str(len(gameEngine.player2.hand)) + " cards", True, (255,255,255))
    window.blit(text, (715, 629))

    text = font.render(str(len(gameEngine.player1.hand)) + " cards", True, (255, 255, 255))
    window.blit(text, (107, 629))

    topCard = gameEngine.pile.peek()
    if (topCard != None):
        window.blit(topCard.image, (400, 250))

    if gameEngine.state == GameState.COPPING:
        clock.tick(30)
        gameEngine.state = GameState.PLAYING

    if gameEngine.state == GameState.PLAYING:
        text = font.render(gameEngine.currentPlayer.name + " to draw", True, (255,255,255))
        window.blit(text, (320,75))

    if gameEngine.state == GameState.ENDED:
        result = gameEngine.result
        message = "Game Over! " + result["winner"].name + " wins!"
        text = font.render(message, True, (255,255,255))
        window.blit(text, (225,75))
        trophy = pygame.image.load('images/gold_trophy.png')
        trophy = pygame.transform.scale(trophy, ((163 * 0.8), int(157 * 0.8)))

        if result["winner"].name == "Player 1":
            trophy = pygame.image.load('images/gold_trophy.png')
            trophy = pygame.transform.scale(trophy, ((60 * 0.8), int(60 * 0.8)))
            window.blit(trophy, (60, 625))


        elif result["winner"].name == "Player 2":
            trophy = pygame.image.load('images/gold_trophy.png')
            trophy = pygame.transform.scale(trophy, ((60 * 0.8), int(60 * 0.8)))
            window.blit(trophy, (915, 625))

# GAME LOOP
run = True
while run:
    key = None;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = event.key

    if gameEngine:
        gameEngine.play(key)
        renderGame(window)

    pygame.display.update()

pygame.quit()