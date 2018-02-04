# Import a library of functions called 'pygame'
import pygame, random
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
size = [512, 512]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Barnsley fern")

def scale(x, y, size):
	h = (x + 2.182)*(size - 1)/4.8378
	k = (9.9983 - y)*(size - 1)/9.9983
	return h, k
	
def transform(x,y):
	rand = random.uniform(0, 100)
	if rand < 1:
		return 0, 0.16*y
	elif 1 <= rand < 86:
		return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
	elif 86 <= rand < 93:
		return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
	else:
		return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

v = [0.0, 0.0]

#Loop until the user clicks the close button.
done = False

# Clear the screen and set the screen background
screen.fill(WHITE)
for i in range(50000):
	pygame.draw.rect(screen, GREEN, [int((v[0] + 2.182)*(512-1)/4.8378),int((9.9983 - v[1])*(512- 1)/9.9983), 2, 2],1)
	v = transform(v[0],v[1])

pygame.display.update()

while not done:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # Flag that we are done so we exit this loop
						
	# All drawing code happens after the for loop and but
	# inside the main while done==False loop.	 
	
# Be IDLE friendly
pygame.quit()
