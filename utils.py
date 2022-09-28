import random

def pickWeight(value,weight):
	place = random.random() * sum(weight)
	for i,w in enumerate(weight):
		place -= w
		if(place < 0.0): return (i,value[i])
