'''
David Fuller

1/4/2018
1/10/2018 - Update: Joystick mapping
'''

import pygame

from .Constants import point


class N64(object):
    '''
    Sets up a Nintendo 64 controller class.
    '''
    
    def __init__(self, app_directory):
        '''
        N64's init method.

        Sets up button imagery for a Nintendo 64 controller.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.path = app_directory + '/images/n64/'
        self.gamepad = pygame.image.load(self.path + 'n64.png')
        self.position = point(x = 36, y = 5)

        self.stick_image = pygame.image.load(self.path + 'stick.png')
        self.stick_offset = point(x = 0, y = 0)

        self.button_images = []
        self.visible_buttons = []
        self.setup_button_images()

    def setup_button_images(self):
        '''
        Stores button images in an array and whether or not they are visible.
        '''
        
        path = self.path
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

        for i in range(len(self.button_images)):
            self.visible_buttons.append(False)

    def map(self, value, old_lower, old_upper, new_lower, new_upper):
        '''
        Maps a value from an old range into a new range.

        Args:
            value (int): Input value to map.
            old_lower (int): Lower boundary of old range.
            old_uppper (int): Upper boundary of old range.
            new_lower (int): Lower boundary of new range.
            new_lower (int): Lower boundary of new range.

        Returns:
            Int: The mapped value.
        '''
        
        old_range = old_upper - old_lower
        new_range = new_upper - new_lower
        return int(((value - old_lower) / old_range) * new_range + new_lower)

    def axis_motion(self, axis, motion):
        '''
        Decides the offset of the joystick.

        Args:
            axis (int): 0 = vertical axis. 1 = horizontal axis.
            motion (int): -1 < x < 1, -1 < y < 1.
        '''
        
        new_x = self.stick_offset.x
        new_y = self.stick_offset.y
        if axis == 1:
            if motion < 0:  # Up
                new_y = self.map(motion, 0, -1, 0, -5)
            else:   # Down
                new_y = self.map(motion, 0, 1, 0, 5)
        if axis == 0:
            if motion < 0:  # Left
                new_x = self.map(motion, 0, -1, 0, -5)
            else:   # Right
                new_x = self.map(motion, 0, 1, 0, 5)

        self.stick_offset = point(x = new_x, y = new_y)

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
                self.axis_motion(event.axis, event.value)
                interaction_made = True
        return interaction_made

    def show(self, surface):
        '''
        Shows the appropriate representation of the gamepad on screen.

        Args:
            surface (pygame.surface): Surface to draw on.
        '''
        
        surface.blit(self.gamepad, self.position)

        stick_position = point(x = self.position.x + self.stick_offset.x, \
                               y = self.position.y + self.stick_offset.y)
        surface.blit(self.stick_image, stick_position)

        for i in range(len(self.visible_buttons)):
            if self.visible_buttons[i] == True:
                surface.blit(self.button_images[i], self.position)
