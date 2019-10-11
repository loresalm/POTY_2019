
class DataSetGenerator:

    price = []

    def __init__(self, price):
        self.price = price

    def write_data(self):

        new_file = open('dataSet.txt', 'w')
        for el in self.price:
            new_file.write(el)
            new_file.write('\n')

        new_file.close()



l = [1, 2, 2, 3, 5, 4, 6]

d = DataSetGenerator(l)
