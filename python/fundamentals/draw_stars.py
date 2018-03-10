# Part 1

def draw_stars_only(list):
    for i in range(0, len(list)):
        starStr = ""
        for x in range(0, list[i]):
            starStr += "*"
        print starStr

# draw_stars_only([4,6,1,3,5,7,25])
# Working as intended!

# Part 2

def draw_stuff(list):
    for i in range(0, len(list)):
        starStr = ""
        letterStr = ""
        if type(list[i]) == int:
            for x in range(0, list[i]):
                starStr += "*"
            print starStr
        elif type(list[i]) == str:
            for y in range(0, len(list[i])):
                letterStr += list[i][0].lower()
            print letterStr        

draw_stuff([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

# Working as intended!