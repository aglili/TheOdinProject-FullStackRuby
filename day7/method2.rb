fruits = ["guava","orange","pawpaw","watermelon","apple","pineapple"]

capital_fruits = []



# fruits.each_with_index{|fruit,index| puts "#{fruit} has the index #{index}"}

# fruits.each_with_index{|fruit,index| puts fruit if index.even?}



# fruits.each{|fruit| capital_fruits.push(fruit.upcase)}


# print capital_fruits


# capital_fruits = fruits.map { |fruit| fruit.upcase }


# print capital_fruits


# my_order = ['medium Big Mac', 'medium fries', 'medium milkshake']

# new_order = my_order.map {|item| item.gsub("medium","small")}

# print new_order

# salaries = [1200, 1500, 1100, 1800]


# after_tax = salaries.map{|salary| salary-500}

# print after_tax


my_numbers = [5, 6, 7, 8]

# sum = 0

# my_numbers.each{|number| sum+=number}

# puts sum


arr = [1,2,3,4,5,6,7,8,9,10]
puts my_numbers.reduce{|sum,number| sum+= number}


puts arr.reduce(100){|sum,number| sum += number}