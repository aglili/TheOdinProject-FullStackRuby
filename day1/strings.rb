
# String Concatenation

# Method 1 - plus operator

puts "Hello"+" Oden"+" Project!"

# Method 2 - shovel operator

puts "Hello"<<" Oden"<<" Project!"

# Method 3 - concat method

puts "Hello".concat(" Oden").concat(" Project!")



sample_string = "Hello Oden Project!"

# puts sample_string[0..4]


# puts sample_string[0,4]

# puts sample_string[4..-1]


# Escape Characters

puts "Hello \"Oden\" Project!"

puts "Hello \"Cecil\" \n How Are You?"


# String Interpolation

user_name = "Cecil"

puts "Hello #{user_name} How Are You?"


# usefull methods

puts "Hello".length

puts "Hello".reverse

puts "Hello".capitalize

puts "Hello".include?("l")

puts "hello".split("")


puts "hello".sub("h","H")

puts "hello".gsub("l","LL")
