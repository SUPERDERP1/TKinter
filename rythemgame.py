import pygame
import math
from time import sleep
import pygameGUI
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
score = 0
font = pygame.font.Font('HelveticaNeue.ttc', 32)
text = font.render(str(score), True, "black")
textRect = text.get_rect()
textRect.center = (200, 100)
player_pos = pygame.Vector2(1300, screen.get_height() / 2)
player_pos2 = pygame.Vector2(1300, screen.get_height() / 2)
active = [False, False, False]
timer = 0
menuActive = True
all_sprites = pygame.sprite.Group()
fontA = pygame.font.Font('HelveticaNeue.ttc', 70)
squareWidth = 40
menu = pygameGUI.Menu("Start Game", "white", fontA, 500, 600, image= None, pos=(100,60))
startB = pygameGUI.Text("Start", fontA, (255, 255, 255), (640, 450))
quitB = pygameGUI.Text("Quit", fontA, (255, 255, 255)) 
all_sprites.add(quitB)
all_sprites.add(startB)
menu.add(startB)
menu.add(quitB)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:     
            pos = pygame.mouse.get_pos()     
            clickedSprites = [s for s in all_sprites if s.rect.collidepoint(pos)]    

            if startB in clickedSprites:
                menuActive = False

            if quitB in clickedSprites: #quits the game when the quit button is clicked
                running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE: 

                if rect.colliderect(circle):
                    player_pos = pygame.Vector2(1300, screen.get_height() / 2)
                    score += 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)

                else:
                    score -= 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
                    testX = 100 

                    if player_pos.x < player_pos2.x:
                        player_pos.x = 1300
                        active[0] = False

                    else:
                        player_pos2.x = 1300
                        active[1] = False

    if not menuActive:

        screen.fill("white")


        missrect = pygame.Rect(1, 0, 5, 720)
        circle = pygame.draw.circle(screen, "red", player_pos, 40)
        circle2 = pygame.draw.circle(screen, "red", player_pos2, 40)
        rect = pygame.Rect(100, 0, 5, 720)
        pygame.draw.rect(screen, "blue", rect)
        screen.blit(text, textRect)


        if missrect.colliderect(circle):
            score -= 1
            player_pos = pygame.Vector2(1300, screen.get_height()/2)
            active[0] = False
            text = font.render(str(score), True, "black")
            screen.blit(text, textRect)

        if missrect.colliderect(circle2):
            score -= 1
            player_pos2 = pygame.Vector2(1300, screen.get_height()/2)
            active[1] = False
            text = font.render(str(score), True, "black")
            screen.blit(text, textRect)

        if active[0] == True:
            player_pos.x -= 10

        if active[1] == True:
            player_pos2.x -= 10


        # flip() the dispay to put your work on screen
        pygame.display.flip()


        timer = dt + timer
        seconds = math.floor(timer)
        timings = [6,7,10,11]

        for sec in timings:
            if seconds == sec and active[0] == False:
                print("1 active")
                player_pos.x = 1300
                active[0] = True
                exit = True
            
            elif seconds == sec and active[1] == False:
                print("2 active")
                player_pos.x = 1300
                active[1] = True
                exit = True
            #not breaking loop is problem
        dt = clock.tick(60) / 1000
    else:
        screen.fill("white")
        menu.draw(screen) 
        pygame.display.flip() 

pygame.quit()