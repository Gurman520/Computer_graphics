import numpy as np
import pygame
import math

pygame.init()  # Запускаем pygame
screen = pygame.display.set_mode((500, 500))  # Устанавливаем размер экрана
pygame.display.set_caption("Отражение")  # Задаём имя для окна
clock = pygame.time.Clock()  # Чтобы программа работала с заданной частотой кадров
running = True
fps = 60

r = 100


def brez_circle(screen):
    x, y = 0, r
    delta = 3 - 2 * r
    while y >= x:
        screen.set_at((250 + x, 250 - y), (0, 0, 0))
        screen.set_at((250 + y, 250 - x), (0, 0, 0))
        screen.set_at((250 + x, 250 + y), (0, 0, 0))
        screen.set_at((250 + y, 250 + x), (0, 0, 0))
        screen.set_at((250 - x, 250 + y), (0, 0, 0))
        screen.set_at((250 - y, 250 + x), (0, 0, 0))
        screen.set_at((250 - x, 250 - y), (0, 0, 0))
        screen.set_at((250 - y, 250 - x), (0, 0, 0))
        if delta < 0:
            delta += 4 * x + 6
        elif delta >= 0:
            y -= 1
            delta += 4 * (x - y) + 10
        x += 1


while running:
    clock.tick(fps)  # Устанавливаем FPS Держим цикл на правильной скорости
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))  # Заполняем экран одним цветом
    pygame.draw.line(screen, (0, 0, 0), [10, 250], [490, 250], 2)
    pygame.draw.line(screen, (0, 0, 0), [250, 10], [250, 490], 2)
    brez_circle(screen)
    pygame.display.flip()  # Переворачиваем экран, при использовании двойной буферезаци
pygame.quit()
