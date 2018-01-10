'''
David Fuller

App class: Initializes application

10-15-2017
'''

import pygame

from .Constants import *
from .controller import Controller


class App(object):
    '''
    Sets up and runs a Pygame application.
    '''
    
    def __init__(self, app_directory):
        '''
        App's init method.

        Stores application directory. Sets up the graphical user interface.
        Runs the applicaiton.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.app_directory = app_directory

        self.setup_GUI()

        self.run_app()

    def setup_GUI(self):
        '''
        Method sets up the graphical user interface.

        Initializes Pygame. Sets up the window size and title. Stores Pygame
        clock variable for setting frames per second.
        '''
        
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption(app_title)
        self.clock = pygame.time.Clock()

        self.controller = Controller(self.app_directory)

    def run_app(self):
        '''
        Runs Pygame application.
        '''

        alt_down = False
        initial_render = False
        rendered = False
        running = True

        if self.controller.controller == None:
            print('No controller found. Exiting application')
            running = False
            
        while running:
            events = pygame.event.get()
            for event in events:
                
                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

                # Handle ALT + F4
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LALT:
                        alt_down = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F4 and alt_down == True:
                        running = False
                    if event.key == pygame.K_LALT:
                        alt_down = True

                # Set rendered to false if there is a new interaction
                # with a gamepad
                else:
                    rendered = not self.controller.interaction(events)

            # Only redraw screen if there is a change
            if rendered == False or initial_render == False:
                self.screen.fill(background_color)
                self.controller.show(self.screen)
                rendered = True
                initial_render = True

            # Update Screen
            pygame.display.update()
            self.clock.tick(fps)            

        # Close app cleanly
        pygame.quit()
