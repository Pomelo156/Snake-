#bring pygame and use random for food to spawn
import pygame
import random

# Initialize pygame
pygame.init()

# Define display size (small window), use round numbers to ends with zero, to fit grid better
display_width = 800
display_height = 600
# Define color for word, snake, food, etc...

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Define font and size(look up some pygame fonts and set the size.)

font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 30) #need to test and see how big is it in the game.

# Create the game window

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock and snake speed(set us snake size, need to test out the speed later)

clock = pygame.time.Clock()
snake_block = 20
snake_speed = 15
# main function