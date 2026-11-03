#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MinHeap {
private:
    // массив элементов
    vector<int> heap;

    void siftUp(int i) {
        // индекс родителя
        int p = (i - 1) / 2;
        while (i > 0 && heap[i] < heap[p]) {
            // обмен элементов
            swap(heap[i], heap[p]);
            // обновление индекса
            i = p;
            p = (i - 1) / 2;
        }
    }

    void siftDown(int i) {
        // размер кучи
        int n = heap.size();
        while (2 * i + 1 < n) {
            // левый потомок
            int left = 2 * i + 1;
            // правый потомок
            int right = 2 * i + 2;
            // минимальный потомок
            int j = left;
            if (right < n && heap[right] < heap[left]) {
                j = right;
            }
            if (heap[i] > heap[j]) {
                // обмен элементов
                swap(heap[i], heap[j]);
                // обновление индекса
                i = j;
            } else {
                break;
            }
        }
    }

public:
    void clear() {
        // очистка вектора
        heap.clear();
    }

    void insert(int x) {
        // добавление элемента
        heap.push_back(x);
        // просеивание вверх
        siftUp(heap.size() - 1);
    }

    void extract() {
        if (heap.empty()) {
            // вывод ошибки
            cout << "CANNOT" << "\n";
            return;
        }
        // минимальный элемент
        int mn = heap[0];
        heap[0] = heap.back();
        // удаление конца
        heap.pop_back();
        if (!heap.empty()) {
            // просеивание вниз
            siftDown(0);
        }
        // вывод результата
        cout << mn << "\n";
    }
};

int main() {
    // оптимизация ввода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // экземпляр кучи
    MinHeap h;
    // строка команды
    string command;
    while (cin >> command) {
        if (command == "CLEAR") {
            // очистка структуры
            h.clear();
        } else if (command == "ADD") {
            // значение элемента
            int x;
            cin >> x;
            h.insert(x);
        } else if (command == "EXTRACT") {
            // извлечение минимума
            h.extract();
        }
    }
    return 0;
}