from namegen import namegen
from gendergen import generateGender
from orientationgen import generateOrientation
import random

def charot():
	name = namegen("Ba",random.randint(0,125264326))
	gender = generateGender()
	orientation = generateOrientation(next(iter(gender[0])))
	return name,gender,orientation

if __name__=="__main__":
	print(charot())
