################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# Controller class: Handles displaying of approrpriate controller and buttons  #
#                   pushed                                                     #
#                                                                              #
# Created on 2017-9-20                                                         #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from   .Attributes import *   # Attributes file
import pygame                 # For GUI

################################################################################
#                                                                              #
#                              CONTROLLER CLASS                                #
#                                                                              #
################################################################################
 
class Controller(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, screen : pygame.display, system : str, name : str, \
                 directory : str, position : point) -> None:
        self.screen = screen
        self.position = position
        self.system = system
        self.name = name
        self.image_directory = directory + '/images/' + self.system + '/'
        self.controller_image = pygame.image.load(self.image_directory + \
                                                  self.system + '.png')
        self.button_images = []
        self.visible = []

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################  

    # Loads button images
    def create_button_images(self) -> None:
        for element in self.button_images:
            self.visible.append(None)

    # Decides what images should be visible
    def visible_or_not(self, button : int, make_visible : bool) -> None:
        if make_visible:
            self.visible[button] = self.button_images[button]
        else:
            self.visible[button] = None

    # Handles button presses
    def button_pressed(self, button : int) -> None:
        self.visible_or_not(button, make_visible = True)

    # Handles button releases
    def button_released(self, button : int) -> None:
        self.visible_or_not(button, make_visible = False)

    # Do this in subclass
    def axis_motion(self, axis : int, motion : int) -> None:
        pass            

    # Display visible images
    def update(self):
        self.screen.blit(self.controller_image, self.position)
        for image in self.visible:
            if image != None:
                self.screen.blit(image, self.position)
            
