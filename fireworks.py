import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size and background color
screen = pygame.display.set_mode((600, 400))
screen.fill((0, 0, 0))

# Run the simulation until the user closes the window
running = True
while running:
    # Draw a random colored circle at a random position on the screen
    x = random.randint(0, 600)
    y = random.randint(0, 400)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(screen, color, (x, y), 2)

    # Update the display
    pygame.display.flip()

    # Check for user input to stop the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
