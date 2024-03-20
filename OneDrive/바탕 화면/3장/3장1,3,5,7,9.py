100>200
100>=200
100<200
100<=200
100==200
100!=200
200==200
200!=200
True or True
True or False
True and False
True and True
True or True and False
True and True or False
'Morning'<'morning'
'A'>'B'


age=int(input('나이를 입력하시오 : '))
height=int(input('키를 입력하시오(단위 cm) : '))
if age>=19 and height>=150:
    print('입장할 수 있습니다.')
else:
    print('입장할 수 없습니다.')



a=int(input('두 정수를 입력하시오 :'))
b=int(input('두 정수를 입력하시오 :'))
if a>b:
    print('b','a')
else:
    print('a','b')



game_score=int(input('게임점수를 입력하시오 : '))
if game_score>=1000:
    print('고수입니다.')
else:
    print('입문자입니다.')


n=int(input('정수를 입력하시오 : '))
if n%2==0:
    print(n,'는(은) 2(으)로 나누어 집니다.')
else:
    print(n,'는(은) 2(으)로 나누어지지 않습니다.')
if n%3==0:
    print(n,'는(은) 3(으)로 나누어집니다.')
else:
    print(n,'는(은) 3(으)로 나누어지지 않습니다.')
if n%2==0 and n%3==0:
    print(n,'는(은) 2와(과) 3 모두로 나누어집니다.')
else:
    print(n,'는(은) 2와(과) 3 모두로 나누어지지 않습니다.')
