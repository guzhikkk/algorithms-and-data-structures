from functools import *

# def money(arr):
#     money_arr = []
#     x = arr[1]
#     y = arr[2]
#     return x + y


# def compare(a, b):
#     x = money(a)
#     y = money(b)
#     if x < y:
#         return -1
#     elif x > y:
#         return 1

#     if a[0] > b[0]:
#         return -1
#     elif a[0] < b[0]:
#         return 1
#     return 0



# data = [
#     ['Гужова', 350, 1000], 
#     ['Брякина', 500, 850], 
#     ['Гравшина', 400, 1000], 
#     ['Логинов', 400, 900], 
#     ['Картушина', 300, 1000],
#     ['Боба', 350, 900]]

# res = sorted(data, key=cmp_to_key(compare), reverse=True)
# print(*res, sep='\n')


def f(arr):
    summ = 0
    number = arr[1]
    for el in number:
        n = int(el)
        summ += n
    return summ

def compare(a, b):
    x = f(a)
    y = f(b)
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
    ['Гужова', '89105038223'], 
    ['Брякина', '89203456278'], 
    ['Гравшина', '89056785432'], 
    ['Логинов', '86789804554'], 
    ['Картушина', '88095353535'],
    ['Боба', '89206005065']]



res = sorted(data, key=cmp_to_key(compare))
print(*res, sep='\n')
for el in data:
    summa = f(el)
    print(el[0], summa, sep=' ')