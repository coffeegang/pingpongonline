import pygame 
import ball


# init
pygame.init ()
pygame.display.set_caption('PingPongOnline')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
size = weight, height = 1024, 768
screen = pygame.display.set_mode (size)
screen_rect = screen.get_rect()


# objects
all_objects = pygame.sprite.Group()
ball = ball.Ball(weight/2, height/2, screen_rect)
all_objects.add(ball)
run = True


# func for obj drawing
def draw():
    screen.fill ((0,0,0))
    all_objects.draw(screen)

# updating func
def update():
    ball.move()
    pygame.display.flip ()


# main loop
while run:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run=False
    draw()
    update()