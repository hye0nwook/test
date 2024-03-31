'4.1'
def my_greet():
    print('환영합니다.')
my_greet()
my_greet()

'4.3'
def max2(m,n):
    if m>n:
        return m
    else:
        return n

def min2(m,n):
    if m<n:
        return m
    else:
        return n
print('100과 200중 큰 수는 :',max2(100,200))
print('100과 200중 작은 수는:',min2(100,200))

'4.5'
def inch2cm(a):
    return 2.54*a
print('1 인치 =',inch2cm(1),'센티미터')
print('2 인치 =',inch2cm(2),'센티미터')
print('3 인치 =',inch2cm(3),'센티미터')
print('4 인치 =',inch2cm(4),'센티미터')
print('5 인치 =',inch2cm(5),'센티미터')

'4.7'
a,b,c=map(int,input('세 수를 입력하시오 : ').split())
def mean3(a,b,c):
    return int(a+b+c)/3
print(a,b,c,'의 평균값은',mean3(a,b,c))
def max3(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    if c>a and c>b:
        return c
print(a,b,c,'의 최댓값은',max3(a,b,c))
def min3(a,b,c):
    if a<b and a<c:
        return a
    if b<a and b<c:
        return b
    if c<a and c<b:
        return c
print(a,b,c,'의 최솟값은',min3(a,b,c))

'4.11'
x1=int(input('x1 좌표를 입력하시오 : '))
y1=int(input('y1 좌표를 입력하시오 : '))
x2=int(input('x2 좌표를 입력하시오 : '))
y2=int(input('y2 좌표를 입력하시오 : '))
def area(x1,y1,x2,y2):
    return ((x2-x1)*(y2-y1))/2
print('직각삼각형의 면적은 : ',area(x1,y1,x2,y2))
        
    
'4.13'
def 정육면체(s):
    return s**3
print('모서리의 길이가 12인 정육면체의 부피 : ',정육면체(12))
print('모서리의 길이가 20인 정육면체의 부피 : ',정육면체(20))
def 직육면체(w,h,l):
    return w*h*l
print('가로, 세로, 길이가 각각 3,5,6인 직육면체의 부피 : ',직육면체(3,5,6))
def 원뿔(r,h):
    return (1/3)*3.14*r**3*h
print('반지름과 높이가 각각 20,10인 원뿔의 부피 : ',원뿔(20,10))
def 구(r):
    return (4/3)*3.14*r**3
print('반지름이 15인 구의 부피 : ',구(15))
def 원기둥(r,h):
    return 3.14*r**2*h
print('반지름과 높이가 각각 20,10인 원기둥의 부피 : ',원기둥(20,10))

'4.19'
def fibonacci(n):
    if n <=1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))

'4.23'
r=int(input('반지름을 입력하시오 : '))
def area_and_circumference(r):
    r1=r**2*3.14
    r2=r*2*3.14
    return r1, r2
result1,result2=area_and_circumference(r)
print('넓이 :',result1,',','둘레 :',result2)
