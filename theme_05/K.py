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

    def next_val(self, key):
        ans = -1
        curr = self.root
        
        # поиск следующего элемента
        while curr:
            # точное совпадение
            if curr.data == key:
                return curr.data
            # кандидат на ответ
            elif curr.data > key:
                ans = curr.data
                curr = curr.left
            # слишком маленькое значение
            else:
                curr = curr.right
                
        return ans

def main():
    # чтение всех данных
    tokens = sys.stdin.read().split()
    if not tokens:
        return
        
    n = int(tokens[0])
    tree = bst()
    
    last_op = ''
    last_y = 0
    idx = 1
    
    # обработка запросов
    for _ in range(n):
        if idx >= len(tokens):
            break
        cmd = tokens[idx]
        val = int(tokens[idx+1])
        idx += 2
        
        if cmd == '+':
            # вычисление значения после запроса
            if last_op == '?':
                val = (val + last_y) % 1000000000
            tree.insert(val)
            last_op = '+'
        elif cmd == '?':
            last_y = tree.next_val(val)
            print(last_y)
            last_op = '?'

if __name__ == '__main__':
    main()