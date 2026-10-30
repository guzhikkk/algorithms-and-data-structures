def binary_search(arr, key):
    left = -1
    right = len(arr)
    
    while right - left > 1:
        medium = (left + right) // 2
        if arr[medium] <= key:
            right = medium
        else:
            left = medium

    if right < len(arr) and arr[right] == key:
        return right
    return -1

    
data = [9, 8, 8, 6, 6, 6, 4, 3, 3, 2, 0]
print(binary_search(data, 0))
print(binary_search(data, 8))
print(binary_search(data, 5))
print(binary_search(data, 11))
print(binary_search(data, -2))
print(binary_search(data, 6))
print(binary_search(data, 2))