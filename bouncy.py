import sys
import pygame

# start running pygame
pygame.init()

width, height = 800, 600
# speed is a list because values need to be able to change
speed = [1, 1]
# colors are tuples because values don't change
black = (0, 0, 0)
white = (255, 255, 255)

# Create a display. The size must be a tuple providing width and height
screen = pygame.display.set_mode( (width, height) )

# Load an image
plane = pygame.image.load("img/plane.png")
planerect = plane.get_rect()

while True:
    # loop through every event in the event queue
    for event in pygame.event.get():
        # if the QUIT event happens, exit the program
        if event.type == pygame.QUIT:
            sys.exit()
    
    planerect = planerect.move(speed)
    if planerect.left < 0 or planerect.right > width:
        speed[0] *= -1
    if planerect.top < 0 or planerect.bottom > height:
        speed[1] *= -1

    # Fill the screen with white
    screen.fill(white)
    # Draw the plane with the size and location specified by planerect
    screen.blit(plane, planerect)
    # Update the display
    pygame.display.flip()