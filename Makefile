PYTHONFILES=$(shell python3 -m pybind11 --includes)
SUFFIX=$(shell python3-config --extension-suffix)

namegen.h:
	cp fantasyname/c/*.h .

pythonhook: namegen.h
	c++ -O3 -Wall -shared -std=c++11 -fPIC $(PYTHONFILES) namegenhook.cpp -o namegen$(SUFFIX)

all: pythonhook
