Mandelbrot com Python e C.

Modo de Uso:
 Utilizar o comando make para a compilação da DLL e executar o arquivo Python.

Arquivos:
mandelbrot.c:
 Arquivo fonte em C que será compilado em uma DLL para ser chamado pelo
código do Python. O Código é do calculo da fractal de Mandelbrot.

graph.py:
 Arquivo fonte em Python que chama a DLL em C do cálculo da fractal de Mandelbrot e
gera a imagem colorida.

Makefile:
 Arquivo para compilar a DLL e executar o arquivo em Python para gerar a imagem.

Testes realizados com:
gcc (MinGW.org GCC-6.3.0-1) 6.3.0
Python 3.10.8 (32-bits)
MSYS 1.0
Windows 10

Pacotes do Python usados:
pip install numpy
pip install Pillow

Linha de comando para executar:
gcc -shared -o mandelbrot.dll mandelbrot.c
python graph.py
