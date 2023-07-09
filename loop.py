import time
import csv
import pymcprotocol
import mysql.connector

def get_data():
    pymc3e = pymcprotocol.Type3E()
    pymc3e.connect("192.168.1.2", 10000)
    MachineAutoMode = pymc3e.batchread_bitunits(headdevice="M310", readsize=1)
    Y1045 = pymc3e.batchread_bitunits(headdevice="Y1045", readsize=1)
    return (MachineAutoMode, Y1045)

def save_data_to_csv(data, filename):
    with open(filename, 'w', encoding='UTF8') as f:

        writer = csv.writer(f)
        writer.writerow(data)

def read_data_from_csv(filename):
    with open(filename) as file:
        csvreader = csv.reader(file)
        # for row in csvreader:
        #     print(csvreader)
        print(next(csvreader))

def main():
    interval = 5
    data = get_data()
    while True:
        print(data)
        time.sleep(interval)
        data = get_data()
        filename = "data.csv"
        read_data_from_csv(filename)
        save_data_to_csv(data, filename)

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
    for row in results:
        print(row)
    connection.close()

def insert_data_to_mysql(data):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    # data = [("John Doe", 30), ("Jane Doe", 25)]
    insert_query = "INSERT INTO my_table (name, age) VALUES (%s, %s)"
    cursor.execute(insert_query, data)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()

    return id

if __name__ == "__main__":

    main()