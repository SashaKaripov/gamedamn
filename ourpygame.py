import pygame
import random



walk_a_w,walk_a_s,walk_d_s,walk_d_w,walk_a,walk_d,walk_s,walk_w, = [],[],[],[],[],[],[],[]         # Переменные
fight_w,fight_s,fight_a, fight_d,fight_a_w,fight_a_s,fight_d_s,fight_d_w = [],[],[],[],[],[],[],[]
fire = []
clock = pygame.time.Clock()
bg = pygame.image.load("gamedamn\_floor\_flooor.png")
screen = pygame.display.set_mode((800, 600))
walk_off = pygame.image.load("gamedamn\_stay\слой-1.png")
player_anime_count = 0
fire_anime_count = 0
fight_anime_count = 0
fight_anime_count_a = 0
fight_anime_1 = 0
bg_x = 0
repeat_walk_anim = 0
repeat_fight_anim = 0
repeat_fire_anim = 0
player_speed = 5
player_x = 150
player_y = 150
running = True



for i in '12345678':                                                                                # Массивы с покадровой анимацией
    walk_a_w.append(pygame.image.load("gamedamn\_aw\слой-"+i+'.png'))
    walk_a_s.append(pygame.image.load("gamedamn\_as\слой-"+i+'.png'))
    walk_d_s.append(pygame.image.load("gamedamn\ds\слой-"+i+'.png'))
    walk_d_w.append(pygame.image.load("gamedamn\dw\слой-"+i+'.png'))
    walk_a.append(pygame.image.load("gamedamn\_a\слой-"+i+'.png'))
    walk_w.append(pygame.image.load("gamedamn\w\слой-"+i+'.png'))
    walk_d.append(pygame.image.load("gamedamn\d\слой-"+i+'.png'))
    walk_s.append(pygame.image.load("gamedamn\s\слой-"+i+'.png'))
    fight_w.append(pygame.image.load("gamedamn\_fight\w\_"+i+".png"))
    fight_a.append(pygame.image.load("gamedamn\_fight\_a\_"+i+".png"))
    fight_s.append(pygame.image.load("gamedamn\_fight\s\_"+i+".png"))
    fight_d.append(pygame.image.load("gamedamn\_fight\d\_"+i+".png"))
for i in range(16):
    fire.append(pygame.image.load("gamedamn\_fire\слой-"+str(i+1)+'.png'))



while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg, (bg_x, 0))
    keys = pygame.key.get_pressed()



    if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:              # Счётчики задаржки кадров анимации
        repeat_walk_anim += 1
        repeat_fight_anim += 1
    repeat_fire_anim += 1



    for i in [(-70,230),(350,-100),(780,230),(355,560)]:                                          # Анимация огня
        screen.blit(fire[fire_anime_count-1], i)



    if keys[pygame.K_w] and keys[pygame.K_e]:                                                     # Анимация ударов
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



    elif keys[pygame.K_a]:                                                                        # Анимация передвижения
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



    if not(keys[pygame.K_e]):                                                                     # Передвижение
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



    if repeat_walk_anim == 4:                                                                       # Измения счётчиков задержки кадров анимации
        player_anime_count += (1*(player_anime_count != 8)-player_anime_count*(player_anime_count == 8))
        repeat_walk_anim = 0
    if repeat_fight_anim == 6:
        fight_anime_count += (1*(fight_anime_count != 8)-fight_anime_count*(fight_anime_count == 8))
        repeat_fight_anim = 0
    if repeat_fire_anim == 4:
        fire_anime_count += (1*(fire_anime_count != 16)-fire_anime_count*(fire_anime_count == 16))
        repeat_fire_anim = 0
    clock.tick(60)



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gamedamn\_stay\слой-1.png")  # Replace "enemy.png" with the actual enemy model file
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,800), random.randint(0,600))

    def update(self, player):
        # Move the enemy towards the player
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max(abs(dx), abs(dy))
        if distance > 0:
            speed = 2
            self.rect.x += dx * speed / distance
            self.rect.y += dy * speed / distance



all_sprites = pygame.sprite.Group()
spawner_positions = [(800 // 2, 0), (800, 600 // 2),
                    (800 // 2, 600), (0, 600 // 2)]
for position in spawner_positions:
    spawner = Enemy()
    spawner.rect.center = position
    all_sprites.add(spawner)