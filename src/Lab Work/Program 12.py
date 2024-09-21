import pygame

# Program to simulate a bouncing ball using Pygame

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Define colors and ball radius
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 20

# Main program loop
def main():
    clock = pygame.time.Clock()  # Initialize clock for controlling FPS
    run = True  # Flag to control the main loop
    x, y = WIDTH // 2, HEIGHT // 2  # Initial position of the ball
    dx, dy = 5, 5  # Velocity of the ball

    while run:
        clock.tick(60)  # Limit frame rate to 60 FPS
        win.fill(BLACK)  # Clear the screen

        # Update the position of the ball
        x += dx
        y += dy

        # Check for collision with the screen edges and reverse direction if needed
        if x - BALL_RADIUS < 0 or x + BALL_RADIUS > WIDTH:
            dx = -dx
        if y - BALL_RADIUS < 0 or y + BALL_RADIUS > HEIGHT:
            dy = -dy

        # Draw the ball
        pygame.draw.circle(win, WHITE, (x, y), BALL_RADIUS)

        pygame.display.update()  # Update the display

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Exit the loop if the window is closed

    pygame.quit()  # Quit Pygame

main()  # Start the simulation