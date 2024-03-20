'13번'
x,y=map(int,input('점의 좌표 x,y를 입력하시오 : ').split())
if ((x-3)**2+(y-4)**2)**(1/2)<=10:
    print('원의 내부에 있음')
else:
    print('원의 외부에 있음')


'15번'
i=0
for i in range(8):
    i=i+1
    print(i*2)

i=0
while i<9:
    i=i+1
    print(i*2)


'17번'
for i in range(3):
    print('Python')
    print('is')
    print('FUN!')
#Python, is, FUN!이 3번씩 출력됨

for i in range(3):
    print('Python')
    print('is.')
print('FUN!')
#3번째 print줄에서 오류가 발생

for i in range(3):
    print('Python')
print('is')
print('FUN!')
#2번째 print줄에서부터 오류 발생


'19번'
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('-햄버거(입력 b)')
print('-치킨(입력 c)')
print('-피자(입력 p)')
selected=None
selected=input('메뉴를 선택하세요(알파벳 b, c, p 입력) : ')
while selected not in['b','c','p']:
    selected=input('메뉴를 다시 입력하세요(알파벳 b, c, p 입력): ')
if selected=='b':
    print('햄버거를 선택하였습니다.')
elif selected=='c':
    print('치킨을 선택하였습니다.')
elif selected=='p':
    print('피자를 선택하였습니다.')
