# Nadia Aly, Lab 6: Stack-based Tools.
# There are two implementations commonly used to implement a stack. One can use a list or a singly linked list. I went
#with the singly linked structure because the previous lab used these and they are useful and with a large number
#of push and pop operations this is the best choice. The front of the list represents the top of the stack. This is
#easy to do because of the way the linked list works. With a stack the middle element can not be accessed unless each
#element from the top (head) of the stack is removed or somehow iterated. The stack ADT supports the following
#operations: initializer, isEmpty, len, peek, pop, and push. This stack code will be used in the next portion to
#preform a number of tasks. Because of it's "last in, first out" storage, this class is useful for several tasks.



class Stack:
    """Implements the Stack Abstract Data time with a singly linked list.
        """


    def __init__(self):
        """Constructor initializes the head as a reference point (this represents the top of the list) and size is

        the length of the list. Creates an empty stack.'
        """
        self._head = None
        self._size = 0


    def isEmpty(self):
        """If the stack is empty returns the Boolean Value true. This can be a helpful operation for example with a

        while statement or assert, has many uses.
        """

        return self._head is None


    def __len__(self):
        """ Returns the number of items in the stack.  Have been incrementing and decrementing this accordingly as we

            add/remove items.
            """
        return self._size


    def peek(self):
        """
            Returns the item on the top of the stack (item at the head references node). Peek operation returns

            the item without removing it.

                Precondition: The list cannot be empty, otherwise can not remove node/item from list.
            """
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._head.item


    def pop(self):
        """
            Removes and returns the top item on the stack.

                Precondition: The list cannot be empty, otherwise can not remove node/item from list.

            """
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._head
        self._head = self._head.next
        self._size -= 1
        #decrement size because we have removed a node/item from the list
        return node.item


    def push(self, item):
        """Pushes the item onto the top of the stack. This is similar to the prepend operation, but the only references

             we are concerned with are head and link.

            """
        self._head = _StackNode(item, self._head)
        self._size += 1
        #increment size by one because a new node has been added


class _StackNode:
    """Creates private storage class for creating the linked list nodes.

        """
    def __init__(self, item, link):
        """Initializes item and link, by including link here the prepend or 'push' operation is simplified.
        """
        self.item = item
        self.next = link










