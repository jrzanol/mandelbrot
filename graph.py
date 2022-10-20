from ctypes import *
from PIL import Image

# Carrega a DLL feita em C.
mandelbrotDll = CDLL("./mandelbrot.dll")

# Tamanho da imagem.
width = mandelbrotDll.getwidth()
height = mandelbrotDll.getheight()

# Cria uma imagem para ser usada como base para criar o grafico da fractal de mandelbrot.
img = Image.new('RGB', (width, height), "black")
graph = img.load()

for i in range(height):
    for j in range(width):
        # Chama a funcao da DLL para calcular o valor na posicao.
        value = mandelbrotDll.mandelbrot(i, j)
        
        # Define a cor utilizada dependendo do valor retornado.
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
            
        # Coloca na imagem a cor definida.
        graph[j,i] = color

# Exibe a imagem.
img.show()
