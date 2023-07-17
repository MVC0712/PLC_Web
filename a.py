def changepos(string):
    words = string.split(" ")
    first_word = words[0]
    second_word = words[1]
    words[0] = second_word
    words[1] = first_word
    print(words)
    return words

changepos("aa bb")