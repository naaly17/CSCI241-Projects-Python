_author__ = 'Nadia Aly'
"""Author Nada Aly, March 23, 2015, CSCI 241, LAB 5: Generic Linked List
This lab looks at the linked list data structure. In this lab we have a doubly linked list, in which traversal can start
at the front and progress one element at a time to the end. The list can also have traversal start at the end and
progress one element at a time. The doubly linked list is made out of "nodes" or a collection of objects called nodes,
each contains a data item and a reference (explained later) to another node in the list. The linked list nodes have a
certain sequence, though no 'unique index.' The nodes can be thought of as a "chain of objects." Each list has three
pointers or "reference points" the 'header' points to the first node in the list, the 'tail' points to the last node
in the list, and the 'current' points to the 'current' pointer points too, or in this case, the current spot on the
list that we have traversed too. There are two classes in this lab the 'Node' Class which constructor contains a data
field to initiate the node with the item with two pointers (previous and next) and the 'GList' Class which constructor
contains a length field, with three pointers (head, tail, and current). The GList ADT must support the following
operations: initialize, contains, length, append, clear, findNext, findPrevious, get, getFirst, getLast, getNext,
getPrevious, insert, prepend, and move. Each separate function has a further description of what each operation does.
"""


class Node:
    """Creates a separate storage class 'Node.' Each list Node has three fields, a data field (item), and two pointers

    prev and _nex (point to previous node and next node from current node). The pointers are set to None because they

    do not have any reference points when the class is first initiated.
    """
    def __init__(self, item):
        self.item = item
        self._next = None
        self.prev = None


class GList:
    """Creates an empty List. Because there are no items in the list the length is set to None. Also, the pointers are

    all initiated and set to "None", because there are no items. There is header, tail, or current node when the list

    is empty (i.e. the head can not be referenced when there are no items/nodes,etc) these are all given values of None.
    """
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        self.curNode = None

    def __len__(self):
        """returns the number of items/nodes in the list

         """
        return self.length

    def append(self, item):
        """This operation appends an item to the end of the list. The newly appended node then becomes the current node.

        There are two cases to consider, if the list is empty and if the list has one or more items already when we append

        the node.

         """
        newNode = Node(item)
        #create a new node for the item
        if self.head is None:
            """This addresses the case and initiates an 'if' loop, if the list is empty and we append the first node/

            item. The newly appended node is then assigned a reference as the list's tail, head, and current node.

            Also, the next and pointer references are assigned. It follows that if the newly appended node is the first

            node then there will be no 'links' i.e. no previous or next node, so these are set to None.

            """
            self.head = newNode
            self.tail = newNode
            self.curNode = newNode
            self.curNode._next = None
            self.curNode.prev = None
        else:
        # The else takes all the other cases that need to be assigned references and pointers. The newly appended node
        #
        # is added to the end of the list, so the tail reference is then set to this node. This is done by setting the
        #
        # previous tail's "next" pointer linked to the new node and then the new node's previous pointer is set to the
        #
        # previous tail. The tail is then referenced as the new node. There were be no next node because we have added
        #
        # this node to the end of the list, so the next reference of the new Node is set to None. Finally, we then set
        #
        # the current node to the new Node


            self.tail._next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail._next = None
            self.curNode = newNode
            self.curNode._next = None
        self.length += 1
        #increment length by one (we add one node/item to the linked-list)

    def __contains__(self, item):
        """The contains operator returns the Boolean value of True/False indicating if an item is in a list (True if the

        item is in the list, false if the item is not) and is accessible through the 'in operator.' The current node is

        set to the header and a while loop is initiated and continues to run as long as the current node is not None

        (implying an empty list) and the item is not found. The while loop 'traverses' through the start of the list to

        the end by setting the current node equal to the current node's successor. Once the item is found,

        the while loop is exited (found condition no longer satisfied) and the node containing this item becomes the

        current item (i.e. current pointer is set to this node).

        """
        self.curNode = self.head
        found = False
        while self.curNode is not None and not found:
            if self.curNode.item ==item:
                found = True
            else:
                self.curNode = self.curNode._next

        return found

# finds the next occurrence of the item in the list from the current node
# (but not including the current) and returns True/False to indicate if the item is found.
#  As a side-effect, sets the current pointer to the newly found node.  Sets the current pointer to None if not found.

    def findNext(self, item):
        """Finds the next occurrence of an item in the list from where the current node is set, but not including the

        current node if the current node contains that item. So, starts at the current item, then goes to the next

        node, etc. If the item is found the Boolean value True is returned, if the item is not found, False is returned.

        The current pointer is set to to the newly found node. If the item is not found, the current pointer is then set

        to none.

        Precondition:
                      The current node must have been set (i.e. current pointer is not None).

        """
        assert self.curNode is not None
        found = False
        self.curNode = self.curNode._next
        while self.curNode is not None and not found:
            if self.curNode.item == item:
                found = True
            else:
                self.curNode = self.curNode._next

        return found



    def findPrevious(self,item):

        #  Finds the previous occurrence of an item in the list from where the current node is set, but not including the
        #
        # current node if the current node contains that item. So, starts at the current item, then goes to the previous
        #
        # node, etc. If the item is found the Boolean value True is returned, if the item is not found, False is returned.
        #
        # The current pointer is set to to the newly found node. If the item is not found, the current pointer is then set
        #
        # to none.
        #
        # Precondition:
        #         The current node must have been set (i.e. current pointer is not None).
        #

        assert self.curNode is not None

        self.curNode = self.curNode.prev
        found = False
        while self.curNode is not None and not found:
            if self.curNode.item ==item:
                found = True
            else:
                self.curNode=self.curNode.prev
        return found


    def get(self):
        """Returns the current data item of the node that the current pointer is set to (not the node structure, this is

       hidden!).If the current pointer is not set (i.e. does not exist), returns None.

       """
        if self.curNode is None:
            return None
        else:
            return self.curNode.item


    def getFirst(self):
        """This returns the first data item (not node structure) of the first node on the list (also referred to as the

        head. The current pointer is then set to the this very first node. Returns none if the current pointer is not set.

        """
        if self.head is None:
            return None
        else:
            self.curNode = self.head
        return self.curNode.item


    def getLast(self):
        """This returns the last data item (not node structure) of the last node on the list (also referred to as the

        tail. The current pointer is then set to the this very last node. Returns none if the current pointer is not set.

        """
        if self.tail is None:
            return None
        else:
            self.curNode = self.tail
            return self.curNode.item


    def getNext(self):
        """This operation returns the next item from the current node. (i.e. the current item of the current node's

         successor. This node this becomes the current node. If there is no next item from the current node, i.e. the

         current pointer is at the end of the list, then this operation returns "None" and the current pointer is set

         to none. I added the precondition that the current pointer must be set, because if it is not set, then the next

         node can not be referenced.

         Precondition:

                      The current node must have been set (i.e. current pointer is not None).

        """

        assert self.curNode is not None
        if self.curNode == self.tail:
            self.curNode = None
            return None
            #elif self.curNode._next is None:
            #return None
        else:
            self.curNode = self.curNode._next
            return self.curNode.item


    def getPrevious(self):
        '''"This operation returns the previous item from the current node. (i.e. the current item of the current node's

         predecessor. This node this becomes the current node. If there is no previous item from the current node, i.e. the

         current pointer is at the beginning of the list, then this operation returns "None" and the current pointer is set

         to none. I added the precondition that the current pointer must be set, because if it is not set, then the

         previous node can not be referenced.

         Precondition:

                      The current node must have been set (i.e. current pointer is not None).

        '''
        assert self.curNode is not None
        if self.curNode is self.head:
            self.curNode = None
            return None
        else:
            self.curNode = self.curNode.prev
            return self.curNode.item

    def insert(self, item):
        """This operation inserts an item at the position the current pointer is set to. The node at the current position

        then becomes the next node of the item that was just inserted. The current pointer is then set to the newly

        inserted node.

        Precondition:
                      The current node must have been set (i.e. current pointer is not None).
        """
        assert self.curNode is not None
        newNode = Node(item)
        #create a new node for the item

        if self.curNode is self.head:
            newNode._next = self.curNode
            newNode.prev = None
            self.head = newNode
            self.curNode = newNode

        else:

            self.curNode.prev._next=newNode
            newNode._next=self.curNode
            tempNode=self.curNode.prev
            self.curNode=newNode
            self.curNode.prev=tempNode

        self.length += 1
        #Incremends the length by one because a node is added to the list, so total number of nodes/items increases by 1


    def prepend(self, item):
        """Given the head as a pointer, 'prepend' adds an item to the beginning of the list and then by definition, the

        new item is the new header of that list. The node that we have just prepended is also then set to the current

        pointer. Order is important because the header's position to the new node must be referenced before assigning

        the header reference to the new node, otherwise in linked-lists can not go back and reference that item if done

        in the wrong order.

        """
        newNode = Node(item)
        #create a new node for the item

        if self.head is None:
            """This case is if a list starts out empty and the first node is added using prepend and not append.

            here, you can find this case by the list that does not have a header. The node that has just been

            prepended is then set to reference the tail, head, and current node. The next and previous pointers are

            set to 'None' so that it is clear that there is no node yet linked to our node (because list was

            empty prior).

            """
            self.head = newNode
            self.tail = newNode
            self.curNode = newNode
            self.curNode._next = None
            self.curNode.prev = None
        else:
            """
            This is the other case, were the list is not empty and has at least one other node. The header's 'previous'

            pointer is set to the newly prepended node, and the newly prepended node's pointer next is set towards the

            previous header- then the newly prepended node is set to reference the head and set to the current node.

            """
            self.head.prev = newNode
            newNode._next = self.head
            self.head=newNode
            self.curNode=self.head

        self.length += 1
        #increments count by one because we are adding one item/node to the list (at the beginning) so number of total
        #elements increases by one


    def remove(self):
        """
        In order to remove an item from a linked list the node containing that item must be "unlinked." This operation

        'removes' the current node (node the pointer is set to). There are three cases to consider: when the

        current node is on set on the head, tail, and middle of the list. I also added a case where the

        current node is the only node in the linked-list. I made this case so that the list would show that it is empty.


        Precondition:

                    The current node must have been set (i.e. current pointer is not None).

        """
        assert self.curNode is not None, "No current node is set"
        if self.curNode is self.head and self.length >= 2:
            '''In this case the current node is the head. This is a special case because it is an important reference and there

            is no predecessor (previous node) that will need to be relinked. However, the head reference must be changed to

            point to the next Node. This is done by changing the current node to the head's successor, then setting the

            current node's previous equal to None (removing the link to the head) and then changing the new head reference

            to reference the current node.
            '''

            self.curNode = self.curNode._next
            self.curNode.prev = None
            self.head = self.curNode

            '''If there is only one item in the list (i.e. the item does not have a previous or next node, the list becomes

            empty. Because the current node has no 'link's to a previous or next node, the node is removed by setting

            all references (head, tail, and current) to that node equal to None.
            '''
            self.head = None
            self.tail = None
            self.curNode = None
            print('list is empty')

        elif self.curNode is self.tail:
            """This case is the special case if the current pointer is set to the tail. It is similar to the header case. The

            tail does not have a next reference, so we just need to make sure that the tail's predecessor will no longer

            reference the tail as next (essentially removing the tail's link to the chain). The current node and tail is

            then set to the removed node's predecessor.
            """
            self.curNode = self.curNode.prev
            self.curNode._next = None
            self.tail = self.curNode

        else:
            """The remove case in which the current node is in the middle of the list: This case involves two references,

             must set the current node's next's previous pointer to the current node's previous pointer. Basically the

             nose after the current node can then reference the previous node as the node before the current node instead

             of the current node. Then the current node's previous node's next must be set to the current node's next.

             In similar words again, the current node's previous will set it's next reference to the node after the

             current node instead of the current node. Finally, create a temporary variable called 'tempNode'- used so

             that we can remove the link's to the current node and then be able to reference a node in the list after

             the link's are removed. The current node is then set to the removed node's previous successor. The node's

             link field is also set to none.

            """
            self.curNode._next.prev = self.curNode.prev
            self.curNode.prev._next = self.curNode._next
            tempNode = self.curNode._next
            self.curNode.prev = None
            self.curNode.next = None
            self.curNode = tempNode

        self.length -= 1
        #One node/item was removed from the linked-list, so the length of the node will decrement by one.

    def clear(self):
        """ This operation clears all the items from the list. The list becomes empty and all nodes are 'removed' from the

        list. The operation starts at the beginning of the list and initiates a while loop, as long as the current node

        is not None, it runs. In the while loop, the current node is set to the next node, and then the link from the

        previous node is then unlinked by setting the current node's previous node's next = None, the link attaching the

        current node's previous is then removed by setting it equal to None. Finally, all of the final 'references'

        head, tail, and current are then set to None so that the list (of length 1) may not be accessed by a reference

        either.

        """
        self.curNode = self.head
        while self.curNode != None:
            self.curNode = self.curNode.next
            self.curNode.prev._next = None
            self.curNode.prev = None

        self.curNode = None
        self.head = None
        self.tail = None
        self.length = 0
        #The length is now zero because the list is empty


