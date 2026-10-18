import sys

def stack():
    stack = []
    for line in sys.stdin:
        cmd = line.split()
        if not cmd:
            continue
        if cmd[0] == 'push':
            stack.append(cmd[1])
            print('ok')
        elif cmd[0] == 'pop':
            print(stack.pop() if stack else 'error')
        elif cmd[0] == 'back':
            print(stack[-1] if stack else 'error')
        elif cmd[0] == 'size':
            print(len(stack))
        elif cmd[0] == 'clear':
            stack.clear()
            print('ok')
        elif cmd[0] == 'exit':
            print('bye')
            break


stack()