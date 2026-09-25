def binary_search(arr1, el):
    left = 0
    right = len(arr1) - 1
    while left <= right:
        medium = (left + right) // 2
        if arr1[medium] == el:
            return 'YES'
        elif el < arr1[medium]:
            right = medium - 1
        else:
            left = medium + 1
    return 'NO'



n, k = [int(el) for el in input().split()]
arr_first_sorted = [int(el) for el in input().split()]
arr_second = [int(el) for el in input().split()]
for x in arr_second:
    print(binary_search(arr_first_sorted, x))