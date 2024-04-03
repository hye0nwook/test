'5.1'
list_ex=[10,20,30,40,50,60,70]
high=5
low=3
print(list_ex[low])
print(list_ex[low+2])
print(list_ex[high-low])
print(list_ex[low-high])
print(list_ex[-1])
print(list_ex[-low])
print(list_ex[2*3])
print(list_ex[2]*3)
print(list_ex[5%4])
print(len(list_ex))

'5.7'
n_list=[10,20,30,50,60]
s=0
for i in n_list:
    s+=i
print(s)

'5.9'
n_list=[10,20,30,50,60]
m=0
for i in range(0,5):
    if m<n_list[i]:
        m=n_list[i]
print(m)

'5.11'
n_list=list(map(int,input('5개의 수를 입력하세요 : ').split()))
print('합 :',sum(n_list))
print('평균 :',sum(n_list)/len(n_list))
print('최댓값 :',max(n_list))
print('최솟값 :',min(n_list))

'5.13'
n_list=list(map(int,input('10개의 수를 입력하세요 : ').split()))
print('합 :',sum(n_list))
print('평균 :',sum(n_list)/len(n_list))

'5.15'
greet='Have a beautiful day.'
greet[0:4]
greet[7:16]
greet[17:20]

'5.17'
animals=['dog','cat','tiger','lion']
print(animals[1:4]+animals[:-3])
for m in animals:
    print('I love',m)
