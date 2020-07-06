def binary_search(arr, left, right, key):
    
    if right < left:
        return -1

    else:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            return binary_search(arr, left, mid-1, key)

        else:
           return binary_search(arr, mid+1, right, key)

arr = [2,3,4,5,6,7,8,9]
x = binary_search(arr, 0, len(arr)-1, 2)
print(x)
y= binary_search(arr, 0, len(arr)-1, 10)
print(y)
