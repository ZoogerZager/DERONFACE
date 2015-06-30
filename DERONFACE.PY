"""

Happy Birthday Program for a friend. Made with Pygame.

"""
 
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Deron:
    def __init__(self, image, x, y, change_x, change_y):
        self.image = image
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
    
    def draw(self):
        screen.blit(self.image, [self.x, self.y])
        
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        
pygame.init()

# Set the width and height of the screen [width, height]
size = (327, 410)
screen = pygame.display.set_mode(size)

dron_one = pygame.image.load('DERON.png').convert()
dron_two = pygame.image.load('DERONu.png').convert()
dron_three = pygame.image.load('DERONl.png').convert()
dron_four = pygame.image.load('DERONr.png').convert()
images = [dron_one, dron_two, dron_three, dron_four]
for image in images:
    image.set_colorkey(WHITE)
    
bg_music = pygame.mixer.music.load('bgmusic.ogg')
pygame.mixer.music.play()
    
background_image = pygame.image.load('DERON.jpg').convert()

 
pygame.display.set_caption("DERONFACE")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

deron_list = []
for dron in range(20): 
    my_object = Deron(random.choice(images), random.randint(0, size[0]), random.randint(0, size[1]), random.randint(-2, 2), random.randint(-2, 2))
    deron_list.append(my_object)
    
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
    
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    screen.fill(BLACK)
    screen.blit(background_image, [0, 0])
    
    for dron in deron_list:
        dron.draw()
        dron.move()
        if dron.x < 0 or dron.x > size[0]:
            dron.change_x *= -1
        if dron.y < 0 or dron.y > size[1]:
            dron.change_y *= -1
        
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()