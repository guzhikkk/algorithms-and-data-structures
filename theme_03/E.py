import sys


def deque():
    d = []
    for line in sys.stdin:
        cmd = line.split()
        if not cmd:
            continue
        
        op = cmd[0]
        if op == 'push_front':
            d.insert(0, cmd[1])
            print('ok')
        elif op == 'push_back':
            d.append(cmd[1])
            print('ok')
        elif op == 'pop_front':
            print(d.pop(0) if d else 'error')
        elif op == 'pop_back':
            print(d.pop() if d else 'error')
        elif op == 'front':
            print(d[0] if d else 'error')
        elif op == 'back':
            print(d[-1] if d else 'error')
        elif op == 'size':
            print(len(d))
        elif op == 'clear':
            d.clear()
            print('ok')
        elif op == 'exit':
            print('bye')
            break


deque()