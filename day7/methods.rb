students = ["kwame","Jake","Abena","Selikem","Shelter","Walter","Comboni"]



# Select method
puts students.select {|student| student != "Jake" && student != "Abena"}


# reject method
print students.reject {|student| student == "Walter"}


# each method


students.each{|student| puts "Hello #{student}"}



arr = [4,6]

arr.each do |num|
  num *=2
  puts "Double your number is #{num}"
end


# Each method also workes for hashes

regions = {
  :VOL => "Volta Region",
  :GA => "Greater Accra Region",
  :EST => "Eastern Region"
}

regions.each {|key,value| puts "#{key} is #{value}"}


regions.each {|pair| puts pair}