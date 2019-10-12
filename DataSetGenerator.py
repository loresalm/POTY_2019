
import csv



class DataSetGenerator:

    price = []
    param = []

    def __init__(self, price, param):
        self.price = price
        self.param = param

    def write_data(self, name):


        with open("../CSVFile/" + name + ".csv", mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(self.param)
            for i in range(len(self.price)):
                csv_writer.writerow(self.price[i])





