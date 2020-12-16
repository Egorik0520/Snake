import pygame
import sys
from menu import menu
from menu import over
from menu import main 
from random import randrange

length = 1
#размер окна
W, H = 800, 800
#размер змеи и яблока
D = 40
#цвета
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)


#координаты
x, y = W // 2, H // 2
snake = [(x, y)]
dx, dy = 0, 0
#координаты яблока
apple_x = randrange(D, W - D, D)
apple_y = randrange(D, H - D, D)

apple = randrange(D, W - D, D), randrange(D, H - D, D)

#скорость
speed_count, snake_speed = 0, 4

#управление 
control = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True, }

#окно
pygame.init()
pygame.display.set_caption('Змейка')
screen = pygame.display.set_mode((W,H))
pygame.mouse.set_visible(True)

#фпс
FPS = 60
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 26, True)
font1 = pygame.font.SysFont('Arial Black', 80, True)

score = 0
SW = 5
SH = 5

#фон
bg = pygame.image.load('spacex.jpg').convert()
bg_rect = bg.get_rect(topleft=(0,0))
run = True
o = True
while o:
    menu(bg, bg_rect,W,H)
    main(run)
    over(bg, bg_rect, W, H, run)