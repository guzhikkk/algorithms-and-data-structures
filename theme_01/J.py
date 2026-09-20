import sys
import functools

def compare(x, y):
    if x + y < y + x:
        return 1
    return -1

parts = [line.rstrip() for line in sys.stdin.readlines()]
res = sorted(parts, key=functools.cmp_to_key(compare))
print(''.join(res))
