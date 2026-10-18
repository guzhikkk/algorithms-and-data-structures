import sys
from collections import deque

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    ptr = 1
    
    for _ in range(n):
        k = int(input_data[ptr])
        ptr += 1
        arr = [float(x) for x in input_data[ptr:ptr+k]]
        ptr += k
        
        target = sorted(arr)
        stack = deque()
        idx = 0
        
        for val in arr:
            stack.append(val)
            while stack and stack[-1] == target[idx]:
                stack.pop()
                idx += 1
                
        if not stack:
            print(1)
        else:
            print(0)