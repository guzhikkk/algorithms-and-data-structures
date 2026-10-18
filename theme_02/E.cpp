#include <iostream>
#include <vector>

using namespace std;

bool good(const vector<int>& a, int k, int m) {
    int cows_count = 1; // 1 корову всегда ставим в первое стойло
    int last_box = a[0];// координата последней поставленной коровы
    
    for (size_t i = 1; i < a.size(); ++i) {
        if (a[i] - last_box >= m) {
            cows_count++;
            last_box = a[i];
        }
    }
    
    return cows_count >= k;
}

int main() {
    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int l = 0; 
    int r = a.back() - a.front() + 1; 

    while (r - l > 1) {
        int m = (l + r) / 2; 
        
        if (good(a, k, m)) {
            l = m; //увеличиваем расстояние если все получилось
        } else {
            r = m; // Если нет, значит расстояние  уменьшаем
        }
    }

    // в l останется максимально возможное минимальное расстояние
    cout << l << "\n";

    return 0;
}