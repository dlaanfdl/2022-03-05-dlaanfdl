import pygame

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

xpos = SCREEN_WIDTH/2
ypos = SCREEN_HEIGHT/2


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((70, 150, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 60)

    pygame.display.update()
