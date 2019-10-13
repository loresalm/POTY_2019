import numpy as np
from KNN import KNN


DS = np.array([[1,1],[2,2],[2,1],[3,1]])
label = np.array(['Sell', 'Buy', 'Buy', 'Buy'])

knn = KNN(DS, label)

V = np.array([0,0])

knn.distance_list(V)

print(knn.make_prediction(1))

