import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddles
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)

# Scores
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 50)

# Game variables
clock = pygame.time.Clock()
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player.y += 7
    if keys[pygame.K_UP]:
        player.y -= 7

    if keys[pygame.K_s]:
        opponent.y += 7
    if keys[pygame.K_w]:
        opponent.y -= 7

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Score
    if ball.left <= 0:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))

    if ball.right >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))

    # Winning condition
    if player_score >= 5 or opponent_score >= 5:
        running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the paddles, ball, and score
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    player_text = font.render(f"{player_score}", True, WHITE)
    screen.blit(player_text, (WIDTH // 2 + 20, 20))

    opponent_text = font.render(f"{opponent_score}", True, WHITE)
    screen.blit(opponent_text, (WIDTH // 2 - 40, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Display the winner
winner_text = font.render("Player wins!" if player_score >= 5 else "Opponent wins!", True, WHITE)
screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))
pygame.display.flip()

# Wait for a few seconds before closing the game
pygame.time.wait(3000)

pygame.quit()
sys.exit()
