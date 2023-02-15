import pygame

class bird(pygame.sprite.Sprite):
    def __init__(self, x, y,imgs):
        super().__init__()
        self.Original_x = x
        self.Original_y = y
        self.images = imgs
        self.images_index = 0
        # self.image = imgs
        self.image = self.images[self.images_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.dy = 0
        self.vy = 0
        self.ay = 0.5
        self.click = -10
        self.last_pic_time = pygame.time.get_ticks()
        self.img_freq = 200
        self.fly = True
        self.rect.topright = (x,y)

    def update(self,button_input,ground_top):
        if self.fly:

            now = pygame.time.get_ticks()
            if now - self.last_pic_time > self.img_freq:
                self.images_index +=1
                if self.images_index >= len(self.images):
                    self.images_index = 0
                self.image = self.images[self.images_index]
                self.last_pic_time = now

        self.rect.y += self.vy
        self.vy += self.ay
        if button_input == True:
            self.vy += self.click

        if self.rect.bottom >= ground_top:
            self.rect.bottom = ground_top

    def lose(self):
        self.fly = False
        self.image = pygame.transform.rotate(self.images[self.images_index],-90)
    def reset(self):
        self.images_index = 0
        self.image = self.images[self.images_index]
        self.rect = self.image.get_rect()
        self.rect.center = (self.Original_x, self.Original_y)
        self.vy = 0
        self.last_pic_time = pygame.time.get_ticks()
        self.fly = True


