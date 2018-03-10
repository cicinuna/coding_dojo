def odd_or_even(start, end):
    for i in range(start, end+1):
        if i%2 == 0:
            print "The number is: " + str(i) + ". This is an even number."
        else:
            print "The number is: " + str(i) + ". This is an odd number."

# odd_or_even(1,2000)
# works as intended!

def multiply_list(list, num):
    new_list = []
    for i in range(0, len(list)):
        new_list.append(list[i]*num)
    return new_list

# print multiply_list([2,4,10,16], 5)
# works as intended!

def layered(list):
    new_list = []
    for i in range(0, len(list)):
        small_list = []
        for x in range(0, list[i]):
            small_list.append(1)
        new_list.append(small_list)
    return new_list

print layered(multiply_list([2,4,5],3))

#works as intended!
