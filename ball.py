
import pygame
from pygame.locals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen_rect = screen_rect
        self.speed = [2, 2]
        self.size = [20, 20]
        self.image = pygame.Surface(self.size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    
    def move(self):
        self.check_collide()
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
    

    def check_collide(self):
        if self.rect.left < 0 or self.rect.right > self.screen_rect.right:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom:
            self.speed[1] = -self.speed[1]