# Define a Caesar cipher function that takes a text and a shift value as input.
def caesar_cipher(text, shift)
  # Initialize an empty string to store the encrypted text.
  encrypted_text = ""

  # Iterate through each character in the input text.
  text.each_char do |char|
    # Check if the character is an alphabetic character (either uppercase or lowercase).
    if char.match(/[a-zA-Z]/)
      # Determine if the character is uppercase or lowercase.
      is_uppercase = char == char.upcase

      # Calculate the character code after applying the Caesar shift.
      char_code = char.ord + shift

      # Set the base and maximum character based on the case.
      if is_uppercase
        base = 'A'.ord
        max_char = 'Z'
      else
        base = 'a'.ord
        max_char = 'z'
      end

      # Wrap around the alphabet if the character code goes beyond 'z' or 'Z'.
      if char_code > max_char.ord
        char_code -= 26
      end

      # Append the shifted character to the encrypted text.
      encrypted_text << char_code.chr
    else
      # Non-alphabetic characters remain unchanged.
      encrypted_text << char
    end
  end

  # Return the encrypted text as the result.
  encrypted_text
end

# Example usage:
result = caesar_cipher("What a string!", 5)
puts result
