import pygame

from pygame.math import Vector2
from pygame import Rect

class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.color = color
        self.touched_by_ball = False


    def update(self, **kwargs):
        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass

class PaddleBlock(KineticBlock):

    def update(self, **kwargs):
        left = kwargs['left']
        right = kwargs['right']

        if left:
            self.position.x -= 10
        
        if right:
            self.position.x += 10
        
        self.rectangle = pygame.Rect(
            self.position.x - (self.rectangle.width/2),
            self.position.y - (self.rectangle.height/2),
            self.rectangle.width,
            self.rectangle.height,
        )

class MultipleBounceBlock(KineticBlock):
    # This block will chage colors each time the ball touch it
    # And will disappear after 4th hit
    pass


     

class SingleBounceBlock(KineticBlock):
    # This block will disappear after the ball touch it
    def update(self, **kwargs):
        if self.touched_by_ball:
            self.object_list.remove(self)
