import pygame
import sys
from random import randrange

def menu(a,b,c,d):
    gray = (128,128,128)
    start = True
    font = pygame.font.SysFont('Arial',80,True)
    font1 = pygame.font.SysFont('Arial', 40,True)
    pygame.init()
    pygame.display.set_caption('Змейка')
    screen = pygame.display.set_mode((c,d))
    pygame.mouse.set_visible(True)
    button = pygame.Rect(300,325,200,50)
    button1 = pygame.Rect(300,390,200,50)

    play = font1.render('Play',1,(0,255,0))
    #exit_e = font1.render('Exit',1,(0,255,0))
     
    while start:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    sys.exit(0)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.pos[0] >=300 and e.pos[0] <= 500 and e.pos[1] >=325 and e.pos[1] <=375:
                    start = False
                elif e.pos[0] >=300 and e.pos[0] <= 500 and e.pos[1] >=390 and e.pos[1] <=440:
                    sys.exit(0)
        snake = font.render('Snake',1,(0,255,0))
        Exit = font1.render('Exit',1,(0,255,0))
        screen.blit(snake,(300,300))
        screen.blit(a, b)
        pygame.draw.rect(screen,gray,(300,325,200,50))
        pygame.draw.rect(screen, gray,(300,390,200,50))
        screen.blit(Exit,(360,390))
        screen.blit(snake,(280,225))
        screen.blit(play,(355,325))

        pygame.display.update()

def over(a,b,c,d,f):
    gray = (128,128,128)
    start = True
    font = pygame.font.SysFont('Arial Black', 80, True)
    font1 = pygame.font.SysFont('Arial', 40,True)
    button = pygame.Rect(300,325,200,50)

    pygame.init()
    pygame.display.set_caption('Змейка')
    screen = pygame.display.set_mode((c,d))
    pygame.mouse.set_visible(True)

    play_again = font1.render('Play Again',1,(255,0,0))
    Game_Over = font.render('Game Over',1,(255,0,0))

    while start:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    f = True
                    start = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.pos[0] >=300 and e.pos[0] <= 500 and e.pos[1] >=325 and e.pos[1] <=375:
                    start = False
                elif e.pos[0] >=300 and e.pos[0] <= 500 and e.pos[1] >=390 and e.pos[1] <=440:
                    sys.exit(0)
                    #sys.exit(0)
        
        Exit = font1.render('exit',1,(255,0,0))
        Con = font1.render('menu',1,(255,0,0))
        screen.blit(a,b)
        screen.blit(Game_Over,(125,215))
        pygame.draw.rect(screen,gray,(300,325,200,50))
        pygame.draw.rect(screen, gray,(300,390,200,50))
        screen.blit(Exit,(365,390))
        screen.blit(Con,(345,325))
        pygame.display.update()

def main(a):
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
    while a:
        speed_count += 1
        if not speed_count % snake_speed:
	        x += dx * D
	        y += dy * D
	        snake.append((x, y))
	        snake = snake[-length:]
        if snake[-1] == apple:
            score += 1
            apple = randrange(D, W - D, D), randrange(D, H - D, D)
            apple_x = randrange(D, W - D, D)
            apple_y = randrange(D, H - D, D)
            length += 1
        
        if x < 0 or x > W-D  or y < 0 or y > H-D or len(snake) != len(set(snake)):
            a = False
                            
        

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                a = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    a = False
                elif e.key == pygame.K_w:
                    pause = True
                    while pause:
                        pygame.display.update()
                        if e.key == pygame.K_w:
                            pause = False
                elif e.key == pygame.K_UP:
                    if control['UP']:
                        dx, dy = 0, -1
                        control = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True, }
                elif e.key == pygame.K_DOWN:
                    if control['DOWN']:
                        dx, dy = 0, 1
                        control = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True, }
                elif e.key == pygame.K_RIGHT:
                    if control['RIGHT']:
                        dx, dy = 1, 0
                        control = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True, }
                elif e.key == pygame.K_LEFT:
                    if control['LEFT']:
                        dx, dy = -1, 0
                        control = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False, }

        #screen.fill(black)
        SCORE = font.render(f'SCORE: {score}',1,green)
        screen.blit(SCORE,(5,5))
        screen.blit(bg, bg_rect)
        for i, j in snake:
            pygame.draw.rect(screen, green, (i, j, D, D))
        pygame.draw.rect(screen, red,(*apple, D, D))
        clock.tick(FPS)
        SCORE = font.render(f'SCORE: {score}',1,green)
        screen.blit(SCORE,(5,5))
        pygame.display.update()

def q():
    while run:    
            Game_Over = font1.render('GAME OVER',1,red)
            screen.blit(Game_Over,(W // 2 - 300, H - 450))
            pygame.display.update()
            for y in pygame.event.get():
                if y.type == pygame.QUIT:
                    #run = False
                    sys.exit(0)
                if y.type == pygame.KEYDOWN:
                    if y.key == pygame.K_ESCAPE:
                        #run = False
                        sys.exit(0)