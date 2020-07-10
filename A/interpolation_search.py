
def interpolation_search(arr, n, key):
    low = 0
    high = n-1

    while low <= high and key >= arr[low] and key <= arr[high]:
        # if array contain single member
        if low == high:
            if arr[low] == key:
                return low
            return  -1

        #interpolation formula to calculate the position
        pos = low  + int(((float(high - low)/(arr[high] - arr[low])) *(key - arr[low])))

        if arr[pos] == key:
            return pos

        if arr[pos]  < key:
            low = pos + 1

        else:
            high = pos - 1

    return -1


arr = [2, 4, 6, 8, 10, 12, 14]
n = len(arr)
index = interpolation_search(arr, n, 1)
print(index)