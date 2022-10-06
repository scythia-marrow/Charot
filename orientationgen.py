# People are weird and wild in their sexuality! Let's celebrate it!
import random
from utils import pickWeight

# TODO put these in files, make a more general topology-based algorithm
orientationTypes = [
	('S',"Sexual"),
	('R',"Romantic"),
	('A',"Aesthetic")
]

directionTypes = [
	('M',"Masculine"),
	('F',"Feminine"),
	('BI',"Bi"),
	('A',"Ace"),
]

orientationGenderTerms = [
	('HE',"Hetero-"),
	('HO',"Homo-"),
	('G',"Gay"),
	('S',"Straight"),
	('Q',"Queer"),
	('D',"Demi-"),
	('L',"Lesbian"),
	('SA',"Sapphic"),
	('AC',"Achillean"),
	('P',"Pan-"),
	('O',"Omni-"),
	('A',"A-"),
	('BI',"Bi-")
]

orientationPrefix = [
	('A',"A-"),
	('BI',"Bi-"),
	('HO',"Homo-"),
	('HE',"Hetero-")
]

orientationGenderMap = {
	('M','HE') : ['S'],
	('M','HO') : ['AC','Q','G'],
	('F','HE') : ['S'],
	('F','HO') : ['SA','L','Q','G'],
	'BI' : ['HO','HE','P','O'],
	'NB' : ['Q','G'],
	'Q' : ['Q'],
	'A' : ['Q','A','D']
}

correlations = [
	('D','HE'),
	('D','HO'),
	('D','BI')
]

# Weights for each term
typeCorrelation = [25.0,25.0,25.0,25.0]
orientationPrefixWeight = [3.0,3.0,3.0,10.0]
orientationSubtermWeight = {
	'Q' : 1.0,
	'A' : 2.0,
	'D' : 2.0,
	'G' : 5.0,
	'P' : 1.0,
	'O' : 0.2,
	'S' : 10.0,
	'SA' : 2.0,
	'AC' : 2.0,
	'L' : 1.0
}
correlationWeight = {
	('D','HE') : 3.0,
	('D','HO') : 1.0,
	('D','BI') : 1.0
}

def attractionToLabel(umbrella,gender=None):
	# Use gender to transform attraction into a label... That's deep...
	label = []
	for typ,umb in umbrella:
		applicableTerms = [umb[0]]
		if umb[0] in orientationGenderMap:
			applicableTerms += orientationGenderMap[umb[0]]
		if gender in orientationGenderMap:
			applicableTerms += orientationGenderMap[gender]
		gendTup = (gender, umb[0])
		if gendTup in orientationGenderMap:
			applicableTerms += orientationGenderMap[gendTup]
		for term in applicableTerms:
			if term in applicableTerms: continue
			termTup = (gender, term)
			if term in orientationGenderMap:
				applicableTerms += orientationGenderMap[term]
			if termTup in orientationGenderMap:
				applicableTerms += orientationGenderMap[termTup]
		# Generate weights for the applicable terms
		appWeight = []
		for term in applicableTerms:
			if term in orientationSubtermWeight:
				appWeight += [orientationSubtermWeight[term]]
			else:
				appWeight += [1.0]
		i,term = pickWeight(applicableTerms,appWeight)
		for char,lab in orientationGenderTerms:
			if term == char: label += [(char,lab)]
	return label

# Return an orientation
def generateOrientation(gender=None,seed=None):
	# Set seed if needed
	if not seed == None: random.seed(seed)
	# First generate umbrellas for each type of attraction
	umbrella = []
	# Generate identities the character is attracted to
	bias = None
	biasedWeight = [x for x in orientationPrefixWeight]
	for typ in orientationTypes:
		# Correlate different orientations
		if not bias == None:
			biasedWeight[bias] += typeCorrelation[bias]
		bias,ori = pickWeight(orientationPrefix, biasedWeight)
		# Great we did it for all
		umbrella += [(typ,ori)]
	# Generate specific labels
	label = attractionToLabel(umbrella, gender)
	sub = []
	# Generate detailed labels if needed
	for idl,lab in label:
		corr = [None]
		corrW = [0.0]
		for correlation in correlations:
			if idl == correlation[0]:
				corr += [correlation]
				corrW += [correlationWeight[correlation]]
		subCorr = pickWeight(corr,corrW)
		if subCorr != None:
			sub += attractionToLabel([subCorr[1]],gender)
	return label,sub

if __name__ == "__main__":
	print("OUTPUT:",generateOrientation())
	print("OUTPUT:",generateOrientation('M'))
	print("OUTPUT:",generateOrientation('F'))
	print("OUTPUT:",generateOrientation('NB'))
	print("OUTPUT:",generateOrientation('Q'))
	print("OUTPUT:",generateOrientation('X'))
