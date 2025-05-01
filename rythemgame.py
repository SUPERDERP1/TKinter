import pygame
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
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
active = True
def quadbeat1():
    player_pos.x = 1100
    
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if rect.colliderect(circle):
                    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                    score += 1
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
                else:
                    score -= 1
                    player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
                    text = font.render(str(score), True, "black")
                    screen.blit(text, textRect)
    screen.fill("white")
    missrect = pygame.Rect(1, 0, 5, 720)
    circle = pygame.draw.circle(screen, "red", player_pos, 40)
    rect = pygame.Rect(100, 0, 5, 720)
    pygame.draw.rect(screen, "blue", rect)
    screen.blit(text, textRect)
    if missrect.colliderect(circle):
        score -= 1
        player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
        text = font.render(str(score), True, "black")
        screen.blit(text, textRect)
    # flip() the dispay to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    quadbeat1()

pygame.quit()