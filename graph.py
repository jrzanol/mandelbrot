from ctypes import *
import numpy

import numpy as np
from PIL import Image

# Carrega a DLL feita em C.
mandelbrotDll = CDLL("./mandelbrot.dll")

# Tamanho.
width = mandelbrotDll.getwidth()
height = mandelbrotDll.getheight()

img = Image.new('RGB', (width, height), "black") # Create a new black image
graph = img.load() # Create the pixel map

for i in range(height):
    for j in range(width):
        value = mandelbrotDll.mandelbrot(i, j)
        color = (0, 0, 0)
        
        if (value == 100):
            color = (0, 0, 0)
        elif (value > 90):
            color = (255, 0, 0)
        elif (value > 70):
            color = (139, 0, 0)
        elif (value > 50):
            color = (255,165,0)
        elif (value > 30):
            color = (255,255,204)
        elif (value > 20):
            color = (124,252,0)
        elif (value > 10):
            color = (0, 255, 0)
        elif (value > 5):
            color = (224,255,255)
        elif (value > 4):
            color = (0,255,255)
        elif (value > 3):
            color = (0, 0, 255)
        elif (value > 2):
            color = (137, 207, 240)
        elif (value > 1):
            color = (255,0,255)
        else:
            color = (200,0,200)
            
        graph[j,i] = color

img.show()
