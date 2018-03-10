def compare(list1, list2):
    isSame = True
    if len(list1) != len(list2):
        isSame = False
    else:
        for i in range(0, len(list1)):
            if list1[i] != list2[i]:
                isSame = False
    
    if isSame == True:
        print "The lists are the same."
    else:
        print "The lists are not the same."

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare(list_one, list_two)

# def compare works for all the above test cases with different instances of list_one and list_two