def f(x):
    return a * x**3 + b * x**2 + c * x + d


a, b, c, d = map(float, input().split())
if a < 0:
    a, b, c, d = -a, -b, -c, -d

left = -2000.0
right = 2000.0

for _ in range(100):
    medium = (left + right) / 2
    if f(medium) > 0:
        right = medium
    else:
        left = medium

print(f"{left:.6f}")