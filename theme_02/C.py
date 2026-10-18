import math

n = float(input())

left = 0.0
right = max(1.0, math.sqrt(n))

for _ in range(100):
    medium = (left + right) / 2
    if medium * medium + math.sqrt(medium) < n:
        left = medium
    else:
        right = medium

print((left + right) / 2)