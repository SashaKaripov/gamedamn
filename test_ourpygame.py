import pytest
from funcs import wave_enemy_alive, movement_body_box, allow_move
from Enemy1 import Enemy


test_enemy_1, test_enemy_2 = Enemy(0, 0, 1),Enemy(0, 0, 0)


def test_wave_enemy_alive_1():
    assert wave_enemy_alive([test_enemy_1, test_enemy_2]) == 1
    assert wave_enemy_alive([test_enemy_2, test_enemy_1]) == 1
    assert wave_enemy_alive([test_enemy_1, test_enemy_1]) == 2
    assert wave_enemy_alive([test_enemy_2, test_enemy_2]) == 0


def test_wave_enemy_alive_2():
    with pytest.raises(TypeError):
        wave_enemy_alive(1)
    with pytest.raises(AttributeError):
        wave_enemy_alive('1')


def start_pos():
    test_enemy_1.enemy_pos_x = test_enemy_1.enemy_pos_y = 0
    test_enemy_2.enemy_pos_x = test_enemy_2.enemy_pos_y = 0


def test_movement_body_box_1():
    movement_body_box([test_enemy_1, test_enemy_2])
    assert test_enemy_1.enemy_pos_x == 1
    start_pos()
    movement_body_box([test_enemy_1, test_enemy_2])
    assert test_enemy_1.enemy_pos_y == 1
    start_pos()
    movement_body_box([test_enemy_1, test_enemy_2])
    assert test_enemy_2.enemy_pos_x == -1
    start_pos()
    movement_body_box([test_enemy_1, test_enemy_2])
    assert test_enemy_2.enemy_pos_y == -1
    start_pos()


def test_movement_body_box_2():
    with pytest.raises(TypeError):
        movement_body_box(1)
    with pytest.raises(AttributeError):
        movement_body_box('1231321')


def test_allow_move_1():
    assert allow_move(0, 0, [test_enemy_1, test_enemy_2]) == 'wasd'
    assert allow_move(20, 40, [test_enemy_1, test_enemy_2]) == 'w'
    assert allow_move(40, 20, [test_enemy_1, test_enemy_2]) == 'a'
    assert allow_move(20, -40, [test_enemy_1, test_enemy_2]) == 's'
    assert allow_move(-40 ,20, [test_enemy_1, test_enemy_2]) == 'd'


def test_allow_move_2():
    with pytest.raises(TypeError):
        allow_move(0, 0, 1)
    with pytest.raises(AttributeError):
        allow_move(0, 0, '1231321')