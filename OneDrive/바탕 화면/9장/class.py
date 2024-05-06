class comx:
    def __init__(self,x,y):
        self.real=x
        self.imag=y
    def __add__(self,other):
        return comx(self.real+other.real,self.imag+other.imag)
    def __sub__(self,other):
        return comx(self.real-other.real,self.imag-other.imag)
    def __mul__(self,other):
        return comx(self.real*other.real-self.imag*other.imag,self.imag*other.real-self.real*other.imag)
    def __truediv__(self,other):
        return comx(self.real*other.real-self.imag*other.imag,self.imag*other.real-self.real*other.imag)
a=comx(1,2)
b=comx(2,3)
c=a+b
d=a-b
e=a*b
f=a/b
print(c,d,e,f)
