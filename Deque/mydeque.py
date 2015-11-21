"""This module provides an implementation of the Deque Abstract Data Type.

The ADT is implemented in class Bag.

Author: Nadia Aly (naaly)

A deque is a linear collection that supports item insertion and removal at both the front and back ends. I implemented

my deque abstract data structure using a doubly linked list. The queue is a special list with a limited number of

operations in which items can be added from one end and removed from another, in the deque, a limited number of

operations are also supported, but items can be added or removed at the end or the front of the list.  This structure

is commonly used in computer science for problems that involve data that must be processed in the order it was

received (example: printer uses a queue such that multiple people can send items to the printer and the printer

prints off items in the order they were received). The queue data structure can also be implemented with a vector or an

array. In a queue to append an item to the end of a list is called  "enqueu" and to remove the first element of the

list is called "dequeue". There are two classes in this lab the 'DequeNode' Class which is a private storage class for

creating deque nodes, with a data field to initiate the node with the item with two pointers (previous and next) and

the 'GList' Class which constructor contains a length field, with two pointers (head, tail,). The Deque ADT must

support the following operations: init (initialize), isEmpty, len (length), addFirst, addLast, removeFirst, removeLast,

peekFirst, and peekLast. Each separate function has a further description of what each operation does.

"""

class MyDeque :
    """Deque ADT

    Creates an empty deque. Because there are no items in the deque, length is set to 0. Also, the pointers are
    all initiated and set to "None", because there are no items there is header, tail, or current node when the list
    is empty (i.e. the head can not be referenced when there are no items/nodes,etc) these are all given values of None.
    """

    def __init__(self):
        """Constructs an empty Deque"""
        self._qhead = None
        self._qtail = None
        self._count = 0


#isEmpty(): Returns a boolean value indicating whether the deque is empty.
    def isEmpty(self):
        return self._qhead is None

#Should this be length or len?
    def __len__(self):
        """Returns the number of items currently in the deque."""
        return self._count


#Is thi definition of how the queue node used correct?
    def addFirst(self, item):
        """ Adds a specified item to the front of the Deque.

        Arguments:
        item -- the data item to be added to the Deque (use node of the double linked list to store & construct item)
        """
        newNode = _DequeNode(item)
        if self.isEmpty():
            self._qhead =self._qtail= newNode
            self._qhead.next=None
            self._qhead.prev=None
        else:
            self._qhead.prev= newNode
            newNode.next = self._qhead
            self._qhead=newNode

        self._count += 1
        #Increment count by one. Have added one item to the Deque


    def addLast(self, item):
        """ Adds a specified item to the back of the Deque.

        Arguments:
        item -- the data item to be added to the Deque (use node of the double linked list to store & construct item)
        """
        newNode = _DequeNode(item)
        if self._qhead is None:
            self._qhead = self._qtail = newNode
        else:
            newNode.prev = self._qtail
            newNode.next = None
            self._qtail.next = newNode
            self._qtail = newNode
        self._count += 1
        #Increment count by one. Have added one item to the Deque


    def removeFirst(self):
        """ Removes and returns the first item from the Deque

        Precondition:
            The Deque cannot be empty, cannot remove from empty Deque.

        Returns:
            the data item removed from the Deque
        """
        assert not self.isEmpty()
        newNode = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        else:
            self._qhead = self._qhead.next

        self._count -= 1
        #Decrement count by one, have removed an item from the Deque.
        return newNode.item


    def removeLast(self):
        """ Removes and returns the last item from the Deque

        Precondition:
            The Deque cannot be empty, cannot remove from empty Deque.

        Returns:
            the data item removed from the Deque
        """
        assert not self.isEmpty()
        lastNode=self._qtail
        if self._qhead is self._qtail:
            self._qhead = None
            self._qtail = None
        else:
            newNode=self._qtail.prev
            newNode.next=None
            self._qtail=newNode
        self._count -=1
        #Decrement count by one, have removed an item from the Deque.
        return lastNode.item


    def peekFirst(self):
        """Returns the first item of the deque. Does not remove item. If the deque is empty, returns None. """
        if self.isEmpty():
            return None
        else:
            return self._qhead.item




    def peekLast(self):
        """Returns the last item of the deque. Does not remove item. If the deque is empty, returns None. """
        if self.isEmpty():
            return None
        else:
            return self._qtail.item



class _DequeNode(object):
    """Creates a private storage class '_DequeNode" for creating linked Nodes.
    """
    def __init__(self, item):
        """Each list Node has three fields, a data field (item), and two pointers prev and next (links to the previous
        node and next node). The pointers are set to None because they do not have any reference points when the class
        is first initiated.
        """
        self.item = item
        self.prev = None
        self.next = None