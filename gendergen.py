# Gender is expressed in a wild amount of cultural ways, that's awesome!
import random
from .utils import pickWeight

genderUmbrella = [
	("A","Agender"),
	("M","Masculine"),
	("F","Feminine"),
	("NB","Nonbinary"),
	("X","Third gender"),
	("Q","Genderqueer")
]
genderUmbrellaWeight = [4.0,30.0,31.0,20.0,2.0,5.0]

genderSpecific = [
	("D","Demi"),
	("GF","Genderfluid"),
	("BI","Bigender"),
	("I","Intersex"),
	("TR","Trans"),
	("SK","Sekhet"),
	("PR","Prakrti"),
	("GA","Galli"),
	("HI","Hijra"),
	("QU","Quariwarmi"),
	("TW","Twospirit"),
	("PH","Phaen"),
	("KH","Khalu"),
	("MU","Mahu"),
	("FA","Faafine"),
	("UR","Uranian"),
	("CH","Chibado"),
	("MN","Mangaiko"),
	("MA","Mashoga"),
	("AS","Ashrime"),
	("MO","Mollie"),
	("FE","Femminiello"),
	("TA","Tavestis"),
	("MX","Muxe"),
	("TI","Tidawena"),
	("BI","Bissu")
]

genderSpecificWeight = {
	"M" : (("TR",0.1),("D",0.2),("I",0.02)),
	"F" : (("TR",0.1),("D",0.2),("I",0.02)),
	"NB": (("GF",0.2),("BI",0.2),("D",0.1),("I",0.04),),
	"X" : (("SK",1.0),("PR",1.0),("GA",1.0),("HI",1.0),("QU",1.0),
		("TW",1.0),("PH",1.0),("KH",1.0),("MU",1.0),("FA",1.0),
		("UR",1.0),("CH",1.0),("MN",1.0),("MA",1.0),("AS",1.0),
		("MO",1.0),("FE",1.0),("TA",1.0),("MX",1.0),("TI",1.0),
		("BI",1.0),),
}

genderCompatible = [
	("D","I","GF","TR",)
]

pronoun = [
	("SH","She / Her"),
	("HE","He / Him"),
	("TH","They / Them"),
	("TN","Thon"),
	("XM","Xe / Xer"),
	("XF","Xe / Xim"),
	("TU","Thee / Thou"),
	("AL","Any / All"),
	("NO","None")
]

pronounWeight = {
	"M" : (("HE",1.0),),
	"F" : (("SH",1.0),),
	"A" : (("NO",5.0),("AL",1.0),),
	"NB" : (("TH",1.0),("TN",0.2),("XM",0.2),("XF",0.2),),
	"Q" : (("XM",1.0),("XF",1.0),("TN",1.0),("TH",1.0),("TU",1.0)),
	"X" : (("TH",1.0),("TN",1.0),("TU",1.0),("AL",1.0)),
	("M","D") : (("TH",2.0),("XM",1.0),("TN",0.5),),
	("F","D") : (("TH",2.0),("XF",1.0),("TN",0.5),),
	("M","I") : (("XM",0.5),),
	("F","I") : (("XF",0.5),),
	("NB","BI") : (("AL",1.0),),
	("NB","GF") : (("HE",2.0),("SH",2.0),),
}

# TODO: make it biased based off the description
def genderUmbrellaPick(weight=[]):
	pid,pick = pickWeight(genderUmbrella,genderUmbrellaWeight)
	return (pid,pick[0])

def genderSpecificPick(umbrella, weight=[]):
	# Add a none type with weight 1.0
	name = [None]
	weight = [1.0]
	if umbrella in genderSpecificWeight:
		for i,w in genderSpecificWeight[umbrella]:
			name.append(i)
			weight.append(w)
	# Pick two in case of overlapp
	pick1 = pickWeight(name,weight)
	picks = set([pick1[1]])
	# Some specific genders can overlap
	if pick1[1] in genderCompatible:
		pick2 = pickWeight(name,weight)
		picks.add(pick2[1])
	if None in picks: picks.remove(None)
	return picks

# TODO: pronoun overlap
def pronounPick(umbrella, specific, weight = []):
	choice = list(pronounWeight[umbrella])
	for spec in specific:
		pair = (umbrella,spec)
		if pair in pronounWeight:
			choice += pronounWeight[pair]
	name = [a for a,_ in choice]
	weight = [b for _,b in choice]
	pid,pick = pickWeight(name,weight)
	return (pid,pick)

def generateGender(seed = None):
	# set the seed if needed
	if not seed == None: random.seed(seed)
	# First, pick the gender umbrella
	guI,genderUmbrella = genderUmbrellaPick()
	# Next, pick a subset if wanted / needed
	genderSpecific = genderSpecificPick(genderUmbrella)
	pri,pronoun = pronounPick(genderUmbrella,genderSpecific)
	return set([genderUmbrella]),genderSpecific,set([pronoun])

if __name__ == "__main__":
	generateGender()
