# Multiples
# Part 1

# prints odd integers from 1 to 1000
for i in range(1,1000,2):
    print i

# Part 2

# prints multiples of 5 from 5 to 1,000,000 inclusive
for i in range(5, 1000001, 5):
    print i

# Sum List
list1 = [1, 2, 5, 10, 255, 3]
sum = 0
for vals in list1:
    sum = sum + vals

print sum

# Average List
list2 = [1,2,5,10,255,3]
avg_sum = 0
avg = 0.0

for vals in list2:
    avg_sum = avg_sum + vals

avg = avg_sum / len(list2)

print avg