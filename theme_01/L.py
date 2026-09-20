far = [int(el) for el in input().split()]
cost = [int(el) for el in input().split()]
res = 0
while cost != []:
    bill = max(cost)
    dist = min(far)
    res += bill*dist
    cost.pop(cost.index(max(cost)))
    far.pop(far.index(min(far)))
print(res)
