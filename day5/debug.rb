# def isogram?(string)
#     original_length = string.length
#     puts original_length
#     string_array  = string.downcase.split("")
#     puts string_array
#     unique_length = string_array.uniq.length
#     original_length == unique_length
# end


require 'pry-byebug'


def  isogram?(string)
    string_length = string.length
    string_array = string.downcase.split

    binding.pry

    unique_characters = string_array.uniq.length
    string_length == unique_characters
end



puts isogram?("timothy") #false
puts isogram?("Kwame") # true
