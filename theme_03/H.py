import sys
from collections import deque

n = int(sys.stdin.readline())
left = deque()
right = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == '+':
        right.append(cmd[1])
    elif cmd[0] == '*':
        right.appendleft(cmd[1])
    elif cmd[0] == '-':
        print(left.popleft())
        
    if len(right) > len(left):
        left.append(right.popleft())
    elif len(left) > len(right) + 1:
        right.appendleft(left.pop())