all: mandelbrot.c
	gcc -shared -o mandelbrot.dll mandelbrot.c
	python graph.py

clean:
	rm -f mandelbrot.dll
