################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# App class: App initializer                                                   #
#                                                                              #
# Created on 2016-12-29                                                        #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from   .controllers  import NES_Controller   # NES controller class
from   .controllers  import N64_Controller   # N64 controller class
from   .Attributes   import *                # Attributes file
from   pygame.locals import *                # For button pressesss
import pygame                                # For GUI

################################################################################
#                                                                              #
#                                   APP CLASS                                  #
#                                                                              #
################################################################################

class App(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, appDirectory: str) -> None:
        self.appDirectory = appDirectory

        # Set up GUI
        self.setupGUI()

        # Run app
        self.runApp()

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Mehtod sets up GUI
    def setupGUI(self) -> None:
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption(application_title)
        self.clock = pygame.time.Clock()   # For frames per second

        # Joystick
        try:
            pygame.joystick.init()
            self.gamepad = pygame.joystick.Joystick(zero)
            self.gamepad.init()
            gamepad_name = self.gamepad.get_name()

            # Decide which controller to show
            self.controller = NES_Controller(screen = self.screen, \
                                  system = NES, name = gamepad_name, \
                                  directory = self.appDirectory, \
                                  position = NES_position) \
                              if gamepad_name == controller.NES else \
                              N64_Controller(screen = self.screen, \
                                  system = N64, name = gamepad_name, \
                                  directory = self.appDirectory, \
                                  position = N64_position)
        except:
            self.controller = None

    # Method runs app
    def runApp(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                
                # Handle quit event
                if (event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == K_ESCAPE)):
                    running = False

                # Handle joystick button presse
                if (event.type == pygame.JOYBUTTONDOWN):
                    self.controller.button_pressed(event.button)

                # Handle joystick button release
                if (event.type == pygame.JOYBUTTONUP):
                    self.controller.button_released(event.button)

                # Handle thumb stick
                if (event.type == JOYAXISMOTION):
                    self.controller.axis_motion(event.axis, event.value)

            # Background is black
            self.screen.fill(background_colour)

            # Update controller imagery
            if self.controller:
                self.controller.update()
            else:
                running = False
                print('No controller')

            # Update Screen
            pygame.display.update()
            self.clock.tick(FPS)            

        # Close app cleanly
        pygame.quit()
