'21번'
num=int(input('숫자를 입력하세요 : '))
a=0
for i in range(2,num):
    if num%i==0:
        a=1
if a==1 or num==0 or num==1:
    print(num,'는 소수가 아닙니다')
else:
    print(num,'는 소수입니다')



'23번'
n=int(input('숫자를 입력하세요 : '))
s=0
for i in range(n+1):
    s=s+(i**2)
print('결과는',s,'입니다.')



'29번'
연료=500
while 연료>=50:
    a=int(input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오 : '))
    연료+=a
    print('현재 탱크양은',연료,'입니다.')
print('경고 : 연료가 10% 미만이니 충전하세요!')
