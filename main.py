import pygame 
import ball
import rockets
import ai

# init
pygame.init ()
pygame.display.set_caption('PingPongOnline')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
size = width, height = 1024, 768
screen = pygame.display.set_mode (size)
screen_rect = screen.get_rect()
run = True
font_name = pygame.font.match_font('arial')


# objects
all_objects = pygame.sprite.Group()
ball = ball.Ball(width/2, height/2, screen_rect)
rocket_right = rockets.Rockets (width - 30, height/2, screen_rect)
rocket_left = rockets.Rockets(30, height/2, screen_rect)
AI = ai.AI(rocket_left, ball)
all_objects.add (ball, rocket_right, rocket_left)
score = [0, 0]


# func for obj drawing
def draw(): 
    screen.fill ((0,0,0))
    all_objects.draw(screen)
    draw_text(screen, str(score[0]), 20, screen_rect.right/2, 5)


# drawing text
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# updating func
def update():
    ball.move([rocket_right.rect, rocket_left.rect], score)
    rocket_right.move()
    AI.move()
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
    