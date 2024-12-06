a=[[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3]]
for x, y in a:
    print(f'{x} * {y} = {x*y}')

print(a)
a[2].append(20)
print(a)
print(a[2][2])

for i in a:
    print(f'{i[1]} * {i[0]} = {i[0]*i[1]}')
#############################################
def f(x):
    result=x**2+2*x+1
    return(result)

print(f(3))


def say_hello():
    print('hello world')
    print('hello world')
    print('hello world')

say_hello()

x=200
def ff():
    x=10
    print(x)

def fff():
    print(x)
    ff()

fff()
print(x)

def ffff(x):
    print(x)
ffff(3)
#############################################
def cal(x, y):
    if x==y:
        print(f'결과(곱): {x*y}')
    else:
        print(f'결과(합): {x+y}')

cal(3,4)
cal(5,5)
#############################################
def delivary(x, y):
    if x*y<20000:
        print(f'가격은 {x*y+2500}원 입니다.')
    else:
        print(f'가격은 {x*y}원 입니다.')

delivary(10000,1)
delivary(30000,3)
#############################################
def times(l):
    l2=[i*2 for i in l]
    return l2

v2=[1,2,3,4,5]
print(times(v2))


def sum_mul(a, b):
    sum = a+b
    mul = a*b
    return sum, mul
s, m= sum_mul(1,2)
#############################################
vending_machine=['게토레이', '게토레이', '레쓰비','레쓰비', '생수','생수','생수', '이프로']

def check_machine():
    print(vending_machine)

def is_drink(a):
    if a in vending_machine:
        print('음료가 있습니다.')
    else:
        print(f'{a}는 없습니다.')

def add_drink(a):
    vending_machine.append(a)
    vending_machine.sort()
    print("추가 완료")

def remove_drink(a):
    if a in vending_machine:
        vending_machine.remove(a)
        print("삭제 완료")
    else:
        print(f'{a}는 없습니다')

check_machine()
is_drink('게토레이')
print(vending_machine)
add_drink('토레타')
print(vending_machine)
remove_drink('생수')
print(vending_machine)
#############################################
import sys

line=sys.stdin.readline().strip()
#line2=input()

print(line)

if line == 'dddd':
    print("작동")
#############################################
import sys
line=sys.stdin.readline()
stack=[]

def push_X(a):
    stack.append(a)

def pop():
    if len(stack)!=0:
        print(stack.pop(),end='')
    else:
        print(-1)
    
def size():
    print(len(stack))

def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def top():
    if len(stack)!=0:
        print(stack[len(stack)-1], end='')
    else:
        print(-1)


if line[0:5] == 'push ':
    push_X(line[5:])
elif line[:] == 'size\n':
    size()
    print('1')
elif line[:] == 'empty\n':
    empty()
elif line[:] == 'pop\n':
    pop()
else:
    top()

match line:
    case 'size\n':
        size()
    case 'empty\n':
        empty()
    case 'pop\n':
        pop()
    case 'top\n':
        top()
    case _:
        push_X(line[5:])
#############################################
def oneUp():
    x=100
    y=x+1
    return y

x=0

print(oneUp())
print(oneUp())


#############################################
a=int(input('숫자 입력: '))
b=int(input('배수 입력: '))


def cal():
    global x
    for i in range(1,a//b+1):
        print(i*b,sep=' ')
        x+=1
    print(f'{b}의 배수의 개수: {x}')

x=0
cal()

#############################################




