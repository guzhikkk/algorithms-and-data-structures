import sys

def queue():
    queue = []
    for line in sys.stdin:
        cmd = line.split()
        if not cmd:
            continue
        
        op = cmd[0]
        if op == 'push':
            queue.append(cmd[1])
            print('ok')
        elif op == 'pop':
            print(queue.pop(0) if queue else 'error')
        elif op == 'front':
            print(queue[0] if queue else 'error')
        elif op == 'size':
            print(len(queue))
        elif op == 'clear':
            queue.clear()
            print('ok')
        elif op == 'exit':
            print('bye')
            break


queue()