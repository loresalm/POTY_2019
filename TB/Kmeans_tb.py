from SelectData import SelectData
from KMeans import KMeans
import numpy as np


labelDataB = SelectData().saveAsPd("../CSVFile/D_S_F_FiltredDataBUY.csv")
labelDataS = SelectData().saveAsPd("../CSVFile/D_S_F_FiltredDataSELL.csv")
ldB = labelDataB.to_numpy()
ldS = labelDataB.to_numpy()

train_data = KMeans().parseALL(np.concatenate((ldB, ldS)))

trained_clusters, trained_centers = KMeans().cluster(train_data, 2)