<b>Mandelbrot com Python e C.</b>

<b>Modo de Uso:</b><br>
Utilizar o comando make para a compilação da DLL e executar o arquivo Python.

<b>Arquivos:</b><br>
<b>mandelbrot.c:</b><br>
 Arquivo fonte em C que será compilado em uma DLL para ser chamado pelo
código do Python. O Código é do calculo da fractal de Mandelbrot.

<b>graph.py:</b><br>
 Arquivo fonte em Python que chama a DLL em C do cálculo da fractal de Mandelbrot e
gera a imagem colorida.

<b>Makefile:</b><br>
 Arquivo para compilar a DLL e executar o arquivo em Python para gerar a imagem.

<b>doc.pdf:</b><br>
 Arquivo com a documentação do programa.

<b>Testes realizados com:</b><br>
gcc (MinGW.org GCC-6.3.0-1) 6.3.0<br>
Python 3.10.8 (32-bits)<br>
MSYS 1.0<br>
Windows 10<br>

<b>Pacotes do Python usados:</b><br>
pip install Pillow<br>

<b>Linha de comando para executar:</b><br>
gcc -shared -o mandelbrot.dll mandelbrot.c<br>
python graph.py
