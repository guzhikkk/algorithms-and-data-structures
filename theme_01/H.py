n = int(input())
points = []
for _ in range(n):
    a, b = map(int, input().split())
    points.append((a, b))

points.sort(key=lambda x: (x[0] ** 2 +x[1] ** 2))
for point in points:
    print(point[0], point[1])
