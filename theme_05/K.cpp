#include <iostream>
#include <set>

using namespace std;

int main() {
    // ускорение потоков ввода-вывода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    // красно-черное дерево
    set<long long> bst;
    
    char last_op = ' ';
    long long last_y = 0;
    
    // обработка запросов
    for (int i = 0; i < n; ++i) {
        char cmd;
        long long val;
        cin >> cmd >> val;
        
        // добавление узла
        if (cmd == '+') {
            // вычисление значения
            if (last_op == '?') {
                val = (val + last_y) % 1000000000;
                // защита от отрицательного остатка
                if (val < 0) val += 1000000000;
            }
            bst.insert(val);
            last_op = '+';
        } 
        // поиск следующего
        else if (cmd == '?') {
            // поиск минимального элемента, большего или равного val
            auto it = bst.lower_bound(val);
            
            if (it != bst.end()) {
                last_y = *it;
            } else {
                last_y = -1;
            }
            
            // вывод результата
            cout << last_y << "\n";
            last_op = '?';
        }
    }
    
    return 0;
}