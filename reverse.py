def reverse(s):
  # Split the string into a list of words
  words = s.split()

  # Reverse the list of words
  words.reverse()

  # Reverse each word in the list
  words = [word[::-1] for word in words]

  # Join the reversed words into a single string
  result = " ".join(words)

  return result
