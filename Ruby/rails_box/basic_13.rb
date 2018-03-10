# 1. print 1-255
# for i in 1..255
#     puts i
# end

# 2. print odd between 1-255
# for i in 1..255
#     puts i if i % 2 != 0
# end

# 3. print sum
# sum = 0
# for i in 0..255
#     sum = sum + i
#     puts "New number: #{i} Sum: #{sum}"
# end

# 4. iterating through an array
# x = [1,3,5,7,9,13]
# for el in x
#     puts el
# end

# 5. Find Max
# def find_max arr
#     puts arr.max
# end

# find_max [1,4,5,88]
# find_max [-2,-4,-77,0]

# 6. Find Average
# def average arr
#     sum = 0 #also tried sum = 0.0 for floats
#     for el in arr
#         sum = sum + el
#     end
#     puts sum / arr.length
# end

# average [2,10,3]
# average [-5,11,16]

# 7. Array with Odd Numbers
# print (1..255).reject { |i| i % 2 == 0 }
# # Iterators instruction section says that
# # .reject returns an array, but the output 
# # seen in terminal is not an array.
# # puts (1..255).reject gives me just all elements in new line
# # but print returns an array.???

# 8. Greater than Y
# def greater arr, y
#     count = 0
#     for el in arr
#         if el > y
#             count = count + 1
#         end
#     end
#     puts count
# end

# greater [1,3,5,7], 3
# greater [1,3,5,7], 0

# 9. Square the values
# def square arr
#     for i in 0...arr.length
#         arr[i] = arr[i] * arr[i]
#     end
#     puts arr
# end

# square [1,5,10,-2]

# 10. Eliminate negative Numbers
# def elim_neg arr
#     for i in 0...arr.length
#         if arr[i] < 0
#             arr[i] = 0
#         end
#     end
#     puts arr
# end

# elim_neg [1,5,10,-2,-5,4]

# 11. Max, Min, Average
# def nums arr
#     max = arr[0]
#     min = arr[0]
#     sum = 0.0
#     for i in 0...arr.length
#         if arr[i] < min
#             min = arr[i]
#         end
#         if arr[i] > max
#             max = arr[i]
#         end
#         sum = sum + arr[i]
#     end
#     puts "Max is #{max}, Min is #{min}, and average is #{sum / arr.length}."
# end

# nums [1,5,10,-2]

# 12. Shifting values in the array
# def shift arr
#     for i in 0...arr.length-1
#         arr[i] = arr[i+1]
#     end
#     arr[arr.length-1] = 0
#     print arr
# end

# shift [1,5,10,7,-2]

# 13. Number to String
def num_to_string arr
    for i in 0...arr.length
        if arr[i] < 0
            arr[i] = 'Dojo'
        end
    end
    puts arr
end

num_to_string [-1,-3,2]