#include <iostream>
#include <algorithm>

using namespace std;

//поместится ли n дипломов на квадратной доске со стороной m
bool good(long long m, long long w, long long h, long long n) {
    long long cols = m / w;
    long long rows = m / h;
    
    // по какой-то стороне не влезает ни один диплом
    if (cols == 0 || rows == 0) return false;
    
    //если по одной из осей уже помещается n дипломов, (а по другой оси помещается хотя бы 1), то мы уже молодцы
    if (cols >= n || rows >= n) return true;

    return cols * rows >= n; 
}

int main() {
    long long w, h, n;
    if (!(cin >> w >> h >> n)) return 0;

    long long l = 0;
    long long r = n * max(w, h);

    while (r - l > 1) {
        long long m = l + (r - l) / 2;
        
        if (good(m, w, h, n)) {
            r = m; //if помещаются, уменьшаем доску
        } else {
            l = m; //не помещаются, доску увеличить
        }
    }

    cout << r << "\n";

    return 0;
}