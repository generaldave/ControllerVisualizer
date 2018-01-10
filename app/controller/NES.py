'''
David Fuller

1/4/2018
'''

import pygame

from .Constants import point


class NES(object):
    '''
    Sets up a Nintendo controller class.
    '''
    
    def __init__(self, app_directory):
        '''
        NES's init method.

        Sets up button imagery for a Nintendo controller.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.path = app_directory + '/images/nes/'
        self.image = pygame.image.load(self.path + 'nes.png')
        self.position = point(x = 5, y = 23)

        self.button_images = []
        self.visible_buttons = []
        self.setup_button_images()

    def setup_button_images(self):
        '''
        Stores button images in an array and whether or not they are visible.
        '''
        
        path = self.path
        self.button_images.append(pygame.image.load(path + 'b.png'))
        self.button_images.append(pygame.image.load(path + 'a.png'))
        self.button_images.append(pygame.image.load(path + 'select.png'))
        self.button_images.append(pygame.image.load(path + 'start.png'))
        self.button_images.append(pygame.image.load(path + 'd_up.png'))
        self.button_images.append(pygame.image.load(path + 'd_down.png'))
        self.button_images.append(pygame.image.load(path + 'd_left.png'))
        self.button_images.append(pygame.image.load(path + 'd_right.png'))

        for i in range(len(self.button_images)):
            self.visible_buttons.append(False)

    def axis_motion(self, axis, motion):
        '''
        Decides whether up, down, left, or right is visible.

        Args:
            axis (int): 0 = vertical axis. 1 = horizontal axis.
            motion (int): -1 < x < 1, -1 < y < 1.
        '''
        
        # Handle left and right
        if axis == 0:
            if (motion < 0):
                self.visible_buttons[6] = True
            elif (motion > 0):
                self.visible_buttons[7] = True
            else:                
                self.visible_buttons[6] = False
                self.visible_buttons[7] = False

        # Handles up and down
        if axis == 1:
            if motion < 0:
                self.visible_buttons[4] = True
            elif motion > 0:
                self.visible_buttons[5] = True
            else:                
                self.visible_buttons[4] = False
                self.visible_buttons[5] = False

    def interaction(self, events):
        '''
        Decides what interaction with the gamepad was made.

        Args:
            events (pygame.events): Events received from gamepad.

        Returns:
            bool: True if there was an interaction. Otherwise False.
        '''
        
        interaction_made = False
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                self.visible_buttons[event.button] = True
                interaction_made = True
            if event.type == pygame.JOYBUTTONUP:
                self.visible_buttons[event.button] = False
                interaction_made = True
            if event.type == pygame.JOYAXISMOTION:
                self.axis_motion(event.axis, int(event.value))
                interaction_made = True
        return interaction_made

    def show(self, surface):
        '''
        Shows the appropriate representation of the gamepad on screen.

        Args:
            surface (pygame.surface): Surface to draw on.
        '''
            
        surface.blit(self.image, self.position)

        for i in range(len(self.visible_buttons)):
            if self.visible_buttons[i] == True:
                surface.blit(self.button_images[i], self.position)
