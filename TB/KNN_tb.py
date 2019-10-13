import numpy as np
from KNN import KNN
from SelectData import SelectData

labelDataB = SelectData().saveAsPd("../CSVFile/D_S_F_FiltredDataBUY.csv")
labelDataS = SelectData().saveAsPd("../CSVFile/D_S_F_FiltredDataSELL.csv")

ldB = labelDataB.to_numpy()
np.random.shuffle(ldB)
ldS = labelDataS.to_numpy()
np.random.shuffle(ldS)

#print(len(ldB[0]))

DS = np.concatenate((ldB[:len(ldB)-1, :len(ldB[0])-1], ldS[:len(ldS)-1, :len(ldS[0])-1]))

label = np.concatenate((ldB[:len(ldB)-1, len(ldB[0])-1:], ldS[:len(ldS)-1, len(ldS[0])-1:]))


Vb = np.array(ldB[len(ldB)-1:, :len(ldB[0])-1])

Vs = np.array(ldS[len(ldS)-1:, :len(ldS[0])-1])
np.reshape(Vs,(92,))

#DS = np.array([[1,1],[2,2],[2,1],[3,1]])--
#label = np.array(['Sell', 'Buy', 'Buy', 'Buy'])

knn = KNN(DS, label)

# V = np.array([0,0])

knn.distance_list(Vs)

print(knn.make_prediction(15))

