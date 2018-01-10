'''
David Fuller

1/4/2018
'''

import pygame

from .NES import NES
from .N64 import N64


class Controller(object):
    '''
    Sets up a Controller class.
    '''
    
    def __init__(self, app_directory):
        '''
        Controller's init method.

        Decides whether or not a controller is plugged. If so, store one.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.controller = None
        try:
            pygame.joystick.init()
            gamepad = pygame.joystick.Joystick(0)
            gamepad.init()
            gamepad_name = gamepad.get_name()

            if gamepad_name == 'RetroUSB.com RetroPad' or \
               gamepad_name == 'Retr':
                self.controller = NES(app_directory)
            elif gamepad_name == 'SealieComputing N64 RetroPort' or \
                 gamepad_name == 'N64 ':
                self.controller = N64(app_directory)
        except:
            self.controller = None

    def interaction(self, events):
        '''
        Decides what interaction with the gamepad was made.

        Args:
            events (pygame.events): Events received from gamepad.

        Returns:
            bool: True if there was an interaction. Otherwise False.
        '''
        
        return self.controller.interaction(events)

    def show(self, surface):
        '''
        Shows the appropriate representation of the gamepad on screen,
        if one exists.

        Args:
            surface (pygame.surface): Surface to draw on.
        '''
        
        if self.controller:
            self.controller.show(surface)
        
