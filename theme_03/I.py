import sys

data = sys.stdin.read().split()
if not data:
    sys.exit(0)
    
n = int(data[0])
if n == 0:
    print(0)
    sys.exit(0)
    
colors = [int(x) for x in data[1:n+1]]
stack = []
destroyed = 0

for c in colors:
    while stack and stack[-1][0] != c and stack[-1][1] >= 3:
        destroyed += stack[-1][1]
        stack.pop()

    if not stack:
        stack.append([c, 1])
    elif stack[-1][0] == c:
        stack[-1][1] += 1
    else:
        stack.append([c, 1])

while stack and stack[-1][1] >= 3:
    destroyed += stack[-1][1]
    stack.pop()

print(destroyed)