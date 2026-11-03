import sys

class MinHeap:
    def __init__(self):
        # инициализация
        self.heap = [0]
        # размер кучи
        self.size = 0

    def shiftUp(self, i):
        # просеивание вверх
        while i // 2 > 0 and self.heap[i] < self.heap[i // 2]:
            # обмен элементов
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            # индекс родителя
            i = i // 2

    def insert(self, x):
        # добавление элемента
        self.heap.append(x)
        # обновление размера
        self.size += 1
        # вызов просеивания
        self.shiftUp(self.size)

    def indMinChild(self, i):
        # поиск потомка
        if i * 2 + 1 > self.size:
            # левый потомок
            return i * 2
        if self.heap[i * 2] < self.heap[i * 2 + 1]:
            # левый потомок
            return i * 2
        # правый потомок
        return i * 2 + 1

    def shiftDown(self, i):
        # просеивание вниз
        while i * 2 <= self.size:
            # индекс потомка
            j = self.indMinChild(i)
            if self.heap[i] > self.heap[j]:
                # обмен элементов
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                # обновление индекса
                i = j
            else:
                break

    def delMin(self):
        # извлечение минимума
        if self.size == 0:
            # пустая куча
            return None
        # минимальный элемент
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        # уменьшение размера
        self.size -= 1
        # удаление конца
        self.heap.pop()
        
        if self.size > 0:
            # вызов просеивания
            self.shiftDown(1)
            
        # результат
        return removed

def solve():
    # чтение данных
    input_data = sys.stdin.read().split()
    if not input_data:
        # завершение программы
        return
    
    # количество элементов
    n = int(input_data[0])
    # экземпляр кучи
    heap = MinHeap()
    
    # добавление элементов
    for i in range(1, n + 1):
        heap.insert(int(input_data[i]))
        
    # массив результатов
    result = []
    # извлечение элементов
    for _ in range(n):
        result.append(str(heap.delMin()))
        
    # вывод результата
    print(" ".join(result))

if __name__ == '__main__':
    solve()