class IntBinaryTree:
    def __init__(self, root=None):
        self.__root = None
        self.insert(root)

    def insert(self, key):
        """
        If the key is neither type 'int' nor NoneType, raise ValueError.
        In this IntBinaryTree class, if the key already exists in the tree, we skip updating.
        If the key is less than a node, it goes to the left.
        If the key is greater than a node, it goes to the right.
        """
        if not isinstance(key, int) and key is not None:
            raise ValueError("The key type has to be 'int'.")
        key_node = self.Node(key)
        if self.__root is None or self.__root.key is None:
            self.__root = key_node
            return
        this_node = self.__root
        while True:
            if key == this_node.key:
                break
            elif key < this_node.key:
                if this_node.left is None:
                    this_node.left = key_node
                    break
                else:
                    this_node = this_node.left
            elif key > this_node.key:
                if this_node.right is None:
                    this_node.right = key_node
                    break
                else:
                    this_node = this_node.right

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
            if node is None or isinstance(node, IntBinaryTree.Node):
                self.__left = node

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, node):
            if node is None or isinstance(node, IntBinaryTree.Node):
                self.__right = node

        def __repr__(self):
            return "--\nNode key: {}\n\tleft-child: {}\n\tright-child: {}".format(self.__key, self.__left, self.__right)


if __name__ == '__main__':
    tree = IntBinaryTree(5)
    print(tree)
    tree.insert(3)
    tree.insert(7)
    tree.insert(8)
    tree.insert(6)
    tree.insert(3)
    tree.insert(4)
    tree.insert(1)
    tree.insert(2)
    print(tree)
