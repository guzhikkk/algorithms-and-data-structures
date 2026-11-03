import heapq

# количество аквариумов
n = int(input())

# создание кучи
heap = []


for i in range(n):
    # начальная численность
    count = int(input())
    # время до первой рыбки
    time = max(1, 1000 - count)
    # добавление в кучу
    heapq.heappush(heap, (time, i, count))

# текущее время
current_time = 0
# текущий аквариум
current_aquarium = 0

# цикл обработки событий
while heap:
    # извлечение ближайшего события
    time, aquarium, count = heapq.heappop(heap)

    # вычисление расстояния
    distance = abs(aquarium - current_aquarium)

    # проверка опоздания
    if current_time + distance > time:
        # вывод времени опоздания
        print(time)
        break

    # обновление времени
    current_time = time
    # обновление позиции
    current_aquarium = aquarium

    # увеличение численности
    count += 1
    # время до следующей рыбки
    next_time = max(1, 1000 - count)

    # добавление нового события
    heapq.heappush(heap, (time + next_time, aquarium, count))