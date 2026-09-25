def binary_search(arr1, el):
    left = -1
    right = len(arr1) - 1
    best_value = arr1[0]
    min_diff = abs(el - arr1[0])
    while left <= right:
        medium = (left + right) // 2
        current_value = arr1[medium]
        current_diff = abs(el - current_value)
        if current_diff < min_diff or (current_diff == min_diff and current_value < best_value):
            min_diff = current_diff
            best_value = current_value
        if el < current_value:
            right = medium - 1
        elif el > current_value:
            left = medium + 1
        else:
            return current_value
    return best_value



n, k = [int(el) for el in input().split()]
arr_first_sorted = [int(el) for el in input().split()]
arr_second = [int(el) for el in input().split()]
for x in arr_second:
    print(binary_search(arr_first_sorted, x))