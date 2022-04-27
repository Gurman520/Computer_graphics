import pygame as pg
import numpy as np
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

cubeVertices = (
    (1, 1, 1, 1), (1, 1, -1, 1), (1, -1, -1, 1), (1, -1, 1, 1), (-1, 1, 1, 1), (-1, -1, -1, 1), (-1, -1, 1, 1),
    (-1, 1, -1, 1))  # Определяет каждую вершину куба
cubeEdges_v1 = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (2, 3), (3, 6), (4, 6), (4, 7), (5, 6),
             (5, 7))  # Определяет вершины, которые необходимо соединить

cubeEdges_v2 = ((0, 4, 7, 1), (0, 1, 2, 3), (0, 4, 6, 3), (4, 6, 5, 7), (7, 5, 2, 1), (6, 3, 5, 2))  # Определяет вершины, которые необходимо соединить


# Функция рисования куба
def wireCube():
    # GL_LINES – это макрос, который указывает, что мы будем рисовать линии.
    glBegin(GL_QUADS)  # Говорим OpenGl что дальше будет исполняемый код для него
    for cubeEdge in cubeEdges_v2:
        for cubeVertex in cubeEdge:
            glVertex4fv(cubeVertices[cubeVertex])
            # функция, определяющая вершину с помощью 4 координат типа GLfloat, которые помещаются внутри вектора (кортежа)
    glEnd()  # Закончили рисовать


def gran():
    # GL_LINES – это макрос, который указывает, что мы будем рисовать линии.
    glBegin(GL_QUADS)  # Говорим OpenGl что дальше будет исполняемый код для него
    for cubeEdge in cubeEdges_v1:
        for cubeVertex in cubeEdge:
            glVertex4fv(cubeVertices[cubeVertex])
    glColor3f(1.0, 0, 0)
            # функция, определяющая вершину с помощью 4 координат типа GLfloat, которые помещаются внутри вектора (кортежа)
    glEnd()  # Закончили рисовать


def rotation_right_x():
    global cubeVertices
    cos_s = np.cos(np.pi / 180)
    sin_s = np.sin(np.pi / 180)
    list_a = [[1, 0, 0, 0], [0, cos_s, -sin_s, 0], [0, sin_s, cos_s, 0], [0, 0, 0, 1]]
    cubeVertices = list(np.array(cubeVertices).dot(list_a))


def rotation_left_x():
    global cubeVertices
    cos_s = np.cos(-np.pi / 180)
    sin_s = np.sin(-np.pi / 180)
    list_a = [[1, 0, 0, 0], [0, cos_s, -sin_s, 0], [0, sin_s, cos_s, 0], [0, 0, 0, 1]]
    cubeVertices = list(np.array(cubeVertices).dot(list_a))


def rotation_right_y():
    global cubeVertices
    cos_s = np.cos(np.pi / 180)
    sin_s = np.sin(np.pi / 180)
    list_a = [[cos_s, 0, sin_s, 0], [0, 1, 0, 0], [-sin_s, 0, cos_s, 0], [0, 0, 0, 1]]
    cubeVertices = list(np.array(cubeVertices).dot(list_a))


def rotation_left_y():
    global cubeVertices
    cos_s = np.cos(-np.pi / 180)
    sin_s = np.sin(-np.pi / 180)
    list_a = [[cos_s, 0, sin_s, 0], [0, 1, 0, 0], [-sin_s, 0, cos_s, 0], [0, 0, 0, 1]]
    cubeVertices = list(np.array(cubeVertices).dot(list_a))


def rotation_right_z():
    global cubeVertices
    cos_s = np.cos(np.pi / 180)
    sin_s = np.sin(np.pi / 180)
    list_a = [[cos_s, -sin_s, 0, 0], [sin_s, cos_s, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    cubeVertices = list(np.array(cubeVertices).dot(list_a))


def rotation_left_z():
    global cubeVertices
    cos_s = np.cos(-np.pi / 180)
    sin_s = np.sin(-np.pi / 180)
    list_a = [[cos_s, -sin_s, 0, 0], [sin_s, cos_s, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    cubeVertices = list(np.array(cubeVertices).dot(list_a))


def main():
    pg.init()
    display = (500, 500)  # Размер окна
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)  # функция, которая очищает указанные буферы

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Устанавливаем угол обзора камеры

    glTranslatef(0.0, 0.0, -5)  # Отдаляем наш куб на -5 по оси Z

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        if pg.key.get_pressed()[pg.K_RIGHT]:
            rotation_right_z()  # Поворот по Оси Z
        if pg.key.get_pressed()[pg.K_LEFT]:
            rotation_left_z()
        if pg.key.get_pressed()[pg.K_UP]:
            rotation_right_y()  # Поворот по Оси Y
        if pg.key.get_pressed()[pg.K_DOWN]:
            rotation_left_y()
        if pg.key.get_pressed()[pg.K_w]:
            rotation_right_x()  # Поворот по Оси X
        if pg.key.get_pressed()[pg.K_s]:
            rotation_left_x()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        wireCube()
        gran()
        pg.display.flip()


if __name__ == "__main__":
    main()
