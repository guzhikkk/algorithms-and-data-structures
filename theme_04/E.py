import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # количество чисел
    n = int(input_data[0])
    # массив чисел
    nums = [int(x) for x in input_data[1:n+1]]
    
    # создание кучи
    heapq.heapify(nums)
    
    # общая сумма промежуточных результатов
    total_intermediate_sum = 0
    
    # цикл слияния элементов
    while len(nums) > 1:
        # первое слагаемое
        a = heapq.heappop(nums)
        # второе слагаемое
        b = heapq.heappop(nums)
        # сумма элементов
        current_sum = a + b
        
        # накопление общей суммы
        total_intermediate_sum += current_sum
        
        # возврат суммы в кучу
        heapq.heappush(nums, current_sum)
        
    # вычисление итоговой стоимости (5% от суммы)
    cost = total_intermediate_sum * 0.05
    
    # вывод результата
    print(f"{cost:.2f}")

if __name__ == '__main__':
    solve()