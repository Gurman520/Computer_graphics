from math import *
import pygame

pygame.init()  # Запускаем pygame
screen = pygame.display.set_mode((500, 500))  # Устанавливаем размер экрана
pygame.display.set_caption("func_graph")  # Задаём имя для окна
all_sprites = pygame.sprite.Group()  # Группируем спрайты
clock = pygame.time.Clock()  # Чтобы программа работала с заданной частотой кадров
running = True
fps = 60


# Класс для рисования осей
class Line(pygame.sprite.Sprite):
    def __init__(self, pos, x, y):
        pygame.sprite.Sprite.__init__(self)
        if pos == "x":
            self.image = pygame.Surface((3, 400))  # Рисуем линию 3х400
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
        elif pos == "y":
            self.image = pygame.Surface((400, 3))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y


# Создаем класс точка
class Dot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((5, 5))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


def Calc(func):
    i = - 0  # начальное значение аргумента
    while i <= 20:  # пока аргумент меньше 10
        mass = ""  # темп-строка
        for j in func:  # для каждого символа в строке func(наша функция)
            if j == "x":  # если символ = x, то добавляем i в темп-строку
                mass += str(i)
            else:  # если нет, то добавить исходный символ
                mass += j
            i += 0.0001  # увеличить аргумент на 0.0001
        try:
            res1 = eval(mass)  # посчитать функцию и получить результат
        except:
            res1 = 10000  # если функцию нельзя посчитать, то результат число вне координат/ Костыль
        dot = Dot(250 + i * 10,
                  250 - res1 * 10)  # dot - точка с координатой(0+x,0+y), так как это дисплей, то вектор "y" направлен вниз
        all_sprites.add(dot)  # добавить точку в группу спрайтов


func = str(input("y = "))  # Вводим функцию
calc = Calc(func)  # Вычисляем

line = Line("y", 250, 250)
all_sprites.add(line)
line1 = Line("x", 250, 250)
all_sprites.add(line1)

while running:
    clock.tick(fps)  # Устанавливаем FPS Держим цикл на правильной скорости
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
