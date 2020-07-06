def linear_search(arr, key):
    for i in arr:
        if i == key:
            # if found return index of item
            return arr.index(i) 
    # if item not found return -1
    return -1


arr = [4, 5, 6, 8, 9, 10, 15, 12]
x = linear_search(arr, 8)
print(x)
y = linear_search(arr, 3)
print(y)