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
total_seconds = 60  # Set the initial time in seconds
current_time = total_seconds

# Set up the clock
clock = pygame.time.Clock()
FPS = 1  # Adjust this value as needed for your game

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the timer based on FPS
    if current_time > 0:
        current_time -= 1 / FPS  # Decrement the timer based on FPS

    # Clear the screen
    window.fill(WHITE)

    # Render the timer text
    timer_text = font.render("{:.1f}".format(current_time), True, BLACK)  # Format time to one decimal place
    text_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(timer_text, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)  # Control the frame rate of the game

# Quit Pygame
pygame.quit()
sys.exit()
