import pygame
import random 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0) 

def random_color():
	return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")
x_speed= 5
y_speed= 5 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

screen=pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))





# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen.fill(WHITE)

class Circle(): 
	def _init_(self,mouse_position):
		self.mouse_position = mouse_position
		self.x_pos = mouse_position[0] 
		self.y_pos = mouse_position[1]
		
	def draw (self):
		global screen 
		global Red
		pygame.draw.circle(screen,RED,self.mouse_position,20)
	def move(self,x_speed,y_speed,x_pos,y_pos):
		self.x_speed = x speed 
		self.y_speed = y speed 
		self.x_pos += x_pos
		self.y_pos += y_pos
		
circle_list = []

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	pressed = pygame.mouse.get_pressed()
	mouse_position= pygame.mouse.get_pos()
	
	if pressed[0] == 1:
		print ("here!")
		circle = circle(mouse _position)
		circle_list.append(circle)
		#class is just a blueprint 
		circles.draw()
		circles.move(x_speed,y_speed)
		
	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(WHITE)

	# --- Drawing code should go here

	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()


	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE