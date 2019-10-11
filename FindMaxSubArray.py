import random


def find_maximum_subarray(a, low, high):

    if low == high:
        return low, high, a[low]
    else:
        mid = (low + high)//2

        l_low, l_high, l_sum = find_maximum_subarray(a, low, mid)

        r_low, r_high, r_sum = find_maximum_subarray(a, mid+1, high)

        cr_low, cr_high, cr_sum = find_max_crossing_subarray(a, low, mid, high)

        if l_sum >= r_sum and l_sum >= cr_sum:
            return l_low, l_high, l_sum
        elif r_sum >= l_sum and r_sum >= cr_sum:
            return r_low, r_high, r_sum
        else:
            return cr_low, cr_high, cr_sum


def find_max_crossing_subarray(a, low, mid, high):

    l_s = -float('Inf')
    sum_ = 0
    max_l = 0
    for i in range(mid, low, -1):
        sum_ += float(a[i])
        if sum_ > l_s:
            l_s = sum_
            max_l = i

    r_s = -float('Inf')
    sum_ = 0
    max_r = 0
    for j in range(mid+1, high):
        sum_ += float(a[j])
        if sum_ > r_s:
            r_s = sum_
            max_r = j

    return max_l, max_r, l_s + r_s


x = [random.randint(-100, 100) for i in range(15)] #<<<change here!!!


print(x)

L, H, S = find_maximum_subarray(x, 0, 15-1) #<<<change here!!!
print("")
print("low=", L, " high=", H, "sum=", S)
print(x[L:H+1])




