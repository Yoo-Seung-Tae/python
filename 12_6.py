def a(x='default', y=1):
    for i in range(y):
        print(x, end=' ')

a('test',10)
a()
#############################################

def cal(*numbers):
    print(type(numbers))
    return sum(numbers)/len(numbers)

print(cal(1,2))
print(cal(1,2,3,4,5))

def a():
    return 1, 2

print(type(a()))

def b(**x):
    print(type(x))
    for k, v in x.items():
        print(f'{k}: {v}')
    for i in x:
        print(f'{i}')
b(name='Alice', age=25, city='new jersy')
#############################################
a=[1,2,3,4,2,6,3,5,3,5]

a.sort()

a1=[1,2,3,4,2,6,3,5,3,5]
print(a)

print(sorted(a1))
print(a1)

print("1+2")
print(eval('1+2')) 
#############################################
#round
print(int(4.6+0.5))
print(int(4.4+0.5))

print(int(4.5+0.5))
print(round(4.5,1))
#############################################
a=0

def hello():
    global a
    a+=1
    print(a)
    while a<=3:
        print('hello world!')
        hello()

print(a,"s")
hello()
print(a,"s")
#############################################
c=[1,1]
n=0
print(c)

def fibo(x):
    global c
    for i in range(x-2):
        n=c[i]+c[i+1]
        c.append(n)

fibo(10)
print(c)
#############################################
c=0
def fibo(n):
    global c
    if n<=2:
        c+=1
        return 1
    else:
        c+=n-1
        return fibo(n-1)

fibo(100)
print(c)
#############################################
#memorization
memory = {1: 1, 2: 1}

def fibo_memoization(n):
    if n in memory:
        number = memory[n]
    else:
        number = fibo_memoization(n-1) + fibo_memoization(n-2)
        memory[n] = number
    return number


fibo_memoization(10)
print(memory)
#############################################
add=lambda x,y:x+y

print(type(add))
print(add(1,2))

def add2(x,y):
    return x+y

print(add2(1,2))

# 람다식 사용
def call_1(func):
    for i in range(3):
        func()

call_1(lambda:print('hi'))

def download(startedcallback, endedcallback):
    startedcallback()
    endedcallback()

download(lambda:print('시작'), lambda:print('완료되었습니다.'))
#############################################
list(map(int, ['1', '2', '3']))

result=map(lambda x:x*3,[1,2,3,4])
print(list(result))


li=[-5, 1, 2, -11, 76]

value=list(filter(lambda x:x<0, li))
print(value)



value2=list(filter(lambda x:x>3, map(lambda x:x*2,li)))
print(value2)
#############################################

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i]>=50 and arr[i]%2==0:
            answer.append(arr[i]/2)
        elif arr[i]%2==1 and arr[i]<50:
            answer.append(arr[i]*2)
        else:
            answer.append(arr[i])

    return answer

solution([1,2,3,100,99,98])
#############################################
def solution(myString):
    answer = []
    sp=myString.split('x')

    for i in range(len(sp)):
        answer.append(len(sp[i]))
    return answer


solution("oxooxoxxox")
solution("xabcxdefxghi")
#############################################
def solution(str1, str2):
    answer = 0
    for i in range(len(str2)-len(str1)+1):
        if str1==str2[i:i+len(str1)]:
            answer+=1
        if answer==1:
            break
    return answer


print(solution("abc","aabcc"))
print(solution("tbt", "tbbttb"))
#############################################
def solution(t, p):
    answer = 0
    k=len(p)
    p=int(p)

    for i in range(len(t)-k+1):
        if int(t[i:k+i])<=p:
            answer+=1
    return answer

print(solution("3141592","271"))
print(solution("500220839878"	, "7"))
print(solution("10203", "15"))
#############################################

#############################################

