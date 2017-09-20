################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# N64_Controller class: Handles N64 controller                                 #
#                                                                              #
# Created on 2017-9-20                                                         #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from   .Attributes import *            # Attributes file
from   .Controller import Controller   # Controller base clase
import pygame                          # For GUI

################################################################################
#                                                                              #
#                            N64_CONTROLLER CLASS                              #
#                                                                              #
################################################################################

class N64_Controller(Controller):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, screen : pygame.display, system : str, name : str, \
                 directory : str, position : point) -> None:
        super().__init__(screen, system, name, directory, position)

        self.create_button_images()

        self.stick_image = pygame.image.load(self.image_directory + \
                                             'stick.png')

        self.offset = point(x = zero, y = zero)

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Method creates and loads button image
    def create_button_images(self) -> None:
        path = self.image_directory
        self.button_images.append(pygame.image.load(path + 'd_right.png'))
        self.button_images.append(pygame.image.load(path + 'd_left.png'))
        self.button_images.append(pygame.image.load(path + 'd_down.png'))
        self.button_images.append(pygame.image.load(path + 'd_up.png'))
        self.button_images.append(pygame.image.load(path + 'start.png'))
        self.button_images.append(pygame.image.load(path + 'z.png'))
        self.button_images.append(pygame.image.load(path + 'b.png'))
        self.button_images.append(pygame.image.load(path + 'a.png'))
        self.button_images.append(pygame.image.load(path + 'c_right.png'))
        self.button_images.append(pygame.image.load(path + 'c_left.png'))
        self.button_images.append(pygame.image.load(path + 'c_down.png'))
        self.button_images.append(pygame.image.load(path + 'c_up.png'))
        self.button_images.append(pygame.image.load(path + 'r_trigger.png'))
        self.button_images.append(pygame.image.load(path + 'l_trigger.png'))

        super().create_button_images()

    # Method handles joystick motion
    def axis_motion(self, axis : int, motion : int) -> None:
        # Handle left and right
        if (axis == zero):
            if (motion < zero):
                self.offset = point(x = -five, y = zero)
            elif (motion > zero):
                self.offset = point(x = five, y = zero)
            else:                
                self.offset = point(x = zero, y = zero)

        # Handles up and down
        if (axis == one):
            if (motion < zero):
                self.offset = point(x = zero, y = -5)
            elif (motion > zero):
                self.offset = point(x = zero, y = five)
            else:
                self.offset = point(x = zero, y = zero)

    # Method draws joystick
    def update(self) -> None:
        super().update()
        position = point(x = self.position.x + self.offset.x, \
                         y = self.position.y + self.offset.y)
        self.screen.blit(self.stick_image, position)
