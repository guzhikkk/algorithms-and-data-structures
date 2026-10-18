#include <iostream>
#include <algorithm> 

using namespace std;

// успеют ли два ксерокса сделать cnt копий за время t
bool good(long long cnt, long long q, long long s, long long t) {
    return (t / q + t / s) >= cnt;
}

int main() {
    long long n, quick, slow;
    if (!(cin >> n >> quick >> slow)) return 0;

    // в quick всегда  время более быстрого ксерокса
    if (quick > slow) {
        swap(quick, slow);
    }

    long long l = 0;
    long long r = (n - 1) * slow; //худший вариант все оставшиеся копии делает медленный

    while (r - l > 1) {
        long long m = l + (r - l) / 2;
        
        // if за время m мы не успеваем сделать n - 1 копий
        if (!good(n - 1, quick, slow, m)) {
            l = m;
        } else {
            r = m;
        }
    }

    //результат время на самую первую копию + минимальное время на оставшиеся, которое нашли
    cout << r + quick << "\n";

    return 0;
}