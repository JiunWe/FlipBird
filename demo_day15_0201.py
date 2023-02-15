import pygame
from Bird import bird
from pipe import pipe
import random
WIDTH =780
HEIGHT = 480
FPS = 45
pipe_freq = 1500
score = 0
last_pipe_time = pygame.time.get_ticks()-pipe_freq
game_over = False



def generate_pipe(last_pipe_time, pipe_freq, pipe_group):
    now = pygame.time.get_ticks()
    if now - last_pipe_time >= pipe_freq:
        rand_parameter = random.randint(-100,100)
        Pipe_bot = pipe(pipe_img, WIDTH, 5 * HEIGHT / 8 + rand_parameter, True, 4)
        Pipe_top = pipe(flip_slip, WIDTH, 3*HEIGHT / 8 + rand_parameter, False, 4)
        pipe_group.add(Pipe_bot)
        pipe_group.add(Pipe_top)
        return now
    return last_pipe_time

# def lose(img,s_top,s_bot):
#     if img

ground_x = 0
ground_speed = 4
pygame.init()
font = pygame.font.Font("微軟正黑體.ttf", 50)
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("你要不要玩我的小鳥")
clock = pygame.time.Clock()

bg_img = pygame.image.load("../img/bg.png")
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

bird_imgs = []
for i in range(1,3):
    bird_imgs.append(pygame.image.load(f'../img/bird{i}.png'))
ground_img = pygame.image.load("../img/ground.png")
pipe_img = pygame.image.load("../img/pipe.png")
restart_img = pygame.image.load("../img/restart.png")
flip_slip = pygame.transform.flip(pipe_img,False,True)
flip_bird = pygame.transform.flip(bird_imgs[0],True,False)

Birdd =bird(70, HEIGHT/2,bird_imgs)
bird_group = pygame.sprite.Group()
bird_group.add(Birdd)



# Pipe_bot = pipe(pipe_img,WIDTH, 3*HEIGHT/4,True,4)
# Pipe_top = pipe(flip_slip,WIDTH, 1*HEIGHT/4,False,4)
pipe_group = pygame.sprite.Group()
# pipe_sprite.add(Pipe_bot)
# pipe_sprite.add(Pipe_top)

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1 and not game_over:
                 bird_group.update(True, HEIGHT - 50)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                last_pipe_time = pygame.time.get_ticks() - pipe_freq
                score = 0
                Birdd.reset()
                for pipee in pipe_group.sprites():
                    pipee.kill()

                # bird_group.sprites()[0].rect.y = HEIGHT/2
                # pipe_group.__init__()
                # score = 0
                # game_over = False


    text_1 = font.render(str(score), True, (0, 0, 0))

    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or\
        Birdd.rect.top<=0 or\
        Birdd.rect.bottom >= HEIGHT - 50:
        game_over = True
        Birdd.lose()

    #畫面更新
    bird_group.update(False, HEIGHT - 50)
    window.blit(bg_img, (0,0))
    bird_group.draw(window)

    if game_over == False:
        last_pipe_time = generate_pipe(last_pipe_time, pipe_freq, pipe_group)
        pipe_group.update()

        ground_x -= ground_speed
        if ground_x<=-900:
            ground_x = 0
        first_pipe = pipe_group.sprites()[0]
        if not first_pipe.pipe_pass:
            if Birdd.rect.left > first_pipe.rect.right:
                score += 1
                first_pipe.pipe_pass = True



    pipe_group.draw(window)
    window.blit(ground_img, (ground_x+900, HEIGHT - 50))
    window.blit(ground_img, (ground_x, HEIGHT-50))
    window.blit(text_1, (WIDTH / 2, HEIGHT / 10))
    if game_over:
        window.blit(restart_img, (WIDTH/2 - restart_img.get_width()/2, HEIGHT/2 - restart_img.get_height()/2))
    pygame.display.update()
pygame.quit()