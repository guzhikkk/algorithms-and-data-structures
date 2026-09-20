#include <vector>
#include <algorithm>
#include <iostream>
 
void countSort(std::vector<int>& arr) {
    if (arr.empty()) return;
    int k = *std::max_element(arr.begin(), arr.end());
    std::vector<int> counter(k + 1, 0);
    
    for (int x : arr) {
        counter[x]++;
    }
    
    arr.clear();
    for (int num = 0; num <= k; ++num) {
        for (int i = 0; i < counter[num]; ++i) {
            arr.push_back(num);
        }
    }
}

int main()
{
    int x;
    std::vector<int> arr;
    while (std::cin >> x) {
        arr.push_back(x);
    }
    countSort(arr);
    for (int y : arr) {
        std::cout << y << " ";
    }
    return 0;
}
