import pygame
from pygame.locals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen_rect = screen_rect
        self.speed = [1, 1]
        self.dir = [1, 1]
        self.size = [20, 20]
        self.image = pygame.Surface(self.size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    

    def move(self, rocket_rects, score):
        self.check_collide(rocket_rects, score)
        self.rect.x += self.speed[0] * self.dir[0]
        self.rect.y += self.speed[1] * self.dir[1]
    

    def check_collide(self, rocket_rects, score):
        if self.rect.right > rocket_rects[0].left and (rocket_rects[0].top < self.rect.y < rocket_rects[0].bottom):
            self.dir[0] = -self.dir[0]
        
        if self.rect.left < rocket_rects[1].right and (rocket_rects[1].top < self.rect.y < rocket_rects[1].bottom):
            self.dir[0] = -self.dir[0]



        if self.rect.x < 0:
            score[1] += 1
            self.rect.x, self.rect.y = self.screen_rect.right / 2, self.screen_rect.bottom / 2

        if self.rect.right > self.screen_rect.right:
            score[0] += 1
            self.rect.x, self.rect.y = self.screen_rect.right / 2, self.screen_rect.bottom / 2

        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom:
            self.dir[1] = -self.dir[1]
        

