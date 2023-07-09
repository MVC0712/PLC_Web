import time
import csv
import pymcprotocol

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



if __name__ == "__main__":

    main()
    # filename = "data.csv"
    # read_data_from_csv(filename)