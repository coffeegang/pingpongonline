import pygame 
pygame.init ()
pygame.display.set_caption('PingPongOnline')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
size = weight, height = 1024, 768
screen = pygame.display.set_mode (size)
run = True
while run:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run=False
    screen.fill ((0,0,0)) 
    pygame.display.flip ()