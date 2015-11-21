__author__ = 'nadia aly'
from arrayADT import Array
from _arrayIterator import _ArrayIterator


class Vector:
    def __init__(self):
        self.vector_helper = Array(2)
        self.capacity = 2
        self.items_in_vector = 0

    def __len__(self):
        return self.items_in_vector

    def __contains__(self, item):
        # arrayIterator appears to not work.  Henceforth all iterations will be done manually.
        # Aw it does work :-/ - commented out the manual iteration


        # for i in range(0,self.items_in_vector-1,1):
        # if item == self.vector_helper[i]:
        # return True
        #     else:
        #         return False

        if item in self.vector_helper:
            return True
        else:
            return False

    def __getitem__(self, ndx):
        assert ndx > -1
        assert type(ndx) == int
        assert ndx <= self.capacity
        # self.items_in_vector

        return self.vector_helper[ndx]

    def __setitem__(self, ndx, item):
        assert ndx > -1
        assert type(ndx) == int
        assert ndx <= self.items_in_vector

        # self.items_in_vector += 1
        self.vector_helper[ndx] = item

    def append(self, item):
        # double the size of the array if necessary
        # the_length = len(self)

        if self.items_in_vector == 0:
            self.vector_helper[0] = item
            self.items_in_vector += 1

        elif self.capacity == self.items_in_vector:
            # if the array is full, double it.  do this by creating another array
            # vector3 = Array()
            vector2 = Array(self.capacity * 2)

            item_2 = item
            vector2.__setitem__((self.capacity), item)
            for i in range(0, self.items_in_vector, 1):
                vector2[i] = self.vector_helper[i]
            self.vector_helper = Array(self.capacity * 2)

            #self.vector_helper[self.items_in_vector+1] = item_2
            self.capacity *= 2
            self.items_in_vector += 1
            for i in range(0, self.items_in_vector, 1):
                self.vector_helper[i] = vector2[i]

        elif self.items_in_vector < self.capacity:
            self.vector_helper[self.items_in_vector] = item
            self.items_in_vector += 1
            # elif self.capacity == self.items_in_vector:
            # self.capacity = self.capacity *2

            #if self.items_in_vector < self.capacity:
            #self.vector_helper[self.items_in_vector] = item

    def insert(self, ndx, item):
        # shift up not down. Disregard the instructions
        # The items in the elements at and following the given position are shifted down to make room for the new item. ndx must be within the valid range.

        # check to see if in valid range - meaning not after a blank element
        assert ndx > -1

        if self.items_in_vector == (ndx) and ndx == 0:
            self.append(item)
            # self.items_in_vector += 1
            return
        # cannot insert if (ndx+2) is greater than the current items in vector
        elif self.items_in_vector < (ndx):
            print('cannot insert item, outside of range')
            return

        # insert an item in the last slot of a full vector; so len equals the position -1
        elif self.items_in_vector == (ndx - 1):
            # run append
            self.append(item)
            # self.items_in_vector += 1
            return

        # insert item in the 'middle' of a vector - full .  So ndx <self.capacity-1.
        # shifting up will not cause a problem
        elif ndx < (self.capacity):
            # first shift everything up
            for i in range((self.items_in_vector - 1), 0, -1):
                self.append(self.vector_helper[self.items_in_vector - 1])

            self.vector_helper[ndx] = item
            self.items_in_vector += 1


            # other cases??

    def remove(self, ndx):

        # it looks like the only way to truly remove is to make a new array.

        assert ndx > -1
        assert type(ndx) == int
        assert ndx < self.capacity

        # remove item at ndx, shift everything after down
        # so start at the ndx, vector[ndx+1 = ndx], move up by 1
        # case 0: index out of range
        if ndx >= self.items_in_vector:
            print("Index out of suitable range")
        # case 1: remove the last item
        if (ndx + 1) == self.capacity and self.capacity == self.items_in_vector:
            element = self.vector_helper[ndx]
            self.vector_helper[ndx] = None
            self.items_in_vector -= 1

            # should slice and make a new array...
            # vector_helper2 = Array(self.capacity)
            # for i in range(0, self.items_in_vector,1):
            # vector_helper2[i] = self.vector_helper[i]
            # self.vector_helper = vector_helper2
            return element



        else:
            element_to_return = self.vector_helper[ndx]
            for i in range(ndx, (self.items_in_vector - 1), 1):
                self.vector_helper[ndx] = self.vector_helper[ndx + 1]
            self.items_in_vector -= 1
            self.vector_helper[self.items_in_vector] = None
            # vector_helper2 = self.vector_helper
            # for i in range(0, (self.items_in_vector-1) ,1):
            # vector_helper2[i] = self.vector_helper[i]
            #self.vector_helper = vector_helper2
            # should slice and dice
            return element_to_return

    def indexOf(self, item):
        # the item must be in the list
        # not sure what that means?  Does that mean that we can assume
        # the item is in the list, or that it should be done through an assert?

        for i in range(0, self.items_in_vector - 1, 1):
            if self.vector_helper[i] == item:
                return i


    def extend(self, otherVector):
        for item in otherVector:
            self.append(item)

    def subVector(self, start, to):
        # from and to must be in valid range
        # renamed from to start because of python parameter problems
        # returns the subVector


        assert start >= 0
        assert start < self.__len__()
        assert to < self.__len__()
        assert to >= 0
        #assert to > start  should this be in such an order?

        new_vector = Vector()
        for i in range(start, to, 1):
            new_vector.append(self.vector_helper[i])
            #for j in range(0,self.capacity,1):
            #new_vector.vector_helper[j] = self.vector_helper[start]
        return new_vector

    def __iter__(self):
        return _ArrayIterator(self.vector_helper)


    def __str__(self):
        for item in self.vector_helper:
            if type(item) is None:
                return
            else:
                print(str(item))



