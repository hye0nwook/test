'9.1'
(123).__add__(334)

(123).__sub__(334)

(123).__mul__(334)

(123).__truediv__(3)

'9.3'
'사용가능=upper()'
'사용 불가능=pop(),sort(),append(),insert(),remove()'

'9.5'
a=1
b=1
c=2
d=3
e=3
print("a와 b는 같은 객체인가? ",(a is b)) 
print("b와 c는 같은 객체인가? ",(b is c)) 
print("a와 b는 같은 객체인가? ",(c is d)) 
print("b와 c는 같은 객체인가? ",(d is e))

'9.7'
class dog:
    def __init__(self,name,age): 
        self.name=name 
        self.age=age  
    def __str__(self): 
        return '이름은 {}이고,나이는 {}살 입니다.'.format(my_dog.name, my_dog.age)
my_dog=dog("Mango",3)
print(my_dog)
