import pygame

pygame.init()

SCREEN_WIDTH = 340
SCREEN_HEIGHT = 720

xpos = SCREEN_WIDTH/2
ypos = 0

yspeed = 0.001

gravity = 0.0001


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((70, 150, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    yspeed += gravity
    ypos += yspeed

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 20)

    pygame.display.update()
