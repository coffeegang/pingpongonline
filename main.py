import pygame 
import ball
import rockets
import time

# init
pygame.init ()
pygame.display.set_caption('PingPongOnline')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
size = weight, height = 1024, 768
screen = pygame.display.set_mode (size)
screen_rect = screen.get_rect()
run = True


# objects
all_objects = pygame.sprite.Group()
ball = ball.Ball(weight/2, height/2, screen_rect)
rocket_right = rockets.Rockets (weight - 30, height/2, screen_rect)
all_objects.add (ball, rocket_right)
score = [0, 0]


# func for obj drawing
def draw(): 
    screen.fill ((0,0,0))
    all_objects.draw(screen)
    draw_text(screen, str(score[0]), 20, screen_rect.right/2, 5)
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# updating func
def update():
    ball.move(rocket_right.rect, score)
    rocket_right.move()
    pygame.display.flip ()


# main loop
while run:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos([1])
            rocket_right.y = pos[1]

    draw()
    update()
    