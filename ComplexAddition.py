class Complex:
    real=0
    img=0
    def __init__(self,a,b):
        self.real=a
        self.img=b
    def add(self,other):
        
        c=Complex(0,0)
        c.real=self.real+ other.real
        c.img=self.img+ other.img
        return c
    def display(self):
        
        print("{}+i{}".format(self.real,self.img))
c1= Complex(1,5)
c2= Complex(4,2)
c3= c1.add(c2)
c1.display()
c2.display()
c3.display()
