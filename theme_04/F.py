import sys
import heapq

def solve():
    # чтение данных
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # количество грузов
    n = int(input_data[0])
    
    # массив интервалов
    intervals = []
    idx = 1
    for _ in range(n):
        t = int(input_data[idx])
        l = int(input_data[idx+1])
        intervals.append((t, t + l))
        idx += 2
        
    # сортировка по времени прибытия
    intervals.sort(key=lambda x: x[0])
    
    # куча для времени окончания
    heap = []
    # максимальное количество аппаратов
    max_machines = 0
    
    # цикл обработки грузов
    for start, end in intervals:
        # освобождение аппаратов (нестрогое неравенство)
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # занятие аппарата
        heapq.heappush(heap, end)
        
        # обновление ответа
        if len(heap) > max_machines:
            max_machines = len(heap)
            
    # вывод результата
    print(max_machines)

if __name__ == '__main__':
    solve()