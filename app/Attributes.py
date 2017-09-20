################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# Attributes file                                                              #
#                                                                              #
# Created on 2017-9-20                                                         #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              SCREEN ATTRIBUTES                               #
#                                                                              #
################################################################################

from collections import namedtuple

resolution        = namedtuple('resolution', ['width', 'height'])
point             = namedtuple('point', ['x', 'y'])

screen_resolution = resolution(width = 200, height = 128)

application_title = "Visualizer"
FPS               = 60

################################################################################
#                                                                              #
#                            CONTROLLER ATTRIBUTES                             #
#                                                                              #
################################################################################

name  = namedtuple('name', ['NES', 'N64'])
point = namedtuple('point', ['x', 'y'])
colour = namedtuple('colour', ['r', 'g', 'b'])

background_colour = colour(r = 0, g = 0, b = 0)

controller = name(NES = 'RetroUSB.com RetroPad', \
                  N64 = 'SealieComputing N64 RetroPort')

NES_position = point(x = 5, y = 23)
N64_position = point(x = 36, y = 5)

NES = 'nes'
N64 = 'n64'

################################################################################
#                                                                              #
#                              NUMBER ATTRIBUTES                               #
#                                                                              #
################################################################################

zero = 0
