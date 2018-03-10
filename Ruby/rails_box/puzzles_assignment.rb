# Part 1

# arr = [3,5,1,2,7,9,8,13,25,32]

# Part 1 section a

# sum = 0;
# for el in arr
#     sum += el
# end

# puts sum

# Part 1 section b

# def greater array
#     print array.reject { |i| i < 10 } 
# end

# greater arr

# Part 2

# arr = ["John", "KB", "Oliver", "Cory", "Matthew", "Christopher"]

# puts arr.shuffle
# puts arr.shuffle.find_all { |name| name.length >= 5 }

# Part 3

# al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# puts al.shuffle[-1]
# puts al.shuffle[0]

# x = al.shuffle[0]
# puts x

# if x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u'
#     puts "You've gotten #{x}, which is a vowel"
# end

# Part 4

# prng = Random.new
# arr = []
# for i in 0...10
#     arr[i] = prng.rand(55...100)
# end

# print arr

# Part 5

# prng = Random.new
# arr = []
# for i in 0...10
#     arr[i] = prng.rand(55...100)
# end

# print arr.sort
# puts arr.min
# puts arr.max

# Part 6
# str = ''
# for i in 0...5
#     str = str + (65+rand(26)).chr
# end

# puts str

# Part 7
arr = []
for x in 0...10
    str = ''
    for i in 0...5
        str = str + (65+rand(26)).chr
    end
    arr[x] = str
end

print arr

