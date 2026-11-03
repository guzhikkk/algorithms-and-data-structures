import sys
import heapq

def solve():
    # чтение данных
    input_data = sys.stdin.read().split()
    # количество слов
    n = len(input_data)
    # индекс слова
    idx = 0
    # структура кучи
    heap = []
    
    while idx < n:
        # строка команды
        cmd = input_data[idx]
        if cmd == "CLEAR":
            # очистка кучи
            heap = []
            idx += 1
        elif cmd == "ADD":
            # значение элемента
            val = int(input_data[idx+1])
            # добавление элемента
            heapq.heappush(heap, -val)
            # сдвиг индекса
            idx += 2
        elif cmd == "EXTRACT":
            if not heap:
                # вывод ошибки
                print("CANNOT")
            else:
                # извлечение элемента
                print(-heapq.heappop(heap))
            # сдвиг индекса
            idx += 1

if __name__ == '__main__':
    solve()