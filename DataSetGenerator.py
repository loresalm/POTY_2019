
import csv


class DataSetGenerator:

    price = []

    def __init__(self, price):
        self.price = price

    def write_data(self, name):


        with open("./CSVFile/" + name + ".csv", mode='x') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(self.price)





