from namegen import namegen
from gendergen import generateGender
from orientationgen import generateOrientation
import random

#NameTemplates
charotElvenStart='''\
(\
al|ar|ca|cir|ear|ell|elr|fro|gil|hal|ist|leg|lin|log|per|pip|pol|roh|vor|\
ae|al|an|are|ar|eo|es|fre|gal|hal|idr|li|lo|lu|mel|mor|nes|nien|ron|rin|ta|yav\
)\
'''

charotElvenMid='''\
(\
don|a|en|ad|ro|go|reg|e|th|an\
)\
'''

charotElvenEnd='''\
(\
don|gorn|od|lin|on|an|dil|dan|hir|and|do|dor|dir|ton|las|gon|grin|pin|den|we|\
ma|na|hel|wen|len|eth|wyn|tel|da|riel|leth|ril|ia|lia|ien|ian|sa|ra\
)\
'''

charotGeneralTemplate='''\
(\
<B>(<C>|)<V>(<s>|)(<V>|)\
)\
'''

charotVowelCluster='''\
(\
aa|ae|ai|aou|ath|\
eja|eh|eho|eu|eth|\
iah|i'a|ie|iou|ith|\
oah|o'a|ohe|oji|o'i|oh|ohu|oth|\
ua|ue|ui|uo|uh|uth|\
tha|the|thi|tho\
)\
'''

charotConsonantCluster='''\
(\
(\
qgch|qch|qsh|\
wt|wz|wd|wch|wsh|wb|\
rgh|rch|rph|rsh|rb|\
tz|tch|tsh|tb|\
ygh|yph|ysh|yb|\
pj|pf|psh|\
sgh|sz|sj|sph|sb|\
dch|dph|dz|db|\
fgh|fch|fn|fs|fz|fsh|fb|\
gch|gn|gz|gb|\
hj|hg|hj|hch|hz|hs|hn|hw|hq|hy|hb|\
jz|js|jn|jw|jy|jb|jgh|jch|jsh|jb\
kj|ks|kz|kgh|kch|kn|kw|kqu|kq'|ksh|kb|\
ln|lch|lgh|lw|lqu|lq'|ly|lsh|lb|\
zz|zsh|zp|zph|zn|zb|\
xn|xb|xgh|xw|\
ch|\
vn|vb|vw|vx|vgh|vch|vb|vj|vz|vs|vk|\
bn|bk|bz|bs|bgh|bch|bj|bsh|by|bq|bq'|bph|\
nq|nq'|nz|ns|ngh|nch|nm|ny|nph|\
mz|ms|mn|my|mt|mw|mgh|mch|mx|mph\
)\
|((q|w|r|t|y|p|a|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m)(l|v|m|'|r|))\
)\
'''

def namegenHook(template,seed = None):
	if not seed == None:
		random.seed(seed)
	return namegen(template, random.randint(0,1234362116))

def clusterTemplate(cluster):
	ret = ""
	for item in cluster: ret += item+"|"
	return "(" + ret[:-1] + ")"

def makeNameTemplate(seed = None):
	# Find a few vowel and consonant clusters
	clusterL = lambda x,y: set([namegenHook(x) for _ in range(y)])
	# Set the seed so that we get the same template each time
	random.seed(seed)
	# Create a linguistic style by slicing a subset of possible sounds
	concluster = clusterL(charotConsonantCluster,10)
	vowelcluster = clusterL(charotVowelCluster,10)
	# Get an arbitrary number of syllable parts
	cTemplate = clusterTemplate(concluster)
	vTemplate = clusterTemplate(vowelcluster)
	# Create a few name syllables for the beginning, middle, and end
	simpleSyllable = "(<s>|<cv>|<vc>)"
	complexSyllable = "(" + cTemplate + "<v>|" + vTemplate + "<c>" + ")"
	namePart = "(" + simpleSyllable + "|" + complexSyllable + ")"
	begTemplate = clusterTemplate(clusterL("(<B>|"+namePart+")",20))
	midTemplate = clusterTemplate(clusterL(vTemplate,40))
	endTemplate = clusterTemplate(clusterL("("+namePart+"|<V>)",10))
	return begTemplate, midTemplate, endTemplate

def generateName(style,seed = None):
	optL = lambda x: "(" + x + "|)"
	begin, middle, end = style
	finalTemplate = begin + optL(middle) + end
	return namegenHook(finalTemplate)

# Strategy: use a full namegen to get a set number of parts, then combine them
def charot(tSeed = None, nSeed = None, gSeed = None, oSeed = None):
	# Generate a name from the provided seed (or a new one)
	styleTemplate = makeNameTemplate(tSeed)
	name = generateName(styleTemplate, nSeed)
	gender = generateGender(gSeed)
	orientation = generateOrientation(next(iter(gender[0])),oSeed)
	return name,gender,orientation

if __name__=="__main__":
	print(charot())
