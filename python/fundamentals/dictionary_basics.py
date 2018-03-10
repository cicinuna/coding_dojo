jasons_info = {
    "name": "Jason Shin",
    "legal name": "Min Woo Shin",
    "age": 25,
    "country of origin": "South Korea",
    "favorite language": ["Matlab", "Python", "Ruby", "JavaScript"]
}

def dict_info(dict):
    # for key,val in dict.items():
    #     print "My "+str(key)+" is " +str(val)
    # Above code doesn't give me what i want in order

    for key in dict:
        print "My " + str(key)+ " is " + str(dict[key])
        # Now this returns keys not in order I want, but in another specific order. 
        # How to fix and get keys to list by my specific order?

# print jasons_info
dict_info(jasons_info)