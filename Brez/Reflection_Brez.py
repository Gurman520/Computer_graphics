import numpy as np
import pygame
import math

pygame.init()  # Запускаем pygame
screen = pygame.display.set_mode((500, 500))  # Устанавливаем размер экрана
pygame.display.set_caption("Отражение")  # Задаём имя для окна
clock = pygame.time.Clock()  # Чтобы программа работала с заданной частотой кадров
running = True
fps = 60
scaling = 1  # Отслеживает масштаб

coordinates = np.array([[50, 50, 1], [100, 100, 1]])


def central():  # Отображение по центру
    global coordinates
    central_sim = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    coordinates = coordinates.dot(central_sim)


def reflection_x():  # Отражение по X
    global coordinates
    otob_x = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    coordinates = coordinates.dot(otob_x)


def reflection_y():  # Отражение по Y
    global coordinates
    otob_y = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    coordinates = coordinates.dot(otob_y)


def turn_left():  # Поворот влево
    global coordinates
    cos_s = np.cos(np.pi / 180)
    sin_s = np.sin(np.pi / 180)
    list_a = [[cos_s, sin_s, 0], [-sin_s, cos_s, 0], [0, 0, 1]]
    turn_l = np.array(list_a)
    coordinates = coordinates.dot(turn_l)


def turn_right():  # Поворот в право
    global coordinates
    cos_s = np.cos(-np.pi / 180)
    sin_s = np.sin(-np.pi / 180)
    list_a = [[cos_s, sin_s, 0], [-sin_s, cos_s, 0], [0, 0, 1]]
    turn_r = np.array(list_a)
    coordinates = coordinates.dot(turn_r)


def scaling_plus():  # Масштабирование плюс
    global coordinates, scaling
    a = (coordinates[0][0] + coordinates[1][0]) / 2
    b = (coordinates[0][1] + coordinates[1][1]) / 2
    s1 = np.array([[1, 0, 0], [0, 1, 0], [-a, -b, 1]])
    s2 = np.array([[1, 0, 0], [0, 1, 0], [a, b, 1]])
    m = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])
    coordinates = coordinates.dot(s1.dot(m).dot(s2))
    scaling *= 2


def scaling_minus():  # Масштабирование минус
    global coordinates, scaling
    a = (coordinates[0][0] + coordinates[1][0]) / 2
    b = (coordinates[0][1] + coordinates[1][1]) / 2
    s1 = np.array([[1, 0, 0], [0, 1, 0], [-a, -b, 1]])
    s2 = np.array([[1, 0, 0], [0, 1, 0], [a, b, 1]])
    m = np.array([[1 / 2, 0, 0], [0, 1 / 2, 0], [0, 0, 1]])
    coordinates = coordinates.dot(s1.dot(m).dot(s2))
    scaling /= 2


def brez(screen: screen):
    global scaling
    del_y = abs(coordinates[1][1] - coordinates[0][1])
    del_x = abs(coordinates[1][0] - coordinates[0][0])
    bet = 0
    # Первая четверть
    if coordinates[0][0] < coordinates[1][0] and coordinates[0][1] < coordinates[1][1]:
        start_x = coordinates[0][0]
        finish_x = coordinates[1][0]
        start_y = coordinates[0][1]
        finish_y = coordinates[1][1]
        z = 1
        y = int(coordinates[0][1])
        x_x = int(coordinates[0][0])
    # Вторая четверть
    elif coordinates[0][0] > coordinates[1][0] and coordinates[0][1] < coordinates[1][1]:
        start_x = coordinates[1][0]
        finish_x = coordinates[0][0]
        start_y = coordinates[0][1]
        finish_y = coordinates[1][1]
        z = -1
        y = int(coordinates[1][1])
        x_x = int(coordinates[0][0])
    # Третья четверть
    elif coordinates[0][0] > coordinates[1][0] and coordinates[0][1] > coordinates[1][1]:
        start_x = coordinates[1][0]
        finish_x = coordinates[0][0]
        start_y = coordinates[1][1]
        finish_y = coordinates[0][1]
        z = 1
        y = int(coordinates[1][1])
        x_x = int(coordinates[1][0])
    # Четвертая четверть
    else:
        start_x = coordinates[0][0]
        finish_x = coordinates[1][0]
        start_y = coordinates[1][1]
        finish_y = coordinates[0][1]
        z = -1
        y = int(coordinates[0][1])
        x_x = int(coordinates[1][0])

    if del_x >= (50 * scaling):
        # Рисует линию, пока линия больше горизонтальная,чем вертикальная
        for x in range(int(math.ceil(start_x)), int(math.ceil(finish_x))):
            bet += 2 * del_y
            if bet >= del_x:
                y += z
                bet -= 2 * del_x
            screen.set_at((250 + x, 250 - y), (0, 0, 0))
    else:
        # Рисует линию, пока линия больше вертикальная,чем горизонтальная
        for y in range(int(math.ceil(start_y)), int(math.ceil(finish_y))):
            bet += 2 * del_x
            if bet >= del_y:
                x_x += z
                bet -= 2 * del_y
            screen.set_at((250 + x_x, 250 - y), (0, 0, 0))


while running:
    clock.tick(fps)  # Устанавливаем FPS Держим цикл на правильной скорости
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                central()
            if event.key == pygame.K_x:
                reflection_x()
            if event.key == pygame.K_y:
                reflection_y()
            if event.key == pygame.K_RIGHT:
                scaling_plus()
            if event.key == pygame.K_LEFT:
                scaling_minus()
    if pygame.key.get_pressed()[pygame.K_UP]:
        turn_left()
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        turn_right()
    screen.fill((255, 255, 255))  # Заполняем экран одним цветом
    pygame.draw.line(screen, (0, 0, 0), [10, 250], [490, 250], 2)
    pygame.draw.line(screen, (0, 0, 0), [250, 10], [250, 490], 2)
    brez(screen)
    pygame.display.flip()  # Переворачиваем экран, при использовании двойной буферезаци
pygame.quit()
