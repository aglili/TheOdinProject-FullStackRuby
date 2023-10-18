
puts "kwame".reverse

# create a method


# def add_to_10(number)
#     return 10+number.to_i
# end

# result = add_to_10(50)


# puts result


# def even_or_odd(number)
#     if number % 2 == 0
#         "That is an even number"
#     else
#         "That is an odd number"
#     end
# end


# puts even_or_odd(21)



def even_odd(number)
    unless number.is_a? Numeric
        return "Invalid Input"
    end

    if number % 2 == 0
        "This is an even number"
    else
        "This is an odd number"
    end
end
    


puts even_odd("hdjfbjd")


puts even_odd(10)

puts 13.between?(20,70)