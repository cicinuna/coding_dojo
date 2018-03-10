def find_characters(list, char):
    new_list = []
    for i in range(0, len(list)):
        if list[i].find(char) != -1:
            new_list.append(list[i])

    print new_list

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

find_characters(word_list, char)

# Just needed 1 loop and 1 check statement