#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& A) {
    int key, j;
    for (int i = 1; i < A.size(); i++) {
        key = A[i];
        j = i - 1;
        while (j >= 0 && A[j] > key) {
            A[j + 1] = A[j];
            j = j - 1;
        }
        A[j + 1] = key;
    }
}

int main() {
    vector<int> A;
    int num;
    
    while (cin >> num) {
        A.push_back(num);
    }
    
    InsertionSort(A);
    
    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }
    cout << endl;
    
    return 0;
}