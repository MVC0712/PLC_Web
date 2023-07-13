import time
import csv
import pymcprotocol
import mysql.connector
from datetime import datetime
import random

def get_data():
    now = datetime.now()
    date_time = now.strftime("%Y/%m/%d %H:%M:00")
    
    pymc3e = pymcprotocol.Type3E()
    pymc3e.connect("192.168.1.2", 10000)
    press_mode = pymc3e.batchread_bitunits(headdevice="M310", readsize=1)
    die_change = pymc3e.batchread_bitunits(headdevice="Y1045", readsize=1)
    billet_counter = pymc3e.batchread_wordunits(headdevice="D7000", readsize=1)
    die_name = pymc3e.batchread_wordunits(headdevice="R395", readsize=5)
    alarm = pymc3e.batchread_wordunits(headdevice="D320", readsize=1)
    
    press_mode = press_mode[1:-1]
    die_change = die_change[1:-1]
    billet_counter = billet_counter[1:-1]
    die_name = listToString(die_name)
    alarm = alarm[1:-1]

    return (date_time, press_mode, die_change, billet_counter, die_name, alarm)
    # die_name = [16973, 12341, 67, 0, 0]
    # die_name = listToString(die_name)
    # print(die_name)
    # return (die_name)

def listToString(list):
    str = ""
    for st in list:
        if st != 0:
            str += hex_to_ascii(decimal_to_hex_16(st))
    return str

def main():
    interval = 5
    data = get_data()
    while True:
        time.sleep(interval)
        data = get_data()
        
        queryData("SELECT date_time, press_mode, die_change, billet_counter, die_name, alarm FROM t_plc_web_log ORDER BY date_time DESC LIMIT 1")

def compare_arrays(array1, array2):
    # array1 = [1, 2, 3, 4, 5]
    # array2 = [1, 2, 3, 4, 5]
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

def connect_to_mysql(host="localhost", port=3306, user="root", password="", database="extrusion"):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return connection

def queryData(sql_query):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    # for row in results:
    #     print(row)
    connection.close()
    print(results[0])

def insert_data_to_log(data):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    # data = [("John Doe", 30), ("Jane Doe", 25)]
    insert_query = "INSERT INTO t_plc_web_log (date_time, press_mode, die_change, billet_counter, die_name, alarm) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, data)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()

    return id

def insert_data_to_web(data):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    # data = [("John Doe", 30), ("Jane Doe", 25)]
    insert_query = "INSERT INTO t_plc_web (start_time, end_time, die_name, billet_quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, data)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()

    return id

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

def compare_tuples(oldData, newData):
    oldPressMode = oldData[1]
    newPressMode = newData[1]

    return oldPressMode == newPressMode

def concatenateData(oldData, newData):    
    start_time = oldData[0]
    die_name = oldData[4]
    start_billet = oldData[3]
    end_time = newData[0]
    end_billet = newData[3]
    
    print([(start_time, end_time, die_name, end_billet-start_billet)])


if __name__ == "__main__":

    # main()
    # get_data()
    queryData("SELECT * FROM `m_code` WHERE 1")
    # decimal_number = 16973
    # hexadecimal_number = decimal_to_hex_16(decimal_number)
    # ascii_string = hex_to_ascii(hexadecimal_number)
    # print(ascii_string)