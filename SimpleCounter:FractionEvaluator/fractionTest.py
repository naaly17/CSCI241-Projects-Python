from fraction import Fraction
def main():

    #general test of constructor
    fraction1 = Fraction(2,5)
    fraction3 = Fraction(6,36)

    #fraction2 = Fraction(2.5,3.5)
    print (fraction1)
    print (fraction3)
    print (Fraction(36,180))

    #test add
    fraction5 = fraction1+fraction3

    #test subtract
    print (fraction5-fraction1)


    #test multilply - result should be 3/8
    fraction6 = Fraction(1,2)
    fraction7 = Fraction(3,4)
    print(fraction6*fraction7)


    #test divide - result should be 1/2
    fraction8 = Fraction(25,100)
    fraction9 = Fraction(500,1000)
    print(fraction8/fraction9)

    #test less than
    if (fraction6<fraction8):
        print("not true should not print")

    if (fraction6>fraction8):
        print("should print")

    #not equal
    if (fraction6 != fraction7):
        print ("ne should print")

    if (fraction6==fraction6):
        print("equal should print")
main()