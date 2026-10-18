#include <iostream>
#include <vector>

using namespace std;

//можно ли нарезать k веревочек длиной m
bool good(const vector<int>& a, int k, int m) {
    long long cnt = 0; 
    
    for (int ln : a) {
        cnt += ln / m; //количество кусков длины m из одной веревки
    }
    
    return cnt >= k; //набралось ли нужное количество
}

int main() {
    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    //100 км = 10 000 000 см, правая граница 10^7 + 1
    int l = 0;
    int r = 10000001; 

    while (r - l > 1) {
        int m = l + (r - l) / 2;
        
        if (good(a, k, m)) {
            l = m; 
        } else {
            r = m; 
        }
    }

    cout << l << "\n";

    return 0;
}