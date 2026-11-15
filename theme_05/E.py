import sys

# узел дерева
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# бинарное дерево поиска
class BST:
    def __init__(self):
        # корень дерева
        self.root = None

    def insert(self, key):
        # пустое дерево
        if self.root is None:
            self.root = Node(key)
            return

        curr_node = self.root
        
        # спуск по дереву
        while True:
            # дубликат узла
            if key == curr_node.data:
                break
            
            # левая ветка
            if key < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = Node(key)
                    break
                curr_node = curr_node.left
            
            # правая ветка
            else:
                if curr_node.right is None:
                    curr_node.right = Node(key)
                    break
                curr_node = curr_node.right

    def print_inorder(self):
        # стек для обхода
        stack = []
        curr = self.root
        
        # итеративный центрированный обход
        while stack or curr:
            # спуск влево
            if curr:
                stack.append(curr)
                curr = curr.left
            # обработка узла и переход вправо
            else:
                curr = stack.pop()
                print(curr.data)
                curr = curr.right

def main():
    tree = BST()
    # чтение всех данных
    tokens = sys.stdin.read().split()
    
    # обработка последовательности
    for token in tokens:
        val = int(token)
        # конец ввода
        if val == 0:
            break
        tree.insert(val)
        
    # вывод результата
    tree.print_inorder()

if __name__ == '__main__':
    main()