# Pre-defined values given from assignmet

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# Integer

def large_or_small(int):
    if int >= 100:
        print "That's a big number!"
    else:
        print "That's a small number!"

large_or_small(sI)
large_or_small(mI)
large_or_small(bI)
large_or_small(eI)
large_or_small(spI)

# String

def long_or_short(str):
    if len(str) >= 50:
        print "Long sentence"
    else:
        print "Short sentence"

long_or_short(sS)
long_or_short(mS)
long_or_short(bS)
long_or_short(eS)

# List

def big_or_small(list):
    if len(list) >= 10:
        print "Big List!"
    else:
        print "Short list."

big_or_small(aL)
big_or_small(mL)
big_or_small(lL)
big_or_small(eL)
big_or_small(spL)