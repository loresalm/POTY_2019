

from SelectData import SelectData
from FindMaxSubArray import FindMaxSubArray
from DataSetGenerator import DataSetGenerator
import numpy as np



#find_maximum_subarray(self, a, low, high):
#return cr_low, cr_high, cr_sum
print("**")
dataSet = SelectData().save(['Open', 'Close'], "CSVFile/DataSetFrom06to12.csv")
print("**")
dataSetDiff = dataSet[1] - dataSet[0]


choseData= []
choseData2= []
acc = 0
acc2= 0
accS = 0
acc2S= 0


dataCVSO = []
dataCVSC = []

for i in range(0, (len(dataSetDiff) - (52359%288)), 288):
    L, H, S = FindMaxSubArray().find_maximum_subarray(dataSetDiff, i, i + 288)
    choseData.append(dataSetDiff[L:H + 1])
    acc += len(dataSetDiff[L:H + 1])
    acc2 += np.sum(dataSetDiff[L:H + 1])

    if(L>82):

        if np.sum(dataSetDiff[H-91:H+1]) > 6: #change meanSUM
            accS += len(dataSetDiff[H-91:H+1])
            acc2S += np.sum(dataSetDiff[H-91:H+1])
            choseData2.append(dataSetDiff[H-91:H+1])

            dataCVSO.append(dataSet[0][H-91:H+1])
            dataCVSC.append(dataSet[1][H-91:H+1])





finalData= np.array(choseData)
print ("mean NUMBER OF CANDLE= ", acc/ len(finalData) )
print ("mean2 GAIN MEAN= ", acc2/ len(finalData) )
print(" ")
finalData2 = np.array(choseData2)
print ("mean NUMBER OF CANDLE'= ", accS/ len(finalData2) )
print ("mean2' GAIN MEAN= ", acc2S/ len(finalData2) )
print("len dataset2 (final)=", len(finalData2))

print("len CSV=", len(dataCVSO))
print("len CSV C=", len(dataCVSC))







fin = np.array([np.concatenate(dataCVSO), np.concatenate(dataCVSC)])
print(np.shape(fin))


fin2 = DataSetGenerator(fin.T, np.array(['Open', 'Close'])).write_data("D_S_F_FiltredData")

















