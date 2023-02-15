import pygame

class pipe(pygame.sprite.Sprite):
    def __init__(self,img,x,y,state,speedx):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speedx = speedx
        self.pipe_pass = False
        if state == True:
            self.rect.topleft = (self.x, self.y)
        else:
            self.rect.bottomleft = (self.x, self.y)

    
    def update(self):
        self.rect.x-= self.speedx
        if self.rect.right < 0:
            self.kill()