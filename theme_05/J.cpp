#include <iostream>

using namespace std;

// узел дерева
struct Node {
    int data;
    int count;
    Node* left;
    Node* right;
    
    Node(int val) {
        data = val;
        count = 1;
        left = nullptr;
        right = nullptr;
    }
};

// добавление элемента
void insert(Node*& root, int key) {
    if (root == nullptr) {
        root = new Node(key);
        return;
    }
    
    Node* curr = root;
    // спуск по дереву
    while (true) {
        // дубликат узла
        if (key == curr->data) {
            curr->count++;
            break;
        } 
        // левая ветка
        else if (key < curr->data) {
            if (curr->left == nullptr) {
                curr->left = new Node(key);
                break;
            }
            curr = curr->left;
        } 
        // правая ветка
        else {
            if (curr->right == nullptr) {
                curr->right = new Node(key);
                break;
            }
            curr = curr->right;
        }
    }
}

// центрированный обход
void print_inorder(Node* node) {
    if (node == nullptr) return;
    
    print_inorder(node->left);
    cout << node->data << " " << node->count << "\n";
    print_inorder(node->right);
}

int main() {
    // ускорение потоков ввода-вывода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    Node* root = nullptr;
    int val;
    
    // чтение данных
    while (cin >> val && val != 0) {
        insert(root, val);
    }
    
    // вывод результата
    print_inorder(root);
    
    return 0;
}