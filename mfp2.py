import pygame
import sys
# import pygame_menu
# import pygamecontroller
import random

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def insert_2_or_4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4


def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_index_from_number(i, j)
                empty.append(num)
    return empty


def get_index_from_number(i, j):
    return i * 4 + j + 1


#   цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (130, 130, 130)
BLACK_GRAY = (54, 54, 54)
frame_color = (204, 255, 240)
#   размеры/кол-во
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN  # ширина
HEIGHT = WIDTH + 110  # высота
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)

#   вывод массива
mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)
#   вывод графики и логика
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
pygame.key.get_mods()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('EXIT')
            quit()
            sys.exit(0)
        elif event.type == pygame.KEYUP:  # отрисовка квадратов
            pygame.draw.rect(screen, WHITE, TITLE_REC)
            for row in range(BLOCKS):
                for column in range(BLOCKS):
                    w = column * SIZE_BLOCK + (column + 1) * MARGIN
                    h = row * SIZE_BLOCK + (row + 1) * MARGIN + 110
                    pygame.draw.rect(screen, GRAY, (w, h, 110, 110))
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
    pygame.display.flip()  # можно pygame.display.update() использовать вроде
