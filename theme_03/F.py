from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dq = deque()

for i in range(n):
    if dq and dq[0] <= i - k:
        dq.popleft()
        
    while dq and arr[dq[-1]] >= arr[i]:
        dq.pop()
        
    dq.append(i)
    
    if i >= k - 1:
        print(arr[dq[0]])