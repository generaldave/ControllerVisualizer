################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# NES_Controller class: Handles NES controller                                 #
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
#                            NES_CONTROLLER CLASS                              #
#                                                                              #
################################################################################

class NES_Controller(Controller):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, screen : pygame.display, system : str, name : str, \
                 directory : str, position : point) -> None:
        super().__init__(screen, system, name, directory, position)

        self.create_button_images()

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Method creates and loads button images
    def create_button_images(self) -> None:
        path = self.image_directory
        self.button_images.append(pygame.image.load(path + 'b.png'))
        self.button_images.append(pygame.image.load(path + 'a.png'))
        self.button_images.append(pygame.image.load(path + 'select.png'))
        self.button_images.append(pygame.image.load(path + 'start.png'))
        self.button_images.append(pygame.image.load(path + 'd_up.png'))
        self.button_images.append(pygame.image.load(path + 'd_down.png'))
        self.button_images.append(pygame.image.load(path + 'd_left.png'))
        self.button_images.append(pygame.image.load(path + 'd_right.png'))

        super().create_button_images()

    # Method handles d-pad
    def axis_motion(self, axis : int, motion : int) -> None:
        # Handle left and right
            if (axis == zero):
                if (motion < zero):
                    self.visible_or_not(left, True)
                elif (motion > zero):
                    self.visible_or_not(right, True)
                else:
                    self.visible_or_not(left, False)
                    self.visible_or_not(right, False)

            # Handles up and down
            if (axis == one):
                if (motion < zero):
                    self.visible_or_not(up, True)
                elif (motion > zero):
                    self.visible_or_not(down, True)
                else:
                    self.visible_or_not(up, False)
                    self.visible_or_not(down, False)      
