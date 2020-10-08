import pygame 
pygame.init ()
screen = pygame.display.set_mode ((800, 600))
run = True
while run:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run=False
    screen.fill ((0,0,0))
    pygame.display.flip ()