########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# App class: App initializer                                           #
#                                                                      #
# Created on 2017-2-3                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants    import *          # Constants file
from   .controllers  import NES, N64   # Controllers package
from   pygame.locals import *          # For key presses
import pygame                          # For GUI

########################################################################
#                                                                      #
#                               APP CLASS                              #
#                                                                      #
########################################################################

class App(object):
    def __init__(self, appDirectory: str) -> None:
        self.appDirectory = appDirectory

        # Set up GUI
        self.setupGUI()

        # Run app
        self.runApp()

    # Mehtod sets up GUI
    def setupGUI(self) -> None:
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION, \
                                              pygame.NOFRAME)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()      # For frames per second
        self.mouse = pygame.mouse.get_pos()   # For mouse position
        pygame.joystick.init()
        self.gamepad = pygame.joystick.Joystick(0)
        self.gamepad.init()
        name = self.gamepad.get_name()
        

        # Decide which controller to show
        if name == NES_NAME:        
            directory = self.appDirectory + NES_IMAGE_PATH
            self.controller = NES(name, directory)
            self.controllerImg = pygame.image.load(self.controller.getImage())
            self.pos = POS_NES
                        
        elif name == N64_NAME:        
            directory = self.appDirectory + N64_IMAGE_PATH
            self.controller = N64(name, directory)
            self.controllerImg = pygame.image.load(self.controller.getImage())
            self.pos = POS_N64

        # Load controller images
        self.images = self.controller.loadImages()
        if name == N64_NAME:
            stickImg    = self.controller.getStickImage()
            self.stick  = pygame.image.load(stickImg)

    # Method runs app
    def runApp(self) -> None:
        offset = (0, 0)
        running = True
        while running:
            for event in pygame.event.get():
                
                # Handle quit event
                if (event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == K_ESCAPE)):
                    running = False

                # Handle joystick button presse
                if (event.type == pygame.JOYBUTTONDOWN):
                    self.controller.buttonPressed(event.button)

                # Handle joystick button release
                if (event.type == pygame.JOYBUTTONUP):
                    self.controller.buttonReleased(event.button)

                # Handle thumb stick
                if (event.type == JOYAXISMOTION):
                    # D-Pad on NES
                    if (self.controller.getType() == "NES"):
                        self.controller.axisMotion(event.axis, event.value)

                    # Stick on N64
                    elif (self.controller.getType() == "N64"):
                        offset = self.controller.axisMotion(event.axis, event.value)

            # Display controller with buttons pressed
            self.screen.blit(self.controllerImg, self.pos)
            self.visible = self.controller.getVisibleImages()
            for i in range(len(self.images)):
                if (self.visible[i]):
                    image = pygame.image.load(self.images[i])
                    self.screen.blit(image, self.pos)

            # N64 stick
            if (self.controller.getType() == "N64"):
                x = self.pos[ZERO] + offset[ZERO]
                y = self.pos[ONE]  + offset[ONE]
                pos = (x, y)
                self.screen.blit(self.stick, pos)
                

            # Update Screen
            pygame.display.update()
            self.clock.tick(FPS)            

        # Close app cleanly
        pygame.quit()
