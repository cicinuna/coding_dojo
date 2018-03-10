import sys

def checkerboard():
    star_first = "* * * * "
    space_first = " * * * *"
    for i in range(0, 8):
        # print "are we here"
        if i % 2 == 0:
            # print "here yet?"
            print star_first
        else:
            print space_first
# Is this cheat?

# checkerboard()

def noCheat():
    for i in range(0, 8):
        for x in range(0, 4):
            if i % 2 == 0:
                sys.stdout.write('* ')
            else:
                sys.stdout.write(' *')
        print ""
noCheat()

# ??

#