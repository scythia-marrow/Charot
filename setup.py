from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
from glob import glob
from os import path
from subprocess import run, PIPE

def gitFetch(name, url):
	if path.exists(name): return True
	print(f"{name} source not found, fetching...")
	result = run(f"git clone {url} {name}",shell=True)
	if result.returncode != 0:
		print(f'Could not fetch "{url}"')
		return False
	return True

if __name__ == "__main__":
	# Get source from github if needed
	gitSources = [
		("fantasyname","https://github.com/skeeto/fantasyname.git")
	]
	for name, url in gitSources:
		if not gitFetch(name, url): exit(-1)
	# Move headers to main directory
	header = glob("fantasyname/c/*.h")
	for head in header: run(f"cp {head} charot/",shell=True)
	# Bind the external FNG module
	FNGfiles = ['charot/namegenhook.cpp']
	FNGmodule = Pybind11Extension('namegen', FNGfiles)
	setup(name = 'FNG',
		description = 'A python wrapper for fantasyname',
		ext_modules = [FNGmodule])
	# After setup, move the library file(s) into the runtime directory
	libloc = glob("build/lib*/*")[0]
	run(f"cp {libloc} charot/", shell=True)
