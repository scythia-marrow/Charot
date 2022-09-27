#include <pybind11/pybind11.h>
#include "namegen.h"

char* generateName(char* prompt, unsigned long seed)
{
	char* buff = (char*)malloc(sizeof(char)*256);
	namegen(buff,sizeof(buff),prompt,&seed);
	return buff;
}


PYBIND11_MODULE(namegen, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("namegen", &generateName, "A function that generates a name");
}
