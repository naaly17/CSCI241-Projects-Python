"""


fractions class

simplify rational fractions


citations:

LCM: https://gist.github.com/endolith/114336

GCD: http://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python

simplifying in constructor:  http://codereview.stackexchange.com/questions/66450/simplify-a-fraction

author: nadia aly



"""



class Fraction:


    def __init__(self,numer,denom):
        ###simplify rational fractions###
        assert type(numer) == int
        assert type(denom) == int
        assert denom>0


        common_factor = 1
        self.numer = numer
        self.denom = denom

        for i in range(min(abs(numer), abs(denom)), 1, -1):
            if numer % i == 0 and denom % i == 0:
                common_factor = i
                break

        self.numer = self.numer/common_factor
        self.denom = self.denom/common_factor
        self.numer = int(self.numer)
        self.denom = int(self.denom)

    def __str__(self):
        """:return string version of fraction"""
        return str(self.numer)+"/"+str(self.denom)

    def __add__(self,other):
        """add overload: return fraction type"""
        gcdToUse = lcm(self.denom,other.denom)


        bottom = self.denom * gcdToUse
        top = self.numer * gcdToUse
        bottom2 = other.denom * gcdToUse
        top2 = other.numer * gcdToUse
        print (other.denom)
        print ('numerator for add is ' + str(top+top2))
        print (bottom2)
        return Fraction((top + top2),(gcdToUse*self.denom))

    def __sub__(self, other):
        """sub overload: return Fraction type"""
        gcdToUse = lcm(self.denom,other.denom)

        bottom = self.denom *gcdToUse
        top = self.numer*gcdToUse
        bottom2 = other.denom*gcdToUse
        top2 = other.numer*gcdToUse

        return Fraction((top-top2),(gcdToUse*self.denom))

    def __mul__(self, other):
        """multiplies fractions, returns fraction type.  Because returns fraction type not entirely accurate
        as floats will be rounded to floor via gcd function"""

        lcdenom = lcm(self.denom,other.denom)

        mulDenom = other.denom*self.denom
        mulNumer = other.numer*self.numer

        return Fraction(mulNumer,mulDenom)


    def __truediv__(self, other):
        "return new Fraction of divided number"
        divTop = self.numer*other.denom
        divBottom = self.denom*other.numer

        return Fraction(divTop,divBottom)

    def __lt__(self,other):
        """return true if x<y"""
        floater = self.numer/self.denom
        otherFloater = other.numer/other.denom

        if floater<otherFloater:
            return True
        else:
            return False

    def __le__(self, other):
        """less than or equal: return true if le or false if otherwise"""
        floater = self.numer/self.denom
        otherFloater = other.numer/other.denom
        if floater == otherFloater:
            return True
        elif floater<otherFloater:
            return False
        else:
            return False
    def __ne__(self, other):
        """return true if self not equal to other, false otherwise"""
        floater = self.numer/self.denom
        otherFloater = other.numer/other.denom

        if floater == otherFloater:
            return False
        else:
            return True




def gcd(x,y):
        while y != 0:
            (x, y) = (y, x % y)
        return x



def lcm(a, b):
    print ('lcm is ' + str((a*b)//gcd(a,b)))
    return (a * b) // gcd(a, b)

    #return reduce(lcm, numbers, 1)