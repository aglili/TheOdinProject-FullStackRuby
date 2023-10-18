require 'pry-byebug'


def yell_greeting(user_name)
  name = user_name
  binding.pry
  name.upcase!
  puts "HELLO #{name}"
end


yell_greeting("Joshua")
