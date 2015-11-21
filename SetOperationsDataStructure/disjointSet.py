__author__ = 'nadiaaly'
""" Author Nadia Aly, February 18, 2014, CSCI 241.
    This part of the lab looks at the properties of a disjoint-set.
    A disjoint-set is a set that contains smaller sets inside of the set. In order to be classified as disjoint,
    these smaller sets are called "subsets" and they can not have any common elements. The lab looks over the
    operations necessary for the disjoint-set. The operations we look over are length (to find out how many elements
    are in the subset, contains checks to see if an element is in a set, 'subset' returns the subset an element is
    inside in a disjoint set, 'add' add a new, unique element to the user's disjoint set, 'remove' removed an element
    from the subset, and 'union' finds the union of two subsets inside of a disjoint set

    """

from linearsetadt import Set
    """Imports the functions from the "linearsetadt" program to use in this program

    """

class DisjointSet:

    def __init__( self ):
        """Creates an empty set instance

        """
        self._theElements = Set()
        """Sets the rank equal to 0, the rank is the number of elements in a given set

        """
        self.rank = 0




    def __len__( self ):
        """Returns the number of elements in all subsets of the disjoint-set. The length corresponds to the number of

        elements and should not get confused with the number of subsets

        """
        return self.rank


    def __contains__( self, element ):
        """The operation "contains" uses a for loop to go through each subset in the disjoint set and for that subset,

        checks to see if the element is in it and if it is, the statement returns a boolean true value

        """
        for subSet in self._theElements:
            for each in subSet:
                if element in each:
                    return True

        return False

    def subset(self, element):
    """Given an element, the operation "subset" returns the subset the element belongs to

        Precondition:

            the element must be already in the disjoint-set.

            """
        for subSet in self._theElements:
            for each in subSet:
                if element in each:
                    return subSet

    def add( self, element ):
        """Adds a new unique element to the disjoint-set. To add the element, a new subset is created inside

         the disjoint-set, whose only member is that element and then the subset is added into the disjoint-set.

         """

        newSubset=Set()
        newSubset.add(element)
        """Precondition:

                the element is not in the disjoint-set already

        """
        assert newSubset not in self._theElements
        self._theElements.add( newSubset )
        """Since an element is added to the set, it follows that the rank should, by definition be increased by 1

        """
        for each in element:
            self.rank +=1
   .
    def remove( self, element):
        """Removes an element from its subset. Once the element is removed, if the subset becomes empty, the subset

         should be removed as well.

        Precondition:

            the element must already be in the disjoint-set.

            """

        assert element in self, "The element must be in the set."

        for subset in self._theElements:
            if element in subset._theElements:
                subset.remove(element)
                """Since an element is removed and no longer in the set, it follows that the rank should be reduced

                by 1

                """
                self.rank -= 1

    def union(self, element1,element2):
        """The "union" operation takes two elements and if they do not belong to the same subset, t

        he union of the sets is put into the disjoint-set. The two elements separate subsets are then removed.

        Precondition:
                        both elements must be already in the disjoint-set.

        """
        assert element1 in self
        assert element2 in self
        subSet1 = self.subset(element1)
        subSet2= self.subset(element2)
        """If the two subsets are already the same, then nothing is done to the set, otherwise both subsets are

        moved and the union is put inside the disjoint set

        """
        if subSet1 == subSet2:
            return
        else:
            unionsubset = subSet1.union(subSet2)
            self._theElements.remove(subSet1)
            self._theElements.remove(subSet2)
            self._theElements.add(unionsubset)







