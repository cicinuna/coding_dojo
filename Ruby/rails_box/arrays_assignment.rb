arr = [1,2,3,4,"hi", 5, 6, "Maybe"]

# puts arr.at(0)
# puts arr.fetch(3)
# puts arr.delete(2)
# puts arr.reverse
# puts arr.length
# puts arr.sort # gives error

num_arr = [1,6,36,68,3,223,6,2]
# puts num_arr.sort
# puts num_arr.slice!(3)
# puts num_arr
# arr.shuffle!
# num_arr.shuffle!

# puts arr
# puts num_arr
# puts ['MY', 'Name', 'IS', "jason"].join(" ")

# puts num_arr.insert(5, 6, 7)
# puts num_arr.insert(1, 44)

al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
puts al.values_at(5,10,4,5,6).join(" ")
puts al.values_at(0, 1, 1, -2)