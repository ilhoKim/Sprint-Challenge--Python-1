import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *
# from paddle import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    #Vector2(10*random.random() - 2, 10*random.random() - 2),
                                    Vector2(8, 8),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    for i in range(10):
        singleBounceBlock = SingleBounceBlock(Vector2(40*i,400), 39, 39, [0, 0, 255])
        object_list.append(singleBounceBlock)
    
    # block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    # object_list.append(block)

    paddle = PaddleBlock(Vector2(200,700), 100, 30, [255, 0, 0])
    object_list.append(paddle)

    multipleBounceBlock = MultipleBounceBlock(Vector2(200,300), 50, 50, [0, 0, 255])
    object_list.append(multipleBounceBlock)



def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            object.update(left = left, right = right) # move paddle
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
