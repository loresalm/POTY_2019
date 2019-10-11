import random

from FindMaxSubArray import FindMaxSubArray




x = [random.randint(-100, 100) for i in range(15)] #<<<change here!!!


print(x)


L, H, S = FindMaxSubArray().find_maximum_subarray(x, 0, (15-1)) #<<<change here!!!
print("")
print("low=", L, " high=", H, "sum=", S)
print(x[L:H+1])


