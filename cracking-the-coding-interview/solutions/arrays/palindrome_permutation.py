def palindrome_permutation(string):
  if string is None:
    return True
  bit_vector = 128*[False]
  num_valid_chars = 0
  for char in string:
    if 0 <= ord(char) <= 127 and char != ' ':
      num_valid_chars += 1
      bit_vector[ord(char)] = not bit_vector[ord(char)]
  if num_valid_chars % 2 == 0:
    return sum(bit_vector) == 0
  return sum(bit_vector) == 1
