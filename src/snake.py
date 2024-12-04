import pygame
import time
import random
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer for sound

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Define display size
display_width = 800
display_height = 600

# Create the game window
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock and snake speed
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10

# Define font and size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load background music
bgm_path = os.path.join('BGM', 'yesterday.mp3')
if os.path.exists(bgm_path):
    pygame.mixer.music.load(bgm_path)
    pygame.mixer.music.set_volume(0.5)   # Set volume to a reasonable level
    pygame.mixer.music.play(-1)          # Loop the background music indefinitely

# Function to display score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    game_display.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for i, x in enumerate(reversed(snake_list)):
        brightness = 255 - int((i / len(snake_list)) * 200)
        color = (0, brightness, 0)
        pygame.draw.rect(game_display, color, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

def main():  # main function
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = snake_block
    y1_change = 0

    snake_List = [[x1 - (i * snake_block), y1] for i in range(5)]
    Length_of_snake = 5

    foodx = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0

    # Define obstacle position
    obstacle_x = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
    obstacle_y = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            game_display.fill(black)
            message("You Lost! Press Q-Quit or R-Play Again", red)
            Your_score(Length_of_snake - 5)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        main()
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)
        # Draw the food as a yellow circle
        pygame.draw.circle(game_display, yellow, (int(foodx + snake_block / 2), int(foody + snake_block / 2)), snake_block // 2)
        # Draw the obstacle
        pygame.draw.polygon(game_display, red, [(obstacle_x, obstacle_y), 
                                               (obstacle_x + snake_block, obstacle_y + snake_block / 2), 
                                               (obstacle_x, obstacle_y + snake_block)])
        
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Check if snake hits the obstacle
        if obstacle_x <= x1 < obstacle_x + snake_block and obstacle_y <= y1 < obstacle_y + snake_block:
            game_close = True
            # Move obstacle to a new random position
            obstacle_x = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
            obstacle_y = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 5)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            # Move obstacle to a new random position after eating food
            obstacle_x = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
            obstacle_y = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0
            while obstacle_x == foodx and obstacle_y == foody:  # Ensure obstacle and food are not in the same position
                obstacle_x = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
                obstacle_y = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0
            foodx = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

main()