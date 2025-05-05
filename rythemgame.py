import pygame
import math
from time import sleep
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
moving = [True, True, True]
timer = 0
tsec = [0, 0, 0]
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
                    player_pos = pygame.Vector2(1300, screen.get_height()/2)
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
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
        moving[0] = False
        text = font.render(str(score), True, "black")
        screen.blit(text, textRect)
    if moving[0] == True:
        player_pos.x -= 10
    if moving[1] == True:
        player_pos2.x -= 10
    # flip() the dispay to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    timer = dt + timer
    seconds = math.floor(timer)
    timings = [2,3,5,6]
    for sec in timings:
        if seconds == sec and active[0] == False:
            tsec[0] = seconds + 1
            print("1 active")
            player_pos.x = 1300
            active[0] = True
            pass
        elif active == True and seconds == tsec[0]:
            active[0] = False
            print("1 deactive")
            pass
        if seconds == sec and active[1] == False:
            tsec[1] = seconds + 1
            print("2 active")
            player_pos.x = 1300
            active[1] = True
            pass
        elif active == True and seconds == tsec[1]:
            active[1] = False
            print("2 deactive")
            pass
        
        
    dt = clock.tick(60) / 1000
    

pygame.quit()