class LinkedList():
    """
    LinkedList from scratch.
    """

    def __init__(self):
        self.__size = 0  # size of the linked list
        self.__first_node = None
        self.__last_node = None

    @property
    def size(self):
        return self.__size

    def add(self, data):
        """
        Add new data at the end of the linked list.
        :param data:
        :return:
        """
        data_node = self.Node(data)
        if self.__first_node is None:
            self.__first_node = data_node
            self.__last_node = data_node
        else:
            self.__last_node.next_node = data_node
            data_node.prev_node = self.__last_node
            self.__last_node = data_node
        self.__size = self.size + 1

    def add_by_index(self, data, index):
        """
        Add new data at the index-th node in the linked list.
        :param data:
        :param index:
        :return:
        """
        if index >= self.size:
            while index > self.size:
                self.add(self.Node(None))
            self.add(data)
        else:
            data_node = self.Node(data)
            nth_node = self.__first_node
            for i in range(index + 1):
                if i == index:
                    if i > 0:
                        nth_node.prev_node.next_node = data_node
                        data_node.prev_node = nth_node.prev_node
                    nth_node.prev_node = data_node
                    data_node.next_node = nth_node
                    nth_node = data_node
                    if i == 0:
                        self.__first_node = nth_node
                    self.__size = self.size + 1
                    break
                nth_node = nth_node.next_node

    def __str__(self):
        all_data_string = ""
        node = self.__first_node
        for i in range(self.size):
            all_data_string += "{0}-th data: {1}\n".format(i, node)
            node = node.next_node
        return all_data_string

    def __reversed__(self):
        all_data_string = ""
        node = self.__last_node
        for i in reversed(range(self.size)):
            all_data_string += "{0}-th data: {1}\n".format(i, node)
            node = node.prev_node
        return all_data_string

    class Node():
        """
        The LinkedList is composed with a group of Node instances.
        """

        def __init__(self, data):
            self.data = data
            self.__prev_node = None
            self.__next_node = None

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, new_data):
            self.__data = new_data

        @property
        def prev_node(self):
            return self.__prev_node

        @prev_node.setter
        def prev_node(self, node):
            if isinstance(node, LinkedList.Node):
                self.__prev_node = node

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, node):
            if isinstance(node, LinkedList.Node):
                self.__next_node = node

        def __str__(self):
            return str(self.__data)


if __name__ == '__main__':
    # node = Node("First Node")
    # print(node.prev_node)
    # print(node.next_node)
    #
    # node2 = Node("Second Node")
    # node.next_node = node2
    # node2.prev_node = node
    # print(node.prev_node)
    # print(node.next_node)
    # print(node2.prev_node)
    linked_list = LinkedList()
    print(linked_list)
    linked_list.add("First data")
    print(linked_list)
    print(reversed(linked_list))
    linked_list.add("Second data")
    linked_list.add("Third data")
    print(linked_list)
    print(reversed(linked_list))
    linked_list.add_by_index("New data", 2)
    print(linked_list)
    linked_list.add_by_index("New Start data", 0)
    print(linked_list)
    linked_list.add_by_index("New New data", 7)
    print(linked_list)
    print(reversed(linked_list))
