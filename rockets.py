import pygame 

class Rockets (pygame.sprite.Sprite):
    def __init__ (self, x, y, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen_rect = screen_rect
        self.size = [10, screen_rect.bottom/5]
        self.image = pygame.Surface(self.size)
        self.image.fill ((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move (self):
        self.check_collide ()
        self.rect.centery = self.y
        
    def check_collide(self):
        if self.rect.top < 0:
            self.rect.y = self.screen_rect.top
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.y = self.screen_rect.bottom
