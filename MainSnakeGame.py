import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
# determining coordinates of my figure
figX, figY = 100, 100
fig_list = []
fig_length = 1
vel = 0.09
# determining change in coordinates
fig_x, fig_y = 0.09, 0
# determining the coordinates of food
foodX = random.randint(0, 300)
foodY = random.randint(0, 300)
# giving a state to our object for no backwards turn
state = "Right"
# score and coordinates where score will be displayed and font of score
score = 0
scorex = 5
scorey = 5
font = pygame.font.SysFont(None, 50)


def show_score(x, y):
    global score
    score_value = font.render("Score: " + str(score), True, (255, 255, 0))
    screen.blit(score_value, (x, y))


game_over = False


def plot_figure(window, color, fig_list, fig_length):
    for x, y in fig_list:a
        pygame.draw.rect(screen, color, [x, y, 20, 20])


run = False
while not run:
    screen.fill((0, 0, 0))
    if game_over is True:
        screen.fill((255,255,255))
        text = font.render("Game Over!",True,(255,0,0))
        screen.blit(text,(150,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and state != "Down":
                    state = "Up"
                    fig_x = 0
                    fig_y = -vel
                if event.key == pygame.K_DOWN and state != "Up":
                    state = "Down"
                    fig_x = 0
                    fig_y = vel
                if event.key == pygame.K_LEFT and state != "Right":
                    state = "Left"
                    fig_y = 0
                    fig_x = -vel
                if event.key == pygame.K_RIGHT and state != "Left":
                    state = "Right"
                    fig_y = 0
                    fig_x = vel

        # food again generates if the distance b/w snake and food becomes less than 6
        if abs(foodX - figX) < 15 and abs(foodY - figY) < 15:
            score += 1
            vel += 0.03
            foodX = random.randint(0, 300)
            foodY = random.randint(0, 300)
            fig_length += 20
        head = []
        head.append(figX)
        head.append(figY)
        fig_list.append(head)

        if len(fig_list) > fig_length:
            del fig_list[0]
        # if head collides with any other part the game ends
        if head in fig_list[:-1] :
            game_over = True

        if figX <= 0 or figX >= 580:
            figX = 300
            game_over = True
        if figY <= 0 or figY >= 580:
            figY = 300
            game_over = True
        figX += fig_x
        figY += fig_y

        show_score(scorex, scorey)
        # this is to create snake and food on the screen
        pygame.draw.rect(screen, (0, 255, 0), [foodX, foodY, 20, 20])
        plot_figure(screen, (255, 255, 0), fig_list, fig_length)
    pygame.display.update()
