__author__ = 'nadiaaly'

from disjointSet import DisjointSet
from linearsetadt import Set

def main():
    #disjoint1 = Disjointset()
    #test add
    setA = Set()
    setA.add('a')
    setA.add('b')
    print(setA)

    setB = Set()
    setB.add('c')
    setB.add('d')

    setC = Set()
    setC.add('a')
    setC.add('b')




    setNumber = Set()
    for i in range(1,10,1):
        setNumber.add(i)
    setNumber2 = Set()
    for i in range(6,25,1):
        setNumber2.add(i)
    print(setNumber)
    print(setNumber2)



    print(setNumber.difference(setNumber2))
    print(setNumber.intersect(setNumber2))


    #test contains
   #print(setA.__contains__('a'))
    #print(setA.__contains__('f'))

    #test the iterator
    #for each in setA:
    #    print(each)


    #test intersect
    #for each in setB:
    #    print (each)

    set0 = setA.intersect(setB)
#    for each in set0:
 #       print (each)
    #print(len(set0))
    setInter = setA.intersect(setC)
    #print(setInter)
    disjoint1 = DisjointSet()
    #print(len(setA))
    disjoint1.add('a')
    disjoint1.add('b')
    disjoint1.add('c')


  #  print(disjoint1.__contains__('a'))

    #should be 4, not 2
    print(len(disjoint1))
    #should print true
 #   print(disjoint1.__contains__('a'))
    disjoint1.remove('a')

#    print(disjoint1.remove(setA))

#    print(disjoint1.__contains__('d'))
#    print(disjoint1.subset('a'))
    #disjoint1.remove('b')
    print(disjoint1.subset('c'))


    print(len(disjoint1))

    disjoint1.add('a')
    disjoint1.union('a','b')
    print(disjoint1.subset('a'))

main()