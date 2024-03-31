import pygame
import random

# # Initialize Pygame
pygame.init()
#
# # Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")
#
# # Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#
#
# # Ball
ball_size = 30
ball_x = random.randint(0, screen_width - ball_size)
ball_y = random.randint(0, screen_height - ball_size)
ball_speed_x = 5
ball_speed_y = 5
ball_color = random.choice([RED, GREEN, BLUE, YELLOW])
#
# # Main game loop
clock = pygame.time.Clock()
running = True
while running:
     screen.fill(WHITE)

#     # Event handling
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
#
#     # Move the ball
     ball_x += ball_speed_x
     ball_y += ball_speed_y
#
#     # Bounce off the walls
     if ball_x <= 0 or ball_x >= screen_width - ball_size:
         ball_speed_x *= -1
         ball_color = random.choice([RED, GREEN, BLUE, YELLOW])
     if ball_y <= 0 or ball_y >= screen_height - ball_size:
         ball_speed_y *= -1
         ball_color = random.choice([RED, GREEN, BLUE, YELLOW])
#
#     # Draw the ball
     pygame.draw.ellipse(screen, ball_color, (ball_x, ball_y, ball_size, ball_size))
#
     pygame.display.flip()
     clock.tick(60)
#
# # Quit Pygame
pygame.quit()


