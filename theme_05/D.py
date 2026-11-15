import sys

# узел дерева
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# бинарное дерево поиска
class bst:
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

    def second_max(self):
        curr = self.root
        
        # поиск узла
        while True:
            # случай с левым поддеревом без правого потомка
            if curr.left and not curr.right:
                curr = curr.left
                # поиск максимума в левом поддереве
                while curr.right:
                    curr = curr.right
                return curr.data
            
            # случай с листом справа
            if curr.right and not curr.right.left and not curr.right.right:
                return curr.data
            
            # шаг вправо
            curr = curr.right

def main():
    tree = bst()
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
    print(tree.second_max())

if __name__ == '__main__':
    main()