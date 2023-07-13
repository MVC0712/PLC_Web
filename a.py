import random

def reposition_random_word_from_last_to_begin(string):
  """Repositions a random word from the last to the beginning of a string.

  Args:
    string: The string to reposition the word in.

  Returns:
    The string with the word repositioned.
  """

  words = string.split(" ")
  random_index = random.randint(0, len(words) - 1)
  word = words[random_index]
  words.remove(word)
  words.insert(0, word)
  new_string = " ".join(words)
  return new_string


if __name__ == "__main__":
  string = "hello world world2"
  new_string = reposition_random_word_from_last_to_begin(string)
  print(new_string)