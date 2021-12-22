class DumbBalancedTree:
    """DumbBalancedTree inserts elements from left to right in order."""

    def __init__(self, root=None):
        self.__root = None
        self.__size = 0
        self.__level = 0
        self.insert(root)

    def insert(self, key):
        key_node = self.Node(key)
        if self.__root is None or self.__root.key is None:
            self.__root = key_node
            if self.__root.key is not None:
                self.__size += 1
                self.__level += 1
            return
        this_node = self.__root
        i = self.__level
        remaining = self.__size + 1 - 2 ** i
        while True:
            i -= 1
            if remaining // 2 ** i == 0:  # go to the left
                if this_node.left is None:
                    this_node.left = key_node
                    self.__size += 1
                    break
                else:
                    this_node = this_node.left
            else:  # go to the right
                if this_node.right is None:
                    this_node.right = key_node
                    self.__size += 1
                    if self.__size == 2 ** (self.__level + 1) - 1:
                        self.__level += 1
                    break
                else:
                    this_node = this_node.right
                    remaining -= 2 ** i

    def __repr__(self):
        return repr(self.__root)

    def __eq__(self, other):
        return repr(self) == repr(other)

    class Node:
        def __init__(self, key=None):
            self.__key = key
            self.__left = None
            self.__right = None

        @property
        def key(self):
            return self.__key

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, node):
            if node is None or isinstance(node, DumbBalancedTree.Node):
                self.__left = node

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, node):
            if node is None or isinstance(node, DumbBalancedTree.Node):
                self.__right = node

        def __repr__(self):
            return "--\nNode key: {}\n\tleft-child: {}\n\tright-child: {}".format(self.__key, self.__left, self.__right)


if __name__ == '__main__':
    range_tree = DumbBalancedTree()
    for i in range(1, 21):
        range_tree.insert(i)
    print(range_tree)
