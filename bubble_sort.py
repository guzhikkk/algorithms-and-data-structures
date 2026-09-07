def BubbleSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


input_data = input().split()
arr = [int(x) for x in input_data]
BubbleSort(arr)
print(*arr)