#Reverse Timer

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 400, 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reverse Timer")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 50)

# Define time variables
total_seconds = 300  # Set the initial time in seconds
current_time = total_seconds

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the timer
    if current_time > 0:
        current_time -= 1

    # Clear the screen
    window.fill(WHITE)

    # Render the timer text
    timer_text = font.render(str(str(current_time//60)+":"+str(current_time-60*(current_time//60))), True, BLACK)
    text_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(timer_text, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(1)  # Update the timer once per second

# Quit Pygame
pygame.quit()
sys.exit()
