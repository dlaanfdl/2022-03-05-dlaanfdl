import pygame

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

xpos = 0
ypos = SCREEN_HEIGHT


xspeed = SCREEN_WIDTH * 0.0001
yspeed = SCREEN_HEIGHT * -0.0001


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((30, 150, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 60)

    xpos = xpos + xspeed
    ypos = ypos + yspeed

    pygame.display.update()
