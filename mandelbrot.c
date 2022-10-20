// Ronei A. Zanol J.
// CLP

const int width = 1024;
const int height = 800;

const double xmin = -2.0;
const double xmax = 1.0;
const double ymin = -1.0;
const double ymax = 1.0;

int basemandelbrot(double real, double imag) {
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

__declspec(dllexport) int mandelbrot(int _i, int _j)
{
	double r = (xmin + (_j * ((xmax - xmin) / (width - 1))));
    double i = (ymax - (_i * ((ymax - ymin) / (height - 1))));
	
	return basemandelbrot(r, i);
}

__declspec(dllexport) int getwidth()
{
	return width;
}

__declspec(dllexport) int getheight()
{
	return height;
}
