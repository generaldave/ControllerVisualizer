'''
David Fuller

Constants file - File contains application constants.

10-15-2017
'''

from collections import namedtuple

color = namedtuple('color', ['r', 'g', 'b'])
resolution = namedtuple('resolution', ['width', 'height'])

background_color = color(r = 127, g = 127, b = 127)
screen_resolution = resolution(width = 200, height = 120)

app_title = "Visualizer"
fps = 60
