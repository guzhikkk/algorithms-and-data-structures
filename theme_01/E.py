def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    ind = len(arr) // 2
    left = merge_sort(arr[:ind])
    right = merge_sort(arr[ind:])
    
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


n = int(input())
arr = list(map(int, input().split()))
print(*merge_sort(arr))