import time 
import csv
import pymcprotocol
import mysql.connector
from datetime import datetime
import random

def get_data():    
    die_name = [16973,12341,67,0,0]
    die_name = listToString(die_name)

    print(die_name)

def listToString(list):
    str = ""
    for st in list:
        if st != 0:
            str += hex_to_ascii(decimal_to_hex_16(st))
    return str

def main():
    interval = 30
    new_data = get_data()
    while True:
        time.sleep(interval)
        new_data = get_data()

def decimal_to_hex_16(decimal_number):
    hexadecimal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_digit = hex(remainder)[2:]
        hexadecimal_number = hexadecimal_digit + hexadecimal_number
        decimal_number = decimal_number // 16
    print("decimal_to_hex_16: " + changepos(insert_space(hexadecimal_number)))
    return changepos(insert_space(hexadecimal_number))

def hex_to_ascii(hex_string):
    ascii_string = ""
    for two_digit_pair in hex_string.split(" "):
        decimal_number = int(two_digit_pair, 16)
        ascii_character = chr(decimal_number)
        ascii_string += ascii_character
    print("hex_to_ascii: " + ascii_string)
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
    word = words[len(words) - 1]
    words.remove(word)
    words.insert(0, word)
    new_string = " ".join(words)
    print(string +" : "+ new_string)
    return new_string

if __name__ == "__main__":

    main()