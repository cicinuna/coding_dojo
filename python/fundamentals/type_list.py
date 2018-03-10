def type_list(list):
    long_string = ""
    sum = 0
    mixed = False
    # for elements in list:
    #     long_string = ""
    #     sum = 0.0

    #     if type(elements) == str:
    #         print "The list you entered is of string type"
    #         long_string += elements + " "
    #         print "String: {}", format(long_string)

    for i in range(1, len(list)):
        if type(list[i]) != type(list[i-1]):

            mixed = True
    # print(mixed)
    # print(type(list[i]))
    # print(type(list[i-1]))
    if mixed == True:
        for i in range(0, len(list)):
            if type(list[i]) == int or type(list[i]) == float:
                sum = sum + list[i]
            elif type(list[i]) == str:
                long_string = long_string + list[i] + " "
        print "The list you entered is of mixed type"
        print "String: ", long_string
        print "Sum: ", sum
    else:
        # print "we are here"
        # print "We are testing "+ long_string
        if type(list[0]) == int or type(list[i]) == float:
            for i in range(0, len(list)):
                sum = sum + list[i]
            print "The list you entered is of integer type"
            print "Sum: ", sum

        if type(list[0]) == str:
            # print "are we here"
            for i in range(0, len(list)):
                long_string = long_string + list[i] + " "
            print "The list you entered is of string type"
            print "String: ", long_string

list = ['magical','unicorns']
type_list(list)

list2 = [2, 3, 1, 7, 4, 12]
type_list(list2)

list3 = ['magical unicorns', 19, 'hello', 98.98, 'world']
type_list(list3)

# list could have elements of dictionary type, list type, boolean type. 
# we would need to adjust the code to check for data types of dictionary, list, boolean types
