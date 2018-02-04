# Import a library of functions called 'pygame'
import pygame
from math import pi
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [512,512]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sierpinski triangle")

def sierpinski(top, left, size):
	size12 = size/2
	size14 = size/4
	size34 = 3*size/4
	if (size <=4):
		pygame.draw.polygon(screen, BLACK, [[left+size12, top], [left, top+size], [left+size, top+size]], 1)
	else:
		sierpinski(top, left+size14, size12)
		sierpinski(top+size12, left, size12)
		sierpinski(top+size12, left+size12, size12)


#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
	# This limits the while loop to a max of 10 times per second.
	# Leave this out and we will use all CPU we can.
	clock.tick(10)
	 
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # Flag that we are done so we exit this loop
						
	# All drawing code happens after the for loop and but
	# inside the main while done==False loop.
	 
	# Clear the screen and set the screen background
	screen.fill(WHITE)
	sierpinski(0, 0, 512)

	# Go ahead and update the screen with what we've drawn.
	# This MUST happen after all the other drawing commands.
	pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
