import pygame
import sys
pygame.display.set_caption("the Game")


class Enemy:
    def __init__(self, enemy_pos_x, enemy_pos_y, alive):
        self.image_l = []
        self.image_r = []
        self.image_u = []
        self.image_d = []
        self.image_die = []
        self.enemy_fight_l = []
        self.enemy_fight_r = []
        self.health_anim_count = 0
        self.enemy_anim_count = 0
        self.enemy_fight_anim_count = 0
        self.anim_die_count = 0
        self.repeat_anim_fight = 0
        self.repeat_anim_die = 0
        self.repeat_enemy_anim = 0
        self.enemy_pos_x = enemy_pos_x
        self.enemy_pos_y = enemy_pos_y
        self.alive = alive

    def movement_plus_anim_enemys(self):
        if self.alive == 1:
            if not (abs(self.enemy_pos_x - player_x) <= 25 and abs(self.enemy_pos_y - player_y) <= 50):
                if -70 <= player_x - self.enemy_pos_x <= 70 and self.enemy_pos_y - player_y > 50:
                    screen.blit(self.image_u[self.enemy_anim_count], (self.enemy_pos_x, self.enemy_pos_y))

                elif -70 <= player_x - self.enemy_pos_x <= 70 and player_y - self.enemy_pos_y > 50:
                    screen.blit(self.image_d[self.enemy_anim_count], (self.enemy_pos_x, self.enemy_pos_y))

                elif self.enemy_pos_x <= player_x:
                    screen.blit(self.image_r[self.enemy_anim_count], (self.enemy_pos_x, self.enemy_pos_y))
                    self.enemy_pos_x += 3 / (2 ** 0.5)
                else:
                    screen.blit(self.image_l[self.enemy_anim_count], (self.enemy_pos_x, self.enemy_pos_y))
                    self.enemy_pos_x -= 3 / (2 ** 0.5)

                if self.enemy_pos_y <= player_y:
                    self.enemy_pos_y += 3 / (2 ** 0.5)
                else:
                    self.enemy_pos_y -= 3 / (2 ** 0.5)

                if self.repeat_enemy_anim == 4:
                    self.enemy_anim_count += (
                                1 * (self.enemy_anim_count != 7) - self.enemy_anim_count * (self.enemy_anim_count == 7))
                    self.repeat_enemy_anim = 0
                self.repeat_enemy_anim += 1

            else:
                if self.enemy_pos_x <= player_x:
                    screen.blit(self.enemy_fight_r[self.enemy_fight_anim_count], (self.enemy_pos_x, self.enemy_pos_y))

                if self.enemy_pos_x > player_x:
                    screen.blit(self.enemy_fight_l[self.enemy_fight_anim_count], (self.enemy_pos_x, self.enemy_pos_y))

                if self.repeat_anim_fight == 4:
                    self.enemy_fight_anim_count += (
                                1 * (self.enemy_fight_anim_count != 5) - self.enemy_fight_anim_count * (
                                    self.enemy_fight_anim_count == 5))
                    self.repeat_anim_fight = 0
                self.repeat_anim_fight += 1

                if self.repeat_anim_fight == 3 and self.enemy_fight_anim_count == 4:
                    self.health_anim_count += 1
        else:
            if self.anim_die_count != 4:
                screen.blit(self.image_die[self.anim_die_count], (self.enemy_pos_x, self.enemy_pos_y))
                if self.repeat_anim_die == 4:
                    self.anim_die_count += (
                                1 * (self.anim_die_count != 4) - self.anim_die_count * (self.anim_die_count == 4))
                    self.repeat_anim_die = 0
                self.repeat_anim_die += 1
            else:
                screen.blit(self.image_die[self.anim_die_count], (self.enemy_pos_x, self.enemy_pos_y))

    def enemy_poss(self):
        return self.enemy_pos_x, self.enemy_pos_y


def wave_enemy_alive(enemys, sum=0):
    for enemy in enemys:
        sum += enemy.alive
    return sum


def allow_move(player_x, player_y):  # Врезается ли игрок во врага
    if wave != 5:
        for enemy in enemys4:
            if 0 < enemy.enemy_pos_y - player_y <= 70 and abs(enemy.enemy_pos_x - player_x) <= 30:
                return 3
            if 0 < player_y - enemy.enemy_pos_y <= 70 and abs(enemy.enemy_pos_x - player_x) <= 30:
                return 1
            if abs(player_y - enemy.enemy_pos_y) <= 30 and 0 < player_x - enemy.enemy_pos_x <= 50:
                return 2
            if abs(player_y - enemy.enemy_pos_y) <= 30 and 0 < enemy.enemy_pos_x - player_x <= 50:
                return 4
            return 5


def movement_body_box(enemys):  # Столкновение врагов
    for i in range(len(enemys) - 1):
        for j in range(i + 1, len(enemys)):
            if abs(enemys[j].enemy_pos_x - enemys[i].enemy_pos_x) <= 25 and abs(
                    enemys[j].enemy_pos_y - enemys[i].enemy_pos_y) <= 50:
                enemys[i].enemy_pos_y += 1
                enemys[i].enemy_pos_x += 1
                enemys[j].enemy_pos_y -= 1
                enemys[j].enemy_pos_x -= 1

window_width = 800
window_height = 600
window_size = (window_width, window_height)

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game Menu")

# Создание меню
background_image = pygame.image.load("gamedamn\menubg\menu.jpg")
play_button_image = pygame.image.load("gamedamn\menubuttons\play_250x62.png")
quit_button_image = pygame.image.load("gamedamn\menubuttons\quit_250x62.png")
play_button_pos = (window_width // 2 - play_button_image.get_width() // 2, 300)
quit_button_pos = (window_width // 2 - quit_button_image.get_width() // 2, 400)

# Game loop
running = True
while running:
    window.fill((0, 0, 0))
    window.blit(background_image, (0, 0))
    window.blit(play_button_image, play_button_pos)
    window.blit(quit_button_image, quit_button_pos)
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button_pos[0] <= mouse_pos[0] <= play_button_pos[0] + play_button_image.get_width() and \
                    play_button_pos[1] <= mouse_pos[1] <= play_button_pos[1] + play_button_image.get_height():
                running = True  # Переменные
                walk_a_w, walk_a_s, walk_d_s, walk_d_w, walk_a, walk_d, walk_s, walk_w, = [], [], [], [], [], [], [], []
                fight_w, fight_s, fight_a, fight_d, fight_a_w, fight_a_s, fight_d_s, fight_d_w = [], [], [], [], [], [], [], []
                healthbar = []
                health_arr = []
                fire = []
                clock = pygame.time.Clock()
                spawn_time = pygame.time.get_ticks()
                bg = pygame.image.load("gamedamn\_floor\_flooor.png")
                dark = pygame.image.load("gamedamn\_floor\_123.png")
                screen = pygame.display.set_mode((800, 600))
                walk_off = pygame.image.load("gamedamn\_stay\слой-1.png")
                player_anime_count = 0
                fire_anime_count = 0
                dark_count = 0
                fight_anime_count = 0
                fight_anime_1 = 0
                repeat_walk_anim = 0
                repeat_fight_anim = 0
                repeat_fire_anim = 0
                wave = 1
                player_speed = 5
                player_x = 380
                player_y = 280
                running = True

                enemy1 = Enemy(-100, 300, 1)  # Made the enemy
                enemy2 = Enemy(800, 300, 1)
                enemy3 = Enemy(400, -100, 1)
                enemy4 = Enemy(400, 700, 1)
                enemy5 = Enemy(-100, 300, 1)
                enemy6 = Enemy(800, 300, 1)
                enemy7 = Enemy(400, -100, 1)
                enemy8 = Enemy(400, 700, 1)
                enemys1 = [enemy1]
                enemys2 = [enemy1, enemy2]
                enemys3 = [enemy1, enemy2, enemy3, enemy4]
                enemys4 = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]

                for i in '12345678':  # Массивы с покадровой анимацией
                    walk_a_w.append(pygame.image.load("gamedamn\_aw\слой-" + i + '.png'))
                    walk_a_s.append(pygame.image.load("gamedamn\_as\слой-" + i + '.png'))
                    walk_d_s.append(pygame.image.load("gamedamn\ds\слой-" + i + '.png'))
                    walk_d_w.append(pygame.image.load("gamedamn\dw\слой-" + i + '.png'))
                    walk_a.append(pygame.image.load("gamedamn\_a\слой-" + i + '.png'))
                    walk_w.append(pygame.image.load("gamedamn\w\слой-" + i + '.png'))
                    walk_d.append(pygame.image.load("gamedamn\d\слой-" + i + '.png'))
                    walk_s.append(pygame.image.load("gamedamn\s\слой-" + i + '.png'))
                    fight_w.append(pygame.image.load("gamedamn\_fight\w\_" + i + ".png"))
                    fight_a.append(pygame.image.load("gamedamn\_fight\_a\_" + i + ".png"))
                    fight_s.append(pygame.image.load("gamedamn\_fight\s\_" + i + ".png"))
                    fight_d.append(pygame.image.load("gamedamn\_fight\d\_" + i + ".png"))
                    if i != '8' and i != '7' and i != '6':
                        healthbar.append(pygame.image.load("gamedamn\healthbar\_" + i + '.png'))
                    for enemy in enemys4:
                        enemy.image_l.append(pygame.image.load("gamedamn\enemy\_a\слой-" + i + '.png'))
                        enemy.image_r.append(pygame.image.load("gamedamn\enemy\d\слой-" + i + '.png'))
                        enemy.image_u.append(pygame.image.load("gamedamn\enemy\w\_" + i + '.png'))
                        enemy.image_d.append(pygame.image.load("gamedamn\enemy\s\_" + i + '.png'))
                        if i != '8' and i != '7' and i != '6':
                            enemy.image_die.append(pygame.image.load("gamedamn\enemy\dyin\_" + i + '.png'))
                        if i != '8' and i != '7':
                            enemy.enemy_fight_l.append(pygame.image.load("gamedamn\enemy\_fight_l\_" + i + '.png'))
                            enemy.enemy_fight_r.append(pygame.image.load("gamedamn\enemy\_fight_r\_" + i + '.png'))
                for i in range(16):
                    fire.append(pygame.image.load("gamedamn\_fire\слой-" + str(i + 1) + '.png'))

                while running:
                    pygame.display.update()  # Stratin settings
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    screen.blit(bg, (0, 0))
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[
                        pygame.K_d]:  # Счётчики задаржки кадров анимации
                        repeat_walk_anim += 1
                        repeat_fight_anim += 1
                    repeat_fire_anim += 1

                    for i in [(-70, 230), (350, -100), (780, 230), (355, 560)]:  # Анимация огня
                        screen.blit(fire[fire_anime_count], i)

                    if keys[pygame.K_w] and keys[pygame.K_e]:  # Анимация ударов
                        if fight_anime_1 < 15:
                            screen.blit(fight_w[0], (player_x, player_y))
                        else:
                            screen.blit(fight_w[fight_anime_count], (player_x, player_y))
                    elif keys[pygame.K_a] and keys[pygame.K_e]:
                        if fight_anime_1 < 15:
                            screen.blit(fight_a[0], (player_x, player_y))
                        else:
                            screen.blit(fight_a[fight_anime_count], (player_x, player_y))
                    elif keys[pygame.K_s] and keys[pygame.K_e]:
                        if fight_anime_1 < 15:
                            screen.blit(fight_s[0], (player_x, player_y))
                        else:
                            screen.blit(fight_s[fight_anime_count], (player_x, player_y))
                    elif keys[pygame.K_d] and keys[pygame.K_e]:
                        if fight_anime_1 < 15:
                            screen.blit(fight_d[0], (player_x, player_y))
                        else:
                            screen.blit(fight_d[fight_anime_count], (player_x, player_y))



                    elif keys[pygame.K_a]:  # Анимация передвижения
                        screen.blit(walk_a[player_anime_count], (player_x, player_y))
                    elif keys[pygame.K_d]:
                        screen.blit(walk_d[player_anime_count], (player_x, player_y))
                    elif keys[pygame.K_w]:
                        screen.blit(walk_w[player_anime_count], (player_x, player_y))
                    elif keys[pygame.K_s]:
                        screen.blit(walk_s[player_anime_count], (player_x, player_y))
                    elif keys[pygame.K_w] and keys[pygame.K_a]:
                        screen.blit(walk_a_w[player_anime_count], (player_x, player_y))
                    elif keys[pygame.K_w] and keys[pygame.K_d]:
                        screen.blit(walk_d_w[player_anime_count], (player_x, player_y))
                    elif keys[pygame.K_s] and keys[pygame.K_a]:
                        screen.blit(walk_a_s[player_anime_count], (player_x, player_y))
                    elif keys[pygame.K_s] and keys[pygame.K_d]:
                        screen.blit(walk_d_s[player_anime_count], (player_x, player_y))
                    else:
                        screen.blit(walk_off, (player_x, player_y))

                    movement_body_box(enemys4)  # Столкновения врагов

                    if wave_enemy_alive(enemys1) == 0:  # Счётчик волн
                        wave = 2
                    if wave_enemy_alive(enemys2) == 0:
                        wave = 3
                    if wave_enemy_alive(enemys3) == 0:
                        wave = 4
                    if wave_enemy_alive(enemys4) == 0 and (
                            (enemys4[7].repeat_anim_die == 4 and enemys4[7].anim_die_count == 3) or (
                            enemys4[6].repeat_anim_die == 4 and enemys4[6].anim_die_count == 3) or
                            (enemys4[5].repeat_anim_die == 4 and enemys4[5].anim_die_count == 3) or (
                                    enemys4[4].repeat_anim_die == 4 and enemys4[4].anim_die_count == 3)):
                        wave = 6

                    if wave == 1:  # Анимация передвижения врага
                        for enemy in enemys1:
                            enemy.movement_plus_anim_enemys()
                            health_arr.append(enemy.health_anim_count)
                        health_anim_count = sum(health_arr)
                        health_arr = []
                    if wave == 2:
                        for enemy in enemys2:
                            enemy.movement_plus_anim_enemys()
                            health_arr.append(enemy.health_anim_count)
                        health_anim_count = sum(health_arr)
                        health_arr = []
                    if wave == 3:
                        for enemy in enemys3:
                            enemy.movement_plus_anim_enemys()
                            health_arr.append(enemy.health_anim_count)
                        health_anim_count = sum(health_arr)
                        health_arr = []
                    if wave == 4:
                        for enemy in enemys4:
                            enemy.movement_plus_anim_enemys()
                            health_arr.append(enemy.health_anim_count)
                        health_anim_count = sum(health_arr)
                        health_arr = []
                    screen.blit(healthbar[health_anim_count],
                                (player_x - 21, player_y - 30))  # Анимация здоровья персонажа

                    if wave == 6 and dark_count < 40:
                        screen.blit(dark, (0, 0))
                        if dark_count == 39:
                            wave = 5
                        dark_count += 1

                    if not (keys[pygame.K_e]):  # Передвижение
                        fight_anime_count = 0
                        fight_anime_1 = 0
                        if keys[pygame.K_a] and keys[pygame.K_w] and player_x > 40 and player_y > 40 and allow_move(
                                player_x,
                                player_y) != 1 and allow_move(
                            player_x, player_y) != 2:
                            player_x -= player_speed / (2 ** 0.5)
                            player_y -= player_speed / (2 ** 0.5)
                        elif keys[pygame.K_d] and keys[pygame.K_w] and player_x < 710 and player_y > 40 and allow_move(
                                player_x,
                                player_y) != 1 and allow_move(
                            player_x, player_y) != 4:
                            player_x += player_speed / (2 ** 0.5)
                            player_y -= player_speed / (2 ** 0.5)
                        elif keys[pygame.K_a] and keys[pygame.K_s] and player_y < 510 and player_x > 40 and allow_move(
                                player_x,
                                player_y) != 2 and allow_move(
                            player_x, player_y) != 3:
                            player_x -= player_speed / (2 ** 0.5)
                            player_y += player_speed / (2 ** 0.5)
                        elif keys[pygame.K_d] and keys[pygame.K_s] and player_y < 510 and player_x < 710 and allow_move(
                                player_x,
                                player_y) != 4 and allow_move(
                            player_x, player_y) != 3:
                            player_x += player_speed / (2 ** 0.5)
                            player_y += player_speed / (2 ** 0.5)
                        elif keys[pygame.K_a] and player_x > 40 and allow_move(player_x, player_y) != 2:
                            player_x -= player_speed
                        elif keys[pygame.K_d] and player_x < 710 and allow_move(player_x, player_y) != 4:
                            player_x += player_speed
                        elif keys[pygame.K_w] and player_y > 40 and allow_move(player_x, player_y) != 1:
                            player_y -= player_speed
                        elif keys[pygame.K_s] and player_y < 510 and allow_move(player_x, player_y) != 3:
                            player_y += player_speed
                    else:
                        fight_anime_1 += 1

                    for enemy in enemys4:  # Сражение с врагами
                        if player_anime_count == 5:
                            if keys[pygame.K_w] and keys[
                                pygame.K_e] and 0 <= player_y - enemy.enemy_pos_y <= 60 and abs(
                                    player_x - enemy.enemy_pos_x) <= 50:
                                enemy.alive = 0
                            elif keys[pygame.K_a] and keys[pygame.K_e] and abs(
                                    player_y - enemy.enemy_pos_y) <= 50 and 0 <= player_x - enemy.enemy_pos_x <= 50:
                                enemy.alive = 0
                            elif keys[pygame.K_s] and keys[
                                pygame.K_e] and 0 <= enemy.enemy_pos_y - player_y <= 60 and abs(
                                    player_x - enemy.enemy_pos_x) <= 50:
                                enemy.alive = 0
                            elif keys[pygame.K_d] and keys[pygame.K_e] and abs(
                                    player_y - enemy.enemy_pos_y) <= 50 and 0 <= enemy.enemy_pos_x - player_x <= 50:
                                enemy.alive = 0

                    if repeat_walk_anim == 4:  # Измения счётчиков задержки кадров анимации
                        player_anime_count += (
                                    1 * (player_anime_count != 7) - player_anime_count * (player_anime_count == 7))
                        repeat_walk_anim = 0
                    if repeat_fight_anim == 6:
                        fight_anime_count += (
                                    1 * (fight_anime_count != 7) - fight_anime_count * (fight_anime_count == 7))
                        repeat_fight_anim = 0
                    if repeat_fire_anim == 4:
                        fire_anime_count += (1 * (fire_anime_count != 15) - fire_anime_count * (fire_anime_count == 15))
                        repeat_fire_anim = 0

                    clock.tick(60)
            elif quit_button_pos[0] <= mouse_pos[0] <= quit_button_pos[0] + quit_button_image.get_width() and \
                    quit_button_pos[1] <= mouse_pos[1] <= quit_button_pos[1] + quit_button_image.get_height():
                # Quit the game
                running = False
                pygame.quit()
                sys.exit()
