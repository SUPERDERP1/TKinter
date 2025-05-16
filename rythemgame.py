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
# text object
score = 0
font = pygame.font.Font('HelveticaNeue.ttc', 32)
text = font.render(str(score), True, "black")
textRect = text.get_rect()
textRect.center = (200, 100)
# note pos
player_pos = pygame.Vector2(1400, 240)
player_pos2 = pygame.Vector2(1400, 240)
bplayer_pos = pygame.Vector2(1400, 480)
bplayer_pos2 = pygame.Vector2(1400, 480)
active = [False, False, False, False]
# timer 
timer = 0
# menu variables
menuActive = True
all_sprites = pygame.sprite.Group()
fontA = pygame.font.Font('HelveticaNeue.ttc', 70)
fontB = pygame.font.Font('HelveticaNeue.ttc', 35)
squareWidth = 40
# menu declaration
menu = pygameGUI.Menu("Start Game", "white", fontA, 500, 600, image= None, pos=(100,60))
startB = pygameGUI.Text("Start", fontA, (255, 255, 255), (640, 450))
quitB = pygameGUI.Text("Quit", fontA, (255, 255, 255)) 
helpL = pygameGUI.Text("Press F to hit Red Notes", fontB, (255, 255, 255), (640, 600))
helpL2 = pygameGUI.Text("Press J to hit Blue Notes", fontB, (255, 255, 255), (640, 600))
# adding sprites to menu
all_sprites.add(quitB)
all_sprites.add(startB)
all_sprites.add(helpL)
all_sprites.add(helpL2)
menu.add(startB)
menu.add(quitB)
menu.add(helpL)
menu.add(helpL2)
# beat timings
timings = [4,4.5]
btimings = [5,5.75]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # menu click detection
        if event.type == pygame.MOUSEBUTTONUP:     
            pos = pygame.mouse.get_pos()     
            clickedSprites = [s for s in all_sprites if s.rect.collidepoint(pos)]    

            if startB in clickedSprites:
                menuActive = False

            if quitB in clickedSprites: #quits the game when the quit button is clicked
                running = False
        # on key press
        if event.type == pygame.KEYDOWN:
            # if keypress is f
            if event.key == pygame.K_f and not menuActive: 
                # if in hit zone detection
                if rect.colliderect(circle):
                    player_pos.xy = 1400, 240
                    score += 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
                    active[0] = False

                elif rect.colliderect(circle2):
                    player_pos2.xy = 1400,240
                    score += 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
                    active[1] = False
                # Not in hit zone logic
                else:
                    score -= 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
                    testX = 100 

                    if player_pos.x < player_pos2.x:
                        player_pos.x = 1400
                        active[0] = False

                    else:
                        player_pos2.x = 1400
                        active[1] = False
            # if j key pressed
            if event.key == pygame.K_j and menuActive: 
                # collision detection
                if rect.colliderect(bcircle):
                    bplayer_pos.xy = 1400, 480
                    score += 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
                    active[2] = False

                elif rect.colliderect(bcircle2):
                    bplayer_pos2.xy = 1400, 480
                    score += 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
                    active[3] = False
                # not in hit zone logic
                else:
                    score -= 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
                    testX = 100 

                    if bplayer_pos.x < bplayer_pos2.x:
                        bplayer_pos.x = 1400
                        active[2] = False

                    else:
                        bplayer_pos2.x = 1400
                        active[3] = False

    # non-menu logic
    if not menuActive:
        #remove old 
        screen.fill("#cdcdcd")


        missrect = pygame.Rect(1, 0, 5, 720)
        circle = pygame.draw.circle(screen, "red", player_pos, 40)
        circle2 = pygame.draw.circle(screen, "red", player_pos2, 40)
        bcircle = pygame.draw.circle(screen, "blue", bplayer_pos, 40)
        bcircle2 = pygame.draw.circle(screen, "blue", bplayer_pos2, 40)
        rect = pygame.Rect(100, 0, 5, 720)
        pygame.draw.rect(screen, "purple", rect)
        screen.blit(text, textRect)


        if missrect.colliderect(circle):
            score -= 1
            player_pos = pygame.Vector2(1400, 240)
            active[0] = False
            text = font.render(str(score), True, "black")
            screen.blit(text, textRect)

        if missrect.colliderect(circle2):
            score -= 1
            player_pos2 = pygame.Vector2(1400, 240)
            active[1] = False
            text = font.render(str(score), True, "black")
            screen.blit(text, textRect)

        if missrect.colliderect(bcircle):
            score -= 1
            bplayer_pos = pygame.Vector2(1400, 480)
            active[2] = False
            text = font.render(str(score), True, "black")
            screen.blit(text, textRect)

        if missrect.colliderect(bcircle2):
            score -= 1
            bplayer_pos2 = pygame.Vector2(1400, 480)
            active[3] = False
            text = font.render(str(score), True, "black")
            screen.blit(text, textRect)

        if active[0] == True:
            player_pos.x -= 10

        if active[1] == True:
            player_pos2.x -= 10
        
        if active[2] == True:
            bplayer_pos.x -= 10
        
        if active[3] == True:
            bplayer_pos2.x -= 10

        # flip() the dispay to put your work on screen
        pygame.display.flip()


        timer = dt + timer
        seconds = round(timer, 2)

        for sec in timings:
            print(timings)
            if seconds == sec and active[0] == False:
                print("1 active ")
                player_pos.xy = 1400, 240
                active[0] = True
                del timings[0]

            elif seconds == sec and active[1] == False:
                player_pos2.xy = 1400, 240
                active[1] = True
                del timings[0]

        for sec in btimings:
            if seconds == sec and active[2] == False:
                bplayer_pos.xy = 1400, 480
                active[2] = True
                del btimings[0]

            elif seconds == sec and active[3] == False:
                bplayer_pos2.xy = 1400, 480
                active[3] = True
                del btimings[0]

        dt = clock.tick(60) / 1000
    else:
        screen.fill("white")
        menu.draw(screen) 
        pygame.display.flip() 
pygame.quit()