words = "It's thanksgiving day. It's my birthday, too!"

print words.find("day")

x = [2, 54, -2, 7, 12, 98]

print min(x)
print max(x)

y = ["hello", 2, 54, -2, 7, 12, 98, "world"]
z = []
z.append(y[0])
z.append(y[len(y)-1])
print z

my_list = [19,2,54,-2,7,12,98,32,10,-3,6]
print sorted(my_list)

my_list = sorted(my_list)

# print my_list[0:(len(my_list)/2)]
new_list = []
new_list.append(my_list[0:(len(my_list)/2)])

for i in range(len(my_list)/2, len(my_list)):
    new_list.append(my_list[i])

print new_list