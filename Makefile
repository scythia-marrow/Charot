PYTHONFILES=$(shell python3 -m pybind11 --includes)
SUFFIX=$(shell python3-config --extension-suffix)

namegen.h:
	cp fantasyname/c/*.h components/

pythonhook: namegen.h
	c++ -O3 -Wall -shared -std=c++11 -fPIC $(PYTHONFILES) components/namegenhook.cpp -o namegen$(SUFFIX)
	mv *.so components
all: pythonhook
clean:
	rm components/*.so components/*.h
