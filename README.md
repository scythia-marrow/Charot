# Charot

A generator for creating fantasy characters with tons of options
including names, gender, and sexuality.
This generator runs the backend of the app at
[scythiamarrow.org](https://scythiamarrow.org/app/createcharacter).

## Credits

Charot generates names using custom templates passed to the fantastic
fantasy name generator by [skeeto](https://github.com/skeeto/fantasyname).

## Installation

Charot uses python setuptools to install. Simply download the source code with
git, then setup with python.

```
git clone https://github.com/scythia-marrow/Charot.git

cd Charot

python3 setup.py build
```

## Use

Charot can be imported from the built "charot" package

```
from charot import charot
character = charot.charot() #returns a name, gender, orientation tuple
```

Charot can also be run directly from python, which will print a character
to the command line.

```
python3 test.py
```

## Plans

Creating characters using text prompt keyword information.

Style, race, class, origin locations, and backstories.

Automatic character portraits using stable diffusion.

## Thanks for reading
Love you!
