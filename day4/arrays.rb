
# arr = [1,2,3,4]


# new_arr = Array.new(5,0) #.new()takes optional array size,default value  


# new_arr[3] = 7 # sets the third index to 7

# new_arr.push(9,10) # Adds 9,10 to the end of the arr
 
# new_arr.pop # removes the last element

# new_arr.unshift(1) # add 1 to the beginning of the array


# string_new = arr.join("-")


# puts string_new


# when creating a string arr

# str_arr = %w(jailer kwmae john appiah muslim loner)

# print str_arr.push("jannelle")

# str_arr << "kwaku"

# puts str_arr

# print new_arr


phone_number  = [0,5,5,7,3,6,2,8,5,9]


p_number = phone_number.join


puts p_number


# phone_number.each { |i| puts i}

phone_number.each_with_index {|item,index| puts "#{item} has the index of #{index}"}