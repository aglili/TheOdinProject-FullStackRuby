# Basic Data Types

# number ie: floats and integers

# floats --> 3.67,8.67
# integers --> 1,2,3,4,5

# References = https://launchschool.com/books/ruby/read/basics, 


# operations on numbers include addition, subtraction, multiplication, division, modulus, exponents

# addition
puts 1 + 1

# subtraction
puts 2 - 1

# multiplication
puts 2 * 2

# division
puts 4 / 2

# modulus
puts 5 % 2

# exponents
puts 2**3


# its immportant to note that when dividing integers, the result will always be an integer

# example 5/2 = 2

# to get the correct result, you need to convert one of the integers to a float

# example 5.0/2 = 2.5

# you can also use the to_f method to convert an integer to a float

# Example 5.to_f = 5.0

# you can also use the to_i method to convert a float to an integer

# Example 5.0.to_i = 5

# Useful Number Methods

puts 10.even? # returns true if the number is even

puts 10.odd? # returns true if the number is odd

puts 10.next # returns the next number in the sequence in this case 11

puts 10.pred # returns the previous number in the sequence in this case 9

puts 10.to_f # converts the number to a float

puts 10.to_s # converts the number to a string

# you can also use the .class method to find out the class of the number

puts 10.class # returns integer

puts 10.0.class # returns float

# you can also use the .zero? method to find out if a number is zero

puts 0.zero? # returns true

puts 10.zero? # returns false

# you can also use the .nonzero? method to find out if a number is not zero

puts 0.nonzero? # returns nil

puts 10.nonzero? # returns 10

# you can also use the .abs method to find the absolute value of a number

puts -10.abs # returns 10

puts 10.abs # returns 10

# you can also use the .round method to round a number to the nearest integer

puts 10.5.round # returns 11

puts 10.4.round # returns 10

# you can also use the .floor method to round a number down to the nearest integer

puts 10.5.floor # returns 10

puts 10.4.floor # returns 10

# you can also use the .ceil method to round a number up to the nearest integer

puts 10.5.ceil # returns 11

puts 10.4.ceil # returns 11

# you can also use the .to_r method to convert a number to a rational number

puts 10.to_r # returns 10/1

# you can also use the .to_c method to convert a number to a complex number

puts 10.to_c # returns 10+0i

# you can also use the .to_i method to convert a number to an integer

puts 10.5.to_i # returns 10

# you can also use the .to_f method to convert a number to a float

puts 10.to_f # returns 10.0

# you can also use the .to_s method to convert a number to a string

puts 10.to_s # returns "10"

# you can also use the .to_sym method to convert a number to a symbol

puts 10.to_sym # returns :"10"

# you can also use the .to_c method to convert a number to a complex number

puts 10.to_c # returns 10+0i