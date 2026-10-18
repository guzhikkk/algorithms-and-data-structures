s = input().split()
stack = []

for c in s:
    if c not in ['+', '-', '*']:
        stack.append(int(c))
    else:
        b = stack.pop()
        a = stack.pop()
        if c == '+':
            stack.append(a + b)
        elif c == '-':
            stack.append(a - b)
        elif c == '*':
            stack.append(a * b)

print(stack[0])