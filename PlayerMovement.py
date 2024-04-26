import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player properties
PLAYER_SIZE = 50
player_x = SCREEN_WIDTH // 2 - PLAYER_SIZE // 2
player_y = SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2
player_speed = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Maze Game')

# Player rectangle
player = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)

def move_player(keys_pressed):
    if keys_pressed[pygame.K_LEFT]:
        player.x -= player_speed
    if keys_pressed[pygame.K_RIGHT]:
        player.x += player_speed
    if keys_pressed[pygame.K_UP]:
        player.y -= player_speed
    if keys_pressed[pygame.K_DOWN]:
        player.y += player_speed

    # Check boundaries to prevent player from going out of screen
    if player.x < 0:
        player.x = 0
    if player.x > SCREEN_WIDTH - PLAYER_SIZE:
        player.x = SCREEN_WIDTH - PLAYER_SIZE
    if player.y < 0:
        player.y = 0
    if player.y > SCREEN_HEIGHT - PLAYER_SIZE:
        player.y = SCREEN_HEIGHT - PLAYER_SIZE

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys_pressed = pygame.key.get_pressed()

    # Move player
    move_player(keys_pressed)

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, player)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# import pygame
# import sys

# # Initialize pygame
# pygame.init()

# # Create a window
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Update Specific Surface')

# # Create two surfaces
# surface1 = pygame.Surface((200, 200))
# surface1.fill((255, 0, 0))  # Fill with red color
# surface2 = pygame.Surface((200, 200))
# surface2.fill((0, 255, 0))  # Fill with green color

# # Blit the surfaces to the screen
# screen.blit(surface1, (100, 100))
# screen.blit(surface2, (150, 150))  # Part of surface2 overlaps with surface1

# # Update the display
# pygame.display.flip()

# # Wait for a moment
# pygame.time.wait(2000)

# # Change the color of surface1
# surface1.fill((0, 0, 255))  # Fill with blue color

# # Update only the area occupied by surface1
# # This will not affect surface2 or any other area of the screen
# screen.blit(surface1, (100, 100))
# pygame.display.update((100, 100, 200, 200))  # Update the rectangle occupied by surface1

# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()
# sys.exit()
