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
        # максимальное количество уровней
        self.max_level = 0

    def insert(self, key):
        # пустое дерево
        if self.root is None:
            self.root = Node(key)
            self.max_level = 1
            return

        curr_node = self.root
        # текущий уровень узла
        current_level = 1
        
        # спуск по дереву
        while True:
            # дубликат элемента
            if key == curr_node.data:
                break
            
            # левая ветка
            if key < curr_node.data:
                current_level += 1
                if curr_node.left is None:
                    curr_node.left = Node(key)
                    # обновление рекорда глубины
                    if current_level > self.max_level:
                        self.max_level = current_level
                    break
                curr_node = curr_node.left
            
            # правая ветка
            else:
                current_level += 1
                if curr_node.right is None:
                    curr_node.right = Node(key)
                    # обновление рекорда глубины
                    if current_level > self.max_level:
                        self.max_level = current_level
                    break
                curr_node = curr_node.right

def main():
    tree = bst()
    # чтение всех данных из потока
    tokens = sys.stdin.read().split()
    
    # обработка последовательности
    for token in tokens:
        val = int(token)
        # конец ввода
        if val == 0:
            break
        tree.insert(val)
        
    # вывод результата
    print(tree.max_level)

if __name__ == '__main__':
    main()