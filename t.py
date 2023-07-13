import random

def decimal_to_hex_16(decimal_number):
    hexadecimal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_digit = hex(remainder)[2:]
        hexadecimal_number = hexadecimal_digit + hexadecimal_number
        decimal_number = decimal_number // 16
    return changepos(insert_space(hexadecimal_number))

def hex_to_ascii(hex_string):
    ascii_string = ""
    for two_digit_pair in hex_string.split(" "):
        decimal_number = int(two_digit_pair, 16)
        ascii_character = chr(decimal_number)
        ascii_string += ascii_character
    return ascii_string

def insert_space(string):
    new_string = ""
    for i in range(0, len(string), 2):
        new_string += string[i:i + 2]
        if i + 2 < len(string):
            new_string += " "
    return new_string

def changepos(string):
  words = string.split(" ")
  random_index = random.randint(0, len(words) - 1)
  word = words[random_index]
  words.remove(word)
  words.insert(0, word)
  new_string = " ".join(words)
  return new_string

if __name__ == "__main__":
    decimal_number = 16973
    hexadecimal_number = decimal_to_hex_16(decimal_number)
    ascii_string = hex_to_ascii(hexadecimal_number)
    print(ascii_string)