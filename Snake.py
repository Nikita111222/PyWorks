import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
width = 800
height = 600

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Создание окна
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

# Управление
clock = pygame.time.Clock()
block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Отображение счета
def our_score(score):
    value = score_font.render("Счет: " + str(score), True, black)
    window.blit(value, [0, 0])

# Отрисовка змейки
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, blue, [x[0], x[1], block_size, block_size])

# Отображение сообщения на экране
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width/6, height/3])

# Главная функция игры
def gameLoop():
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = width/2
    y1 = height/2

    # Изменение координат змейки
    x1_change = 0
    y1_change = 0

    # Создание списка для хранения координат змейки
    snake_List = []
    Length_of_snake = 1

    # Случайные координаты для появления еды
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(white)
            message("Нажми Пробел для продолжения или Q для выхода", red)
            our_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        # Управление змейкой
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Проверка, если змейка достигла границы
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Изменение координат змейки
        x1 += x1_change
        y1 += y1_change
        window.fill(white)

        # Отрисовка еды
        pygame.draw.rect(window, red, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка, если змейка съела саму себя
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Отрисовка змейки
        our_snake(block_size, snake_List)
        our_score(Length_of_snake - 1)

        pygame.display.update()

        # Проверка, если змейка съела еду
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

# Запуск игры
gameLoop()
