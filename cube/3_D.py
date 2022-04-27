import pygame
import numpy as np

cubeVertices = np.array(
    [[0, 80, 80, 1], [0, 0, 80, 1], [80, 0, 80, 1], [80, 80, 80, 1], [0, 80, 0, 1], [0, 0, 0, 1], [80, 0, 0, 1],
     [80, 80, 0, 1]])  # Определяет каждую вершину куба
cubeEdges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (5, 6),
             (6, 7))  # Определяет вершины, которые необходимо соединить


def vid(x, y, z):
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    fi = np.arctan(y / x)
    tet = np.arccos(z / np.sqrt(x ** 2 + y ** 2 + z ** 2))
    cdvig = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-x, -y, -z, 1]])
    cos_al = (np.pi / 2) - fi
    sin_al = (np.pi / 2) - fi
    list_z = np.array([[cos_al, sin_al, 0, 0], [-sin_al, cos_al, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cos_s = np.cos(np.pi - tet)
    sin_s = np.sin(np.pi - tet)
    list_x = np.array([[1, 0, 0, 0], [0, cos_s, sin_s, 0], [0, -sin_s, cos_s, 0], [0, 0, 0, 1]])
    m_x = np.array([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    return cdvig.dot(list_z.dot(list_x.dot(m_x)))


def cube(vidov, screen):
    global cubeVertices
    matrix = cubeVertices.dot(vidov)
    for cubeEdge in cubeEdges:
        pygame.draw.line(screen, (0, 0, 0), (250 + matrix[cubeEdge[0]][0], 250 - matrix[cubeEdge[0]][1]),
                         (250 + matrix[cubeEdge[1]][0], 250 - matrix[cubeEdge[1]][1]), 2)


def rotation_right_x():
    global cubeVertices
    cos_s = np.cos(np.pi / 180)
    sin_s = np.sin(np.pi / 180)
    list_a = [[1, 0, 0, 0], [0, cos_s, -sin_s, 0], [0, sin_s, cos_s, 0], [0, 0, 0, 1]]
    cubeVertices = cubeVertices.dot(list_a)


def rotation_left_x():
    global cubeVertices
    cos_s = np.cos(-np.pi / 180)
    sin_s = np.sin(-np.pi / 180)
    list_a = [[1, 0, 0, 0], [0, cos_s, -sin_s, 0], [0, sin_s, cos_s, 0], [0, 0, 0, 1]]
    cubeVertices = cubeVertices.dot(list_a)


def rotation_right_y():
    global cubeVertices
    cos_s = np.cos(np.pi / 180)
    sin_s = np.sin(np.pi / 180)
    list_a = [[cos_s, 0, sin_s, 0], [0, 1, 0, 0], [-sin_s, 0, cos_s, 0], [0, 0, 0, 1]]
    cubeVertices = cubeVertices.dot(list_a)


def rotation_left_y():
    global cubeVertices
    cos_s = np.cos(-np.pi / 180)
    sin_s = np.sin(-np.pi / 180)
    list_a = [[cos_s, 0, sin_s, 0], [0, 1, 0, 0], [-sin_s, 0, cos_s, 0], [0, 0, 0, 1]]
    cubeVertices = cubeVertices.dot(list_a)


def rotation_right_z():
    global cubeVertices
    cos_s = np.cos(np.pi / 180)
    sin_s = np.sin(np.pi / 180)
    list_a = np.array([[cos_s, -sin_s, 0, 0], [sin_s, cos_s, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cubeVertices = cubeVertices.dot(list_a)


def rotation_left_z():
    global cubeVertices
    cos_s = np.cos(-np.pi / 180)
    sin_s = np.sin(-np.pi / 180)
    list_a = [[cos_s, -sin_s, 0, 0], [sin_s, cos_s, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    cubeVertices = cubeVertices.dot(list_a)


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))  # Устанавливаем размер экрана
    pygame.display.set_caption("Кубик")  # Задаём имя для окна
    vidov_matrix = vid(10, 10, 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            rotation_right_z()  # Поворот по Оси Z
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            rotation_left_z()
        if pygame.key.get_pressed()[pygame.K_UP]:
            rotation_right_y()  # Поворот по Оси Y
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            rotation_left_y()
        if pygame.key.get_pressed()[pygame.K_w]:
            rotation_right_x()  # Поворот по Оси X
        if pygame.key.get_pressed()[pygame.K_s]:
            rotation_left_x()
        screen.fill((255, 255, 255))
        cube(vidov_matrix, screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
