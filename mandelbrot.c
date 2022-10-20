// Ronei A. Zanol J.
// CLP

// Tamanho da Imagem.
const int width = 1024;
const int height = 800;

int getwidth() { return width; }
int getheight() { return height; }

// Coordenadas mínimas/máximas do gráfico.
const double xmin = -2.0;
const double xmax = 1.0;
const double ymin = -1.0;
const double ymax = 1.0;

// Função que gera o cálculo da fractal de mandelbrot.
int mandelbrot(int _i, int _j)
{
	double real = (xmin + (_j * ((xmax - xmin) / (width - 1))));
    double imag = (ymax - (_i * ((ymax - ymin) / (height - 1))));
	
	int limit = 100;
	double zReal = real;
	double zImag = imag;

	for (int i = 0; i < limit; ++i) {
		double r2 = zReal * zReal;
		double i2 = zImag * zImag;
		
		if (r2 + i2 > 4.0) return i;

		zImag = 2.0 * zReal * zImag + imag;
		zReal = r2 - i2 + real;
	}
	
	return limit;
}
