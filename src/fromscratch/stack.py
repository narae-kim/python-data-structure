from linked_list import LinkedList


class Stack():
    """
    Stack from scratch by LinkedList implemented in the same package.
    """

    def __init__(self):
        self.__top_pointer = -1  # track the top of the stack
        self.__linked_list = LinkedList()

    @property
    def top_pointer(self):
        return self.__top_pointer

    def push(self, data):
        """
        Push the new data at the top of the stack.
        """
        self.__linked_list.add(data)
        self.__top_pointer = self.top_pointer + 1

    def pop(self):
        """
        Pop the data at the top of the stack.
        Return the data from the top of the stack if the stack is not empty. Otherwise, raise ValueError.
        """
        if self.__top_pointer >= 0:
            data = self.__linked_list.get(self.top_pointer)
            self.__linked_list.remove()
            self.__top_pointer = self.top_pointer - 1
            return data
        else:
            raise ValueError("Stack is empty already.")

    def __str__(self):
        return str(self.__linked_list)


if __name__ == '__main__':
    stack = Stack()
    print(stack)
    stack.push(1)
    stack.push(2)
    print(stack)
    data = stack.pop()
    print(stack, data)
    stack.push(3)
    print(stack)
    data = stack.pop()
    print(stack, data)
    data = stack.pop()
    print(stack, data)
    stack.pop()  # error test
