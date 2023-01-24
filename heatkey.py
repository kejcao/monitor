from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageChops, ImageEnhance

from data import kall

coords = {
    'KEY_TILDE': (25, 136),
    'KEY_1': (125, 136),
    'KEY_2': (225, 136),
    'KEY_3': (325, 136),
    'KEY_4': (425, 136),
    'KEY_5': (525, 136),
    'KEY_6': (625, 136),
    'KEY_7': (725, 136),
    'KEY_8': (825, 136),
    'KEY_9': (925, 136),
    'KEY_0': (1025, 136),
    'KEY_MINUS': (1125, 136),
    'KEY_EQUAL': (1225, 136),
    'KEY_BACKSPACE': (1375, 136),
    'KEY_TAB': (50, 233),
    'KEY_Q': (174, 233),
    'KEY_W': (278, 233),
    'KEY_E': (378, 233),
    'KEY_R': (478, 233),
    'KEY_T': (578, 233),
    'KEY_Y': (678, 233),
    'KEY_U': (778, 233),
    'KEY_I': (878, 233),
    'KEY_O': (978, 233),
    'KEY_P': (1078, 233),
    'KEY_LEFTBRACE': (1178, 233),
    'KEY_RIGHTBRACE': (1278, 233),
    'KEY_BACKSLASH': (1378, 233),
    'KEY_CAPSLOCK': (75, 329),
    'KEY_A': (200, 329),
    'KEY_S': (300, 329),
    'KEY_D': (400, 329),
    'KEY_F': (500, 329),
    'KEY_G': (600, 329),
    'KEY_H': (700, 329),
    'KEY_J': (800, 329),
    'KEY_K': (900, 329),
    'KEY_L': (1000, 329),
    'KEY_SEMICOLON': (1100, 329),
    'KEY_APOSTROPHE': (1200, 329),
    'KEY_ENTER': (1350, 329),
    'KEY_LEFTSHIFT': (100, 425),
    'KEY_Z': (250, 425),
    'KEY_X': (350, 425),
    'KEY_C': (450, 425),
    'KEY_V': (550, 425),
    'KEY_B': (650, 425),
    'KEY_N': (750, 425),
    'KEY_M': (850, 425),
    'KEY_COMMA': (950, 425),
    'KEY_PERIOD': (1050, 425),
    'KEY_SLASH': (1150, 425),
    'KEY_RIGHTSHIFT': (1300, 425),
    'KEY_LEFTCTRL': (75, 522),
    'KEY_LEFTMETA': (175, 522),
    'KEY_LEFTALT': (300, 522),
    'KEY_SPACE': (700, 522),
}

for key, (x,y) in coords.items():
    coords[key] = (x//50, y//50)

heatmap = np.zeros((643//50, 2227//50))
for key, freq in Counter(kall).most_common():
    try:
        x, y = coords[key]
        heatmap[y:y+2, x:x+2] = min(freq, sum(kall.values())/len(kall)*2)
    except KeyError:
        pass

plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.imshow(heatmap, interpolation='lanczos', cmap='hot')
plt.savefig('/tmp/heatmap.png', pad_inches=0, bbox_inches='tight')
Image.blend(
    Image.open('/tmp/heatmap.png').convert('RGB').resize((2227, 643)),
    Image.open('keyboard.jpeg').convert('RGB'), .4
).save('heatmap.png')
plt.imshow(plt.imread('heatmap.png'))
plt.show()
