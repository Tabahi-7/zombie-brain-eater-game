import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import random

pygame.init()

width, height = 600, 400
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = window.get_size()

pygame.display.set_caption("Zombie Snake Game 🧟‍♂️")

red = (213, 50, 80)
green = (0, 255, 0)

clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10


base_path = os.path.dirname(os.path.abspath(__file__))

zombie_img = pygame.image.load(os.path.join(base_path, "zombie.png"))
zombie_img = pygame.transform.scale(zombie_img, (snake_block, snake_block))

brain_img = pygame.image.load(os.path.join(base_path, "brain.png"))
brain_img = pygame.transform.scale(brain_img, (snake_block, snake_block))

background_img = pygame.image.load(os.path.join(base_path, "graveyard.png"))
background_img = pygame.transform.scale(background_img, (width, height))

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 20)

def draw_snake(snake_list):
    for x, y in snake_list:
        window.blit(zombie_img, (x, y))

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

def draw_score(score):
    value = score_font.render("Brains Eaten: " + str(score), True, green)
    window.blit(value, [10, 10])

def gameLoop():
    game_over = False
    game_close = False
    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            window.blit(background_img, (0, 0))
            message("You Died! Press C-Play Again or Q-Quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    x1_change, y1_change = -snake_block, 0
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    x1_change, y1_change = snake_block, 0
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    y1_change, x1_change = -snake_block, 0
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    y1_change, x1_change = snake_block, 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.blit(background_img, (0, 0))
        window.blit(brain_img, (foodx, foody))

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_List)
        draw_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

gameLoop()

