name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

challenge_name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Jason", "Bosco", "Nick", "Stephanie"]
challenge_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    unused = []
    new_dict = []

    if len(arr1) > len(arr2):
        for i in range(len(arr2), len(arr1)):
            unused.append(arr1[i])
        print "Unused keys were: " + str(unused)
    else:
        for i in range(len(arr1), len(arr2)):
            unused.append(arr2[i])
        print "Unused keys were: " + str(unused)

    new_dict = zip(arr1, arr2)
    new_dict = dict(new_dict)
    print new_dict

# print make_dict(name, favorite_animal)

make_dict(challenge_name, challenge_animal)
# make_dict(challenge_animal, challenge_name)


# def challenge(arr1, arr2):
#     key = []
#     new_dict = []
#     if len(arr1) > len(arr2):
#         key = arr1
        
#     elif len(arr2) > len(arr1):
#         key = arr2
#     else:

