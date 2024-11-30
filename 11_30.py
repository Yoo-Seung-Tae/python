import pandas as pd


num=1000
a=pd.DataFrame([num,2])
#print(a)
#############################################
print(type(77))
print(type('s\'s'))
print(type("s"))
print(type(7.2))

a1=77
a2=7.2
print(type(a1+a2-0.2))
print(a1+a2-0.2)

#이스케이프 문자#############################################
print('s\'s')
print('111\t1111')

#print("'집가고싶다.'")
#print('"집가고싶다."')
#############################################
num=10
num_b=0b1010
num_x=0xA

print(num, num_b, num_x)

print(bin(10))
print(hex(10))

#ASCII문자 값#############################################
print(ord('0'))
print(ord('A'))
print(chr(48))
print(chr(65))

#print(not 1!=1)

print(211.5//3)
print(211%3)
print(2**2)

print(1+2*-3**2)

#############################################
print('빵의 개수 :',30//4)
print('남은 빵의 개수 :', 30%4)

#############################################
a=1
a+=2
print(a)

print("1"*10)

for i in [1,2,3,4,5]:
    print("럭키", i, end="", sep="")

print()

#입력 받기#############################################
song=input("노래: ")
print(song)
print(type(song))

print(int(song)+2)

k=int(input("숫자: "))
print(k+2)


c=str(2)
print(c*10)
print(c, "입니다.")
#############################################
print('|\\_/|')
print('|q p|\t/}')
print('( 0 )"""\\')
print('|"^"`\t |')
print('||_/=\\\\__|')

# 1번#############################################
name1=input('이름을 입력하세요. ')
age=input('나이를 입력하세요. ')
print(f'안녕하세요! {name1}님 ({age}세)')
print()

# 2번#############################################
name2=input('이름을 입력하세요. ')
birth_year=int(input('태어난 연도를 입력하세요. '))
year=int(input('올해 연도를 입력하세요. '))
print(f'올해는 {year}년, {name2}님의 나이는 {year-birth_year}세 입니다.')
#############################################
a=['s', 1]
print(a)
print(type(a))
print(type(a[0]))
print(type(a[1]))

a=['s', 1]
print(a)
print(type(a))
print(type(a[0]))
print(type(a[1]))


a[0]="카리나"
print(a)
print(len(a))

del a[1]
print(a)
a.append("장원영")
a.append("안유진")
print(a)
#############################################
seasons=['봄', '여름', '가을', '겨울']

print(seasons[:len(seasons)])
print(seasons[0:1])
print(seasons[1:3])
print(seasons[1:])

print(seasons[1::2])

print(seasons[3:1:-1])

print(seasons[0:2:-2])
#############################################

seasons2=['봄', '여름', '가을', '겨울',[1,2,3,4]]
print(seasons2[4].append(2))
print(seasons2)
#############################################

seasons=['봄', '여름', '가을', '겨울']

print(seasons[::-2])

print(seasons[:len(seasons)])
print(seasons[0:1])
print(seasons[1:3])
print(seasons[1:])

print(seasons[1::2])

print(seasons[3:1:-1])

#############################################

a=[1,2,3,4,5,6,7,8,9,10]
even=a[1::2]
print(even)
#############################################
a=[1,5,3,8,4,5,7]

a.sort()
a.reverse()
print(a)

b=["a",'h','e','y']
b.sort()
print(b)

#############################################
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# 1번
print(rainbow[2])
print(type(rainbow[2]))

# 2번
rainbow.sort()
print(rainbow)

# 3번
rainbow.append('blue')
print(rainbow)

# 4번
del rainbow[3:7]
print(rainbow)

print(rainbow.index('green'))
rainbow.pop()
print(rainbow)

#pop맨 마지막 것 삭제 append는 상극
#sort는 정렬, reverse는 상극
#insert 원하는곳에 하나 넣기
#del은 여러개 구간지정해서 여러개 삭제
#remove는 첫번째 한개 삭제
#index는 첫번째 것 위치 출력