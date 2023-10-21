# Nested Arrays

test_scores = [
  [97, 76, 79, 93],
  [79, 84, 76, 79],
  [88, 67, 64, 76],
  [94, 55, 67, 81]
]

teacher_mailboxes = [
  ["Adams", "Baker", "Clark", "Davis"],
  ["Jones", "Lewis", "Lopez", "Moore"],
  ["Perez", "Scott", "Smith", "Young"]
]


# Accessing elements


# Accessing a specific element within a nested array is as simple as calling array[x][y], 
# where x is the index of the nested element and y is the index inside of the nested element.

puts teacher_mailboxes[2][3]

puts  test_scores[2][3]