__author__ = 'nadiaaly'
""" Author Nadia Aly, February 18, 2014, CSCI 241.
    In mathematics, a set is a collection of distinct objects. This part of the lab looks at sets, and the operations
    that can be done to sets. In probability, set notation is important in understanding how the probability of two or
    more events interact. The operations we look at are: checking the number of elements in a set, determining
    if an element is in the set, adding a unique element to the set, removing an element from a set, determining if
    two sets are equal and contain the same elements ("eq"), determining if one set is a subset of another set,
    finding the union of sets, finding the intersect, and finding the difference of sets.

    """


class Set :
    """Implementation of the Set ADT container using a Python list.

    """
    def __init__( self ):
        """Uses a list to creates an empty set instance

         """
        self._theElements = list()

    def __len__( self ):
        """Returns the number of items in the set by using the built-in 'len' operation

        """
        return len( self._theElements )

    def __contains__( self, element ):
        """Determines if an element is in a set

        Arguements:
        The element from set to check if is contained
        """
        return element in self._theElements

    def add( self, element ):
        """ Checks to make sure an element is not already in a set, and if it not, adds the new element to the set.

        """
        if element not in self :
            self._theElements.append( element )

    def remove( self, element ):
        """Removes an element from the set. As a precondition, the element must already be in the set

        """
        assert element in self, "The element must be in the set."
        self._theElements.remove( element )

    def __eq__( self, setB ):
        """Determines if two sets are equal. First this checks the length of the set vs the length of the other set

         and if the length is not equal it returns False because if two sets do not have the same length they could not

         possibly be equal.

         """
        if len( self ) != len( setB ) :
            return False
        else :
            return self.isSubsetOf( setB )

    def isSubsetOf( self, setB ):
        """Determines if this set is a subset of setB. If checks the elements of the set and if they are not in SetB it

        returns False, because if one element is not in setB then the tested set could not be a subset.

        """

        for element in self :
            if element not in setB :
                return False
            return True

    def union( self, setB ):
    """Creates a new set from the union of this set and setB

    """

        newSet = Set()
        """Creates an empty set called 'newSet'

        """
        newSet._theElements.extend( self._theElements )
        """adds the elements from the set to the new set that was just created. Checks to see for each element in setB

        if that element is not in the set, the element is then added to the subset.

        """
        for element in setB :
            if element not in self :
                newSet._theElements.append( element )
        return newSet

    def intersect( self, setB ):
        """Creates a new set from the intersection of this set A and B. The intersection contains only elements that

         are in both sets (or if there are more than one sets, of all these sets.

         """
        newSet = Set()
        """
        initializes a new empty set called newSet

        """
        for each in setB:
            newSet.add(each)
            """adds each element from set B to the newSet using the 'add' function
            """
        for element in setB :
            if element not in self:
                newSet._theElements.remove( element)
                """checks for each element in setB and if the element is not in the users set, the element is removed

                using the remove function.

                """
        return newSet

    def difference( self, setB ):
        """Creates a new set from the difference of two sets

        """
        returnSet = Set()
        newSet = Set()
        for each in self:
            newSet.add(each)
        for element in setB :
            if element in self:
                newSet._theElements.remove( element)
            """Uses a for loop to check if an element is in setB and if it is adds this to a set to test against

            user's set if the element is not in this set, then it is removed

            """
        return newSet


    def __iter__(self):
        return _SetIterator( self._theElements )

    def __str__(self):
        total = len(self)
        count = 1
        printer = '{'
        for each in self._theElements:
            each = str(each)
            printer += each

            if count ==len(self):
                printer+='}'
            else:
                printer += ', '
            count+=1

        return printer

class _SetIterator:
    """An iterator class for the Set ADT, based on the list/container

    """
    def __init__(self,theSet):
        self.setIter = theSet
        self.count = 0
    def __iter__(self):
        """Returns a reference to the set adt

        """
        return self
    def __next__(self):
        """ Returns the next object in the container

        """
        if self.count<len(self.setIter):
            ele = self.setIter[self.count]
            self.count+=1
            return ele
        else:
            raise StopIteration


