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

    def check_balance(self):
        # пустое дерево
        if not self.root:
            return "YES"

        # стек для обхода
        stack = []
        curr = self.root
        # последний посещенный узел
        last_visited = None
        
        # словарь высот
        heights = {None: 0}
        
        # итеративный обратный обход
        while stack or curr:
            # спуск влево
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek_node = stack[-1]
                
                # переход вправо
                if peek_node.right and last_visited != peek_node.right:
                    curr = peek_node.right
                # обработка узла
                else:
                    node = stack.pop()
                    
                    # высота поддеревьев
                    left_h = heights.get(node.left, 0)
                    right_h = heights.get(node.right, 0)
                    
                    # разница высот
                    if abs(left_h - right_h) > 1:
                        return "NO"
                        
                    # запись высоты текущего узла
                    heights[node] = max(left_h, right_h) + 1
                    last_visited = node
                    
        return "YES"


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
    print(tree.check_balance())

if __name__ == '__main__':
    main()