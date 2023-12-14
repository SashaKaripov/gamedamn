def wave_enemy_alive(enemys: list, sum=0) -> int:  # счётчик выживших врагов
    """"Returns sum of the living enemies

        :param enemys: enemys
        :type enemys: list
        :param sum: sum of the living enemies
        :type sum: int
        :returns: sum of the living enemies
        :rtype: int"""
    
    for enemy in enemys:
        sum += enemy.alive
    return sum


def movement_body_box(enemys: list):  # Столкновение врагов
    """"Changes enemy's coordinate if enemys collide

        :param enemys: enemys
        :type enemys: list
        :changes: enemy's coordinate
        :ctype: float"""
    
    for i in range(len(enemys) - 1):
        for j in range(i + 1, len(enemys)):
            if abs(enemys[j].enemy_pos_x - enemys[i].enemy_pos_x) <= 25 and abs(enemys[j].enemy_pos_y - enemys[i].enemy_pos_y) <= 50:
                enemys[i].enemy_pos_y += 1
                enemys[i].enemy_pos_x += 1
                enemys[j].enemy_pos_y -= 1
                enemys[j].enemy_pos_x -= 1



def allow_move(player_x: float, player_y: float, enemys: list, cases_ = '') -> str:  # Врезается ли игрок во врага
    """"Returns the cases when the button's disabled 

        :param player_x: x-coordinate 
        :type player_x: float
        :param player_y: y-coordinate
        :type player_y: float
        :returns: cases of button's disabled 
        :rtype: str"""

    for enemy in enemys:
        if enemy.alive == 1:
            if 0 <= player_y - enemy.enemy_pos_y <= 40 and abs(enemy.enemy_pos_x - player_x) <= 20 and 'w' not in cases_:
                cases_ += 'w'
            if abs(player_y - enemy.enemy_pos_y) <= 20 and 0 <= player_x - enemy.enemy_pos_x <= 40 and 'a' not in cases_:
                cases_ += 'a'
            if 0 <= enemy.enemy_pos_y - player_y <= 40 and abs(enemy.enemy_pos_x - player_x) <= 20 and 's' not in cases_:
                cases_ += 's'
            if abs(player_y - enemy.enemy_pos_y) <= 20 and 0 <= enemy.enemy_pos_x - player_x <= 40 and 'd' not in cases_:
                cases_ += 'd'
    return cases_