n = int(input())
cars = list(map(int, input().split()))
stack = []
expected = 1

for car in cars:
    stack.append(car)
    while stack and stack[-1] == expected:
        stack.pop()
        expected += 1

if not stack:
    print("YES")
else:
    print("NO")