from scipy.spatial import distance
import numpy as np


class KNN:
    def __init__(self, data_set, label):

        # self.DataSet = data_set[:, :len(data_set)]
        self.DataSet = data_set
        # self.labels = data_set[:, len(data_set):]
        self.labels = label
        # print(len(self.labels), len(self.DataSet))
        self.dist_list = np.zeros(len(data_set))

    def distance_list(self, v1):

        for i in range(len(self.DataSet)):
            self.dist_list[i] = distance.euclidean(self.DataSet[i], v1)

    def make_prediction(self, n):
        vote_sell = 0
        vote_buy = 0
        dist_sorted = np.argsort(self.dist_list)

        for i in range(n):
            if self.labels[dist_sorted[i]] == 'sell':
                vote_sell += 1
                # print('sell:',vote_sell)
            else:
                # print('Buy:',vote_buy)
                vote_buy += 1

        if vote_sell >= vote_buy:
            return 'Sell'
        else:
            return 'Buy'

