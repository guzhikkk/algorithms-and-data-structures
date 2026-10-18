from collections import deque

#сразу преобразуем их в двустороннюю очередь
p1 = deque(map(int, input().split()))
p2 = deque(map(int, input().split()))

turns = 0

#пока у обоих есть карты и не превышен лимит ходов
while p1 and p2 and turns < 1000000:
    #берем верхние карты
    c1 = p1.popleft()
    c2 = p2.popleft()
    
    #условие победы 1 игрока:
    #у него 0, а у 2 9 - искл
    #или его карта больше, но это не когда у него 9, а у 2 0
    if (c1 == 0 and c2 == 9) or (c1 > c2 and not (c1 == 9 and c2 == 0)):
        p1.append(c1)
        p1.append(c2)
    else:
        #в остальных случаях побеждает второй
        p2.append(c1)
        p2.append(c2)
        
    turns += 1


if not p1:
    print(f"second {turns}")
elif not p2:
    print(f"first {turns}")
else:
    print("botva")