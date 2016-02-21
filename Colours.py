from __future__ import division
import re

RED = ('red', [1, 0, 0])
BLUE = ('blue', [0, 0, 1])
YELLOW = ('yellow', [1, 1, 0])
GREEN = ('green', [0, 1, 0])
PURPLE = ('purple', [1, 0, 1])
PINK = ('pink', [1, 0.31, 0.39])
ORANGE = ('orange', [1, 0.64, 0.26])
CYAN = ('cyan', [0, 1, 1])

BLACK = ('black', [0, 0, 0])
WHITE = ('white', [1, 1, 1])

COLOURS_LIST = [RED, BLUE, YELLOW, GREEN, PURPLE, PINK, ORANGE, CYAN, BLACK, WHITE]
COLOURS_DICT = dict(COLOURS_LIST)

HEX_PATTERN = '^#([A-Fa-f0-9]{6})$'
colour_regex = re.compile(HEX_PATTERN)

def is_hex_colour_code(colour_code):
    if colour_regex.match(colour_code):
        return True
    return False

def convert_hex_colour_code(colour_code):
    r = int(colour_code[1:3], 16)
    g = int(colour_code[3:5], 16)
    b = int(colour_code[5:7], 16)

    r /= 255
    g /= 255
    b /= 255

    return [r, g, b]





