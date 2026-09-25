from functools import *

def money(arr):
    money_arr = []
    x = arr[1]
    y = arr[2]
    return x + y


def compare(a, b):
    x = money(a)
    y = money(b)
    if x < y:
        return -1
    elif x > y:
        return 1

    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    return 0



data = [
    ['Гужова', 350, 1000], 
    ['Брякина', 500, 850], 
    ['Гравшина', 400, 1000], 
    ['Логинов', 400, 900], 
    ['Картушина', 300, 1000],
    ['Боба', 350, 900]]

res = sorted(data, key=cmp_to_key(compare), reverse=True)
print(*res, sep='\n')
