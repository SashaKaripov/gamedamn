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
        self.hp = 1


    def movement_plus_anim_enemys(self, player_x, player_y, screen):
        if self.alive == 1:
            if not(abs(self.enemy_pos_x - player_x) <= 25 and abs(self.enemy_pos_y - player_y) <= 50):
                if -70 <= player_x - self.enemy_pos_x <= 70 and self.enemy_pos_y - player_y > 50:
                    screen.blit(self.image_u[self.enemy_anim_count], (self.enemy_pos_x, self.enemy_pos_y))
                elif -70 <= player_x - self.enemy_pos_x <= 70 and player_y - self.enemy_pos_y > 50:
                    screen.blit(self.image_d[self.enemy_anim_count], (self.enemy_pos_x, self.enemy_pos_y))
                elif self.enemy_pos_x <= player_x:
                    screen.blit(self.image_r[self.enemy_anim_count], (self.enemy_pos_x, self.enemy_pos_y))
                    self.enemy_pos_x += 3 / 2**0.5
                else:
                    screen.blit(self.image_l[self.enemy_anim_count], (self.enemy_pos_x, self.enemy_pos_y))
                    self.enemy_pos_x -= 3 / 2**0.5
                if self.enemy_pos_y <= player_y:
                    self.enemy_pos_y += 3 / 2**0.5
                else:
                    self.enemy_pos_y -= 3 / 2**0.5

                if self.repeat_enemy_anim == 4:
                    self.enemy_anim_count += (self.enemy_anim_count != 7) - self.enemy_anim_count*(self.enemy_anim_count == 7)
                    self.repeat_enemy_anim = 0
                self.repeat_enemy_anim += 1
            else:
                if self.enemy_pos_x <= player_x:
                    screen.blit(self.enemy_fight_r[self.enemy_fight_anim_count], (self.enemy_pos_x, self.enemy_pos_y))
                if self.enemy_pos_x > player_x:
                    screen.blit(self.enemy_fight_l[self.enemy_fight_anim_count], (self.enemy_pos_x, self.enemy_pos_y))
                if self.repeat_anim_fight == 4:
                    self.enemy_fight_anim_count += (self.enemy_fight_anim_count != 5) - self.enemy_fight_anim_count*(self.enemy_fight_anim_count == 5)
                    self.repeat_anim_fight = 0
                self.repeat_anim_fight += 1

                if self.repeat_anim_fight == 3 and self.enemy_fight_anim_count == 4:
                    self.health_anim_count += 1
        else:
            if self.anim_die_count != 4:
                screen.blit(self.image_die[self.anim_die_count], (self.enemy_pos_x, self.enemy_pos_y))
                if self.repeat_anim_die == 4:
                    self.anim_die_count += (self.anim_die_count != 4) - self.anim_die_count * (self.anim_die_count == 4)
                    self.repeat_anim_die = 0
                self.repeat_anim_die += 1
            else:
                screen.blit(self.image_die[self.anim_die_count], (self.enemy_pos_x, self.enemy_pos_y))