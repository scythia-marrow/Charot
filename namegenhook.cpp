#include <pybind11/pybind11.h>
#include "namegen.h"
#include <stdio.h>

char* generateName(char* prompt, unsigned long seed)
{
	unsigned long buffsize = sizeof(char) * 256;
	char* buff = (char*)malloc(buffsize);
	namegen(buff,buffsize,prompt,&seed);
	return buff;
}


PYBIND11_MODULE(namegen, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("namegen", &generateName, "A function that generates a name");
}
