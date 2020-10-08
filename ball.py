
import pygame
from pygame.locals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen_rect = screen_rect
        self.speed = [1, 1]
        self.size = [20, 20]
        self.image = pygame.Surface(self.size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    

    def move(self, rocket_rect, score):
        self.check_collide(rocket_rect, score)
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
    

    def check_collide(self, rocket_rect, score):
        if self.rect.right > rocket_rect.left and (rocket_rect.top < self.rect.y < rocket_rect.bottom):
            self.speed[0] = -self.speed[0]
        
        if (self.rect.top < rocket_rect.bottom and (rocket_rect.x < self.rect.x < rocket_rect.right)) or (self.rect.bottom < rocket_rect.top and (rocket_rect.x < self.rect.x < rocket_rect.right)):
            self.speed[1] = -self.speed[1]

        if self.rect.x < 0:
            self.speed[0] = -self.speed[0]
            # score[1] += 1
            # self.rect.x, self.rect.y = self.screen_rect.right / 2, self.screen_rect.bottom / 2

        if self.rect.right > self.screen_rect.right:
            score[0] += 1
            self.rect.x, self.rect.y = self.screen_rect.right / 2, self.screen_rect.bottom / 2

        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom:
            self.speed[1] = -self.speed[1]