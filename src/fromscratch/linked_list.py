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
        :param data: any data to insert at the end of the linked list
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
        If the input is non-int type or negative value, ValueError will be raised.
        :param data: any data to insert at the index-th node
        :param index: non-negative int
        """
        if type(index) is not int or index < 0:
            raise ValueError("The index should be non-negative integer.")
        if index >= self.size:
            while index > self.size:
                self.add(None)
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
                    if i == 0:
                        self.__first_node = data_node
                    self.__size = self.size + 1
                    break
                nth_node = nth_node.next_node

    def get(self, index):
        """
        Get data at the index-th node in the linked list.
        This method searches from the first node if the index is closer to the first node. Otherwise, it searches from the last node.
        If the input is non-int type or negative value or above the size of the linked list, ValueError will be raised.
        :param index: non-negative int which is smaller than the size of the linked list
        :return: data at the index-th node
        """
        if type(index) is not int or index >= self.size or index < 0:
            raise ValueError(
                "The index should be non-negative integer and smaller than the size of the linked list ({}).".format(
                    self.size))
        if (self.size - 2 * index) >= 0:  # (size -1 - index) + (0 - index) > 0 then closer from the first node
            nth_node = self.__first_node
            for i in range(index + 1):
                if i == index:
                    return nth_node.data
                nth_node = nth_node.next_node
        else:
            nth_node = self.__last_node
            for i in range(self.size - 1, index - 1, -1):
                if i == index:
                    return nth_node.data
                nth_node = nth_node.prev_node

    def remove(self, index):
        """
        Remove data at the index-th node in the linked list.
        This method searches from the first node if the index is closer to the first node. Otherwise, it searches from the last node.
        If the input is non-int type or negative value or above the size of the linked list, ValueError will be raised.
        :param index: non-negative int which is smaller than the size of the linked list
        """
        if type(index) is not int or index >= self.size or index < 0:
            raise ValueError(
                "The index should be non-negative integer and smaller than the size of the linked list ({}).".format(
                    self.size))
        if self.size <= 1:
            self.__first_node = None
            self.__last_node = None
            self.__size = self.size - 1
        elif (self.size - 2 * index) > 0:  # (size -1 - index) + (0 - index) > 0 then closer from the first node
            nth_node = self.__first_node
            for i in range(index + 1):
                if i == index:
                    nth_node.next_node.prev_node = nth_node.prev_node
                    if i > 0:
                        nth_node.prev_node.next_node = nth_node.next_node
                    if index == 0:
                        self.__first_node = nth_node.next_node
                    self.__size = self.size - 1
                    break
                nth_node = nth_node.next_node
        else:
            nth_node = self.__last_node
            for i in range(self.size - 1, index - 1, -1):
                if i == index:
                    nth_node.prev_node.next_node = nth_node.next_node
                    if i < self.size - 1:
                        nth_node.next_node.prev_node = nth_node.prev_node
                    if index == self.size - 1:
                        self.__last_node = nth_node.prev_node
                    self.__size = self.size - 1
                    break
                nth_node = nth_node.prev_node

    def __iter__(self):
        """
        Make the LinkedList iterable.
        """
        self.__n = 0
        self.__iter_next_node = self.__first_node
        return self

    def __next__(self):
        if self.__n < self.size:
            iter_next_node = self.__iter_next_node
            self.__iter_next_node = self.__iter_next_node.next_node
            self.__n += 1
            return iter_next_node
        else:
            raise StopIteration

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
            if isinstance(node, LinkedList.Node) or node is None:
                self.__prev_node = node

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, node):
            if isinstance(node, LinkedList.Node) or node is None:
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
    # print(linked_list)
    linked_list.add("First data")
    # print(linked_list)
    # print(reversed(linked_list))
    linked_list.add("Second data")
    linked_list.add("Third data")
    # print(linked_list)
    # print(reversed(linked_list))
    linked_list.add_by_index("New data", 2)
    # print(linked_list)
    linked_list.add_by_index("New Start data", 0)
    # print(linked_list)
    linked_list.add_by_index("New New data", 7)
    print(linked_list)
    linked_list.add_by_index("Test data", 6)
    print(reversed(linked_list))
    print(linked_list.get(0))
    print(linked_list.get(3))
    print(linked_list.get(8))
    # print(linked_list.get(3.0))  # Error test
    linked_list.remove(5)
    print(linked_list)
    linked_list.remove(7)
    print(linked_list)
    linked_list.remove(5)
    print(linked_list)
    linked_list.remove(2)
    print(linked_list)
    linked_list.remove(0)
    print(linked_list)
    linked_list.remove(1)
    print(linked_list)
    print(linked_list.get(0))
    print(linked_list.get(1))
    print(linked_list.get(2))
    print("\n --- Iterator ---")
    ll_iter = iter(linked_list)
    for node in ll_iter:
        print(node)
        print("data: {0}\t\tprev_node: {1}\t\tnext_node: {2}".format(node.data, node.prev_node, node.next_node))
    ll_iter2 = iter(linked_list)
    print(ll_iter2.__next__())
    print(next(ll_iter2))
    print(ll_iter2.__next__())
    print(next(ll_iter2))
