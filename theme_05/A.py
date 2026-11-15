import sys

# узел дерева
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# бинарное дерево поиска
class bst:
    def __init__(self):
        # корень дерева
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)
            return "DONE"

        curr = self.root
        # спуск по дереву
        while True:
            if val == curr.data:
                return "ALREADY"
            elif val < curr.data:
                # левая ветка
                if not curr.left:
                    curr.left = Node(val)
                    return "DONE"
                curr = curr.left
            else:
                # правая ветка
                if not curr.right:
                    curr.right = Node(val)
                    return "DONE"
                curr = curr.right

    def search(self, val):
        curr = self.root
        # поиск узла
        while curr:
            if val == curr.data:
                return "YES"
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return "NO"

    def delete(self, val):
        parent = None
        curr = self.root

        # поиск целевого узла
        while curr and curr.data != val:
            parent = curr
            if val < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            return "CANNOT"

        # узел с двумя потомками
        if curr.left and curr.right:
            max_parent = curr
            max_node = curr.left

            # поиск максимума в левом поддереве
            while max_node.right:
                max_parent = max_node
                max_node = max_node.right

            # замена значения
            curr.data = max_node.data

            # подготовка к удалению дубликата
            curr = max_node
            parent = max_parent

        # потомок удаляемого узла
        child = curr.left if curr.left else curr.right

        # удаление корня
        if not parent:
            self.root = child
        # удаление левого узла
        elif parent.left == curr:
            parent.left = child
        # удаление правого узла
        else:
            parent.right = child

        return "DONE"

    def print_tree(self):
        # стек для обхода
        stack = []
        curr = self.root
        # уровень узла
        level = 0

        # итеративный вывод дерева
        while stack or curr:
            if curr:
                stack.append((curr, level))
                curr = curr.left
                level += 1
            else:
                curr, level = stack.pop()
                print('.' * level + str(curr.data))
                curr = curr.right
                level += 1

def main():
    tree = bst()
    # чтение всех строк из потока ввода
    lines = sys.stdin.read().splitlines()

    # обработка команд
    for line in lines:
        if not line:
            continue
        parts = line.split()
        cmd = parts[0]

        if cmd == "ADD":
            print(tree.add(int(parts[1])))
        elif cmd == "SEARCH":
            print(tree.search(int(parts[1])))
        elif cmd == "DELETE":
            print(tree.delete(int(parts[1])))
        elif cmd == "PRINTTREE":
            tree.print_tree()

if __name__ == '__main__':
    main()