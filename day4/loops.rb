# Loops

# Explantion of what a loop is
# A loop is a block of code that is executed until a certain condition is met

# Loop loop
# A loop loop is a loop that will run forever until the program is stopped

#example
# i= 0
# loop do
#     puts "i is #{i}"
#     i+=1
#     break if i == 10
# end

# While loop
# A while loop is a loop that will run until a certain condition is met
#example
# x = 0

# while x < 20
#     puts "x is #{x}"
#     x += 1
# end

# puts "Are you done yet?"
# while gets.chomp != "yes"
#     puts "Are you done yet?"
# end


# Until loop
# An until loop is a loop that will run until a certain condition is met

#example

# i = 0
# until i >= 10 do
#  puts "i is #{i}"
#  i += 1
# end


# until gets.chomp == "yes"
#     puts "Are you done yet?"
# end


#Ranges

# for i in 0...5
#     puts "#{i} zombies incoming!"
# end 


#Times loop

# 5.times do
#     puts "Hello!"
# end


# 6.times do |number|
#     puts "#{number} zombies incoming!"
# end



sum = 0
10.times do |number|
    sum += number
    puts sum
end

