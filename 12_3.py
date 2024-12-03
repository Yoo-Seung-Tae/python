i=1

while i<10:
    print(i)
    i+=2

print('끝')


#############################################
# 실습1
i=int(input('숫자 입력: '))
a=0

for i in range(i+1):
    a+=i

print(a)


# 번외(홀수 합)
i=int(input('숫자 입력: '))
a=0

for i in range(1, i+1, 2):
    a+=i

print(a)


#############################################

a=int(input('몇 초?: '))

for i in range(a,0,-1):
    print(i, end=' ')

print('발사!!')


a=list(range(0,10,1))
b=list(range(10,0,-1))
print(a)
print(b)
#############################################

# 실습3
a=int(input('몇 단을 출력할까요? '))

for i in range(1, 10):
    print(f'{a} * {i} = {i*a}')


#############################################
a=[1,2,3,4,5]
a3=[i*3 for i in a]
a4=[i*3 for i in a if i%2==0]

print(a3)
print(a4)

for i in range (2, 10):
    print(f'[{i}단]')
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print()

#############################################
row=int(input('행 수 입력: '))
cus=int(input('고객 수 입력: '))

if cus%row == 0:
    col=cus//row
else:
    col=cus//row+1

a=0
for i in range(row):
    for j in range(col):
        a+=1
        if(a>cus):
            break
        print(a, end=' ')
    print()
#############################################

# 1번
a=int(input('몇 줄? '))
for i in range(1,a+1):
    for j in range(i):
        print('*', end=' ')
    print()

# 2번
b=int(input('몇 줄? '))
for i in range(1, b+1):
    for j in range(b, 0,-1):
        if j>i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    
    print()


# 3번
c=int(input('몇 줄? '))

for i in range(1, c+1):
    print(" " * (c-i) + "*"*(2*i-1))
#############################################


#############################################


#############################################


#############################################


#############################################
