a=[1,2,3,4]
b=[1,2,3,4]
a[0]+=b[0]
print(a)

###################################################################3

num=5
print("이번에 %.23f권의 책을 %d 샀다." %(num,2))
print(f"이번에 {num}권의 책을 샀다.")
print("이번에 {0}가 {1}권의 책을{1} 샀다.".format("yoo",num))
print("My name is {1}".format('yoo', 'seung', 'tae'))

###################################################################3

k='n dd'

print(k[0], k[1], k[2])

print('dd',2, sep='')

###################################################################3

a='apple'

print(a.upper())
print(a.lower())

###################################################################3

stri='dd 코딩온, 안녕하세요 코딩온입니다.'

print(stri.find('코딩온'))
print(stri.rfind('코딩온'))

###################################################################3
friends="고찬국 김다운 김민창"
a=friends.split(" ")
print(a)

###################################################################3

a="       d e g        r r r r r r     "
print(a)
print(a.strip())
print(a.lstrip())

###################################################################3
a='hello, python.'
print(a.replace('python','c++'))
###################################################################3

a=int(input()) #472
b=int(input()) #385


b=str(b)

sol_3=int(b[2])*a
sol_4=int(b[1])*a
sol_5=int(b[0])*a

sol_6=int(b)*a

print(sol_3, sol_4, sol_5, sol_6,sep='\n')
###################################################################3

a=range(10)

b=str(473)
print(len(b))

for i in range(len(b)):
    print(i)
###################################################################3
a=[1,2,3,4]
print(list(map(str,a)))
print(list(map(int, input().split())))

def b(a):
    c=a+1
    return c
print(type(a))
print(list(map(b,a)))

###################################################################3
print(bool(' '))
print(1==2)
print(1==1 and 1==2)

print(not True)

cart = ['두부','계란','마늘','콩나물']

print('두부' in cart)
print('커피' in cart)

###################################################################3
if False:
    print(1+1)

elif True:
    print(1+2)

elif True:
    print(1+4)

else:
    print(1+3)

a=int(input())

if a%2==1:
    print("홀수")
if a%2==0:
    print("짝수")


###################################################################3

num=3
def plus(a):
    c=a+num
    return c

print(plus(1))

###################################################################3
# >=는 두번 비교, >는 한번만 비교한다
a=int(input())

if a>=90:
    print('A')
elif a>=80:
    print('B')
elif a>=70:
    print('C')
elif a>=60:
    print('D')
else:
    print('E')

###################################################################3
#print를 너무 많이 썼음. 중복을 줄이자
a=int(input("나이 입력 : "))
b=input("결재 방법(카드/현금): ")

if b!='현금' and b!='카드':
    print("입력 오류")
elif a<8:
    print("무료")
elif a<14:
    print('450원')
elif a<20:
    if(b=='카드'):
        print("720원")
    elif(b=='현금'):
        print("1,000원")
elif a<75:
    if(b=='카드'):
        print("1,200원")
    elif(b=='현금'):
        print("1,300원")
else:
    print('무료')

###################################################################3
# 과제 1
a=[]
b=int(input('숫자 입력: '))

for i in range(b):
    a.append(i+1)

print(a)

# 과제 2
vending_machine=['게토레이', '레쓰비', '생수', '이프로']

print('=================RESTART')
a=input('마시고 싶은 음료? ')

if a in vending_machine:
    print(f'{a} 드릴께요')
else:
    print(f'{a}는 지금 없네요')


###################################################################3

# 과제 3
vending_machine=['게토레이', '게토레이', '레쓰비','레쓰비', '생수','생수','생수', '이프로']
who=int(input('사용권한 입력(1: 소비자 or 2: 주인): '))

if who != 1 and who != 2:
    print("잘못 입력하셨습니다.")

elif who == 1:
    drink=input("음료를 입력하시오: ")
    if drink in vending_machine:
        print(f'{drink} 드릴께요')
        vending_machine.remove(drink)

    else:
        print(f'{drink}는 지금 없네요')

else:
    work=int(input("작업을 입력하시오(1: 추가, 2: 삭제): "))
    if work != 1 and work != 2:
        print("잘못 입력하셨습니다.")

    elif work == 1:
        a=input("추가 사항 입력: ")
        vending_machine.append(a)
        vending_machine.sort()
        print("추가 완료")

    else:
        a=input("삭제 사항 입력: ")
        if a in vending_machine:
            vending_machine.remove(a)
            print("삭제 완료")
        else:
            print(f'{a}는 없습니다')
        
print("음료 현황:", vending_machine)
###################################################################3
a=list(range(10))

print(type(a))
print(a)

import numpy as np
b=np.array(range(5))

print(b)
