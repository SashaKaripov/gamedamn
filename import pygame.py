import pygame
clock = pygame.time.Clock()
bg = pygame.image.load("project\_floor\_flooor.png")
screen = pygame.display.set_mode((800, 600))
walk_a_w,walk_a_s,walk_d_s,walk_d_w,walk_a,walk_d,walk_s,walk_w, = [],[],[],[],[],[],[],[]
fire = []
fight_w,fight_s,fight_a, fight_d,fight_a_w,fight_a_s,fight_d_s,fight_d_w = [],[],[],[],[],[],[],[]
for i in '12345678':
    for r in range(4):
        walk_a_w.append(pygame.image.load("project\_aw\слой-"+i+'.png'))
        walk_a_s.append(pygame.image.load("project\_as\слой-"+i+'.png'))
        walk_d_s.append(pygame.image.load("project\ds\слой-"+i+'.png'))
        walk_d_w.append(pygame.image.load("project\dw\слой-"+i+'.png'))
        walk_a.append(pygame.image.load("project\_a\слой-"+i+'.png'))
        walk_w.append(pygame.image.load("project\w\слой-"+i+'.png'))
        walk_d.append(pygame.image.load("project\d\слой-"+i+'.png'))
        walk_s.append(pygame.image.load("project\s\слой-"+i+'.png'))
    for r in range(6):
        fight_w.append(pygame.image.load("project\_fight\w\_"+i+".png"))
        fight_a.append(pygame.image.load("project\_fight\_a\_"+i+".png"))
        fight_s.append(pygame.image.load("project\_fight\s\_"+i+".png"))
        fight_d.append(pygame.image.load("project\_fight\d\_"+i+".png"))
for i in range(16):
    for r in range(4):
        fire.append(pygame.image.load("project\_fire\слой-"+str(i+1)+'.png'))
walk_off = pygame.image.load("project\stay\слой-1.png")
player_anime_count = 0
fire_anime_count = 0
fight_anime_count = 0
fight_anime_count_a = 0
fight_anime_1 = 0
bg_x = 0
ff = 0
player_speed = 5
player_x = 150
player_y = 150
is_jump = False
jump_count = 5
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg, (bg_x, 0))
    for i in [(-70,230),(350,-100),(780,230),(355,560)]:
        
        screen.blit(fire[fire_anime_count-1], i)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and keys[pygame.K_e]:
        if fight_anime_1 < 15:
            screen.blit(fight_w[0], (player_x, player_y))
        else:
            screen.blit(fight_w[fight_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_a] and keys[pygame.K_e]:
        if fight_anime_1 < 15:
            screen.blit(fight_a[0], (player_x, player_y))
        else:
            screen.blit(fight_a[fight_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_s] and keys[pygame.K_e]:
        if fight_anime_1 < 15:
            screen.blit(fight_s[0], (player_x, player_y))
        else:
            screen.blit(fight_s[fight_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_d] and keys[pygame.K_e]:
        if fight_anime_1 < 15:
            screen.blit(fight_d[0], (player_x, player_y))
        else:
            screen.blit(fight_d[fight_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_a]:
        screen.blit(walk_a[player_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_d]:
        screen.blit(walk_d[player_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_w]:
        screen.blit(walk_w[player_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_s]:
        screen.blit(walk_s[player_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_w] and keys[pygame.K_a]:
        screen.blit(walk_a_w[player_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        screen.blit(walk_d_w[player_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        screen.blit(walk_a_s[player_anime_count-1], (player_x, player_y))
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        screen.blit(walk_d_s[player_anime_count-1], (player_x, player_y))
    else:
        screen.blit(walk_off, (player_x, player_y))

    if not(keys[pygame.K_e]):
        fight_anime_count = 0
        fight_anime_1 = 0
        if keys[pygame.K_a] and keys[pygame.K_w] and player_x > 40 and player_y > 40:
            player_x -= player_speed/(2**0.5)
            player_y -= player_speed/(2**0.5)
        elif keys[pygame.K_d] and keys[pygame.K_w] and player_x < 710 and player_y > 40:
            player_x += player_speed/(2**0.5)
            player_y -= player_speed/(2**0.5)
        elif keys[pygame.K_a] and keys[pygame.K_s] and player_y < 510 and player_x > 40:
            player_x -= player_speed/(2**0.5)
            player_y += player_speed/(2**0.5)
        elif keys[pygame.K_d] and keys[pygame.K_s] and player_y < 510 and player_x < 710:
            player_x += player_speed/(2**0.5)
            player_y += player_speed/(2**0.5)
        elif keys[pygame.K_a] and player_x > 40:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < 710:
            player_x += player_speed
        elif keys[pygame.K_w] and player_y > 40:
            player_y -= player_speed
        elif keys[pygame.K_s] and player_y < 510:
            player_y += player_speed
    else:
        fight_anime_1+=1

    player_anime_count += (1*(player_anime_count != 32)-player_anime_count*(player_anime_count == 32))
    fight_anime_count += (1*(fight_anime_count != 48)-fight_anime_count*(fight_anime_count == 48))
    fire_anime_count += (1*(fire_anime_count != 64)-fire_anime_count*(fire_anime_count == 64))

    clock.tick(60)