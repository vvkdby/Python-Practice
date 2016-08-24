class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num,"/",self.den)
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum/common,newden/common)
    def __eq__(self,other):
        numone = self.num*other.den
        numtwo = self.den*other.num
        return numone == numtwo
    def __mul__(self, other):
        newnumer = self.num*other.num
        newdenom = self.den*other.den
        hcf = gcd(newnumer,newdenom)
        return Fraction(newnumer/hcf,newdenom/hcf)
    def __lt__(self,other):
        return self.num*other.den < self.den*other.num


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


x = Fraction(1,2)
y = Fraction(6,1)
print(x+y)
print(x == y)
print(x*y)
print(x<y)
