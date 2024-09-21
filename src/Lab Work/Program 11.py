import pygame
import math

# Program to simulate elliptical orbits in Pygame

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elliptical Orbits")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw an orbiting object
def draw_orbit(x, y):
    pygame.draw.circle(win, WHITE, (int(x), int(y)), 5)

# Main program loop
def main():
    clock = pygame.time.Clock()  # Initialize clock for controlling FPS
    run = True  # Flag to control the main loop
    angle = 0  # Initial angle for orbit

    while run:
        clock.tick(60)  # Limit frame rate to 60 FPS
        win.fill(BLACK)  # Clear the screen

        # Calculate the position of the orbiting object
        x = WIDTH / 2 + 200 * math.cos(angle)
        y = HEIGHT / 2 + 100 * math.sin(angle)
        draw_orbit(x, y)  # Draw the orbiting object
        angle += 0.01  # Increment the angle for the next frame

        pygame.display.update()  # Update the display

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Exit the loop if the window is closed

    pygame.quit()  # Quit Pygame

main()  # Start the simulation