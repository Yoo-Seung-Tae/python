#tuple
a=(10,20,30)

print(a)
print(a[1])
print(type(a))

b=(10)
c=10,
d=10, 20
print(b, c, d)

num, num2 = 1, 2
a=(num, num2)
print(a)
#############################################
#set
a=[1,2,3,4,4,5]
a=list(set(a))
print(type(a))
print(a)

set1={1,2,3}
set2={2,3,4,4}

set2.add(12)
set2.pop()

print(set1, set2)

while len(set2)>0:
    a=set2.pop()
    print(1, a)

set3=set('apple')

print(set3)

while len(set3):
    a=set3.pop()
    print(a)

name=['1', '2', '3', '2']

for i in range(len(name)):
    if name.count(name[i]) > 1:
        print(name[i])



#############################################

name=['1', '2', '3', '2','3','1','4']
a=len(name)-1

for i in range(a):
    if name[i] in name[i+1:a]:
        name[i]=0
print(name)

while 0 in name:
    name.remove(0)

print(name)


#############################################
#dict
a={}
a=dict()

#set
b={1}

print(a)
a[1]=1
a['c']=3
print(type(a))
print(a)

print(a[1])


#del a[1]

print(a)

print(a.get('c'))
print(a.get('g'))

print(a.keys())
print(type(a.keys()))

print(list(a.keys()))

print(a.values())

print(3 not in a)

a.clear()
print(a)

#############################################
dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}

print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")

if word in dic:
    print(f'{word}: {dic[word]}')
else:
    print("정의된 단어가 없습니다.")

#############################################
data='5 11 baekjoononlinejudge startlink codeplus sundaycoding codingsh baekjoon codeplus codeminus startlink starlink sundaycoding codingsh codinghs sondaycoding startrink icerink'


data=list(input().split())

N=int(data[0])
M=int(data[1])
#data=data[2:]

#S=set()

S=set(data[0:N])
data_m=set(data[N:M+N])

sol=S&data_m
print(len(sol))

#############################################

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())
ans = 0
for _ in range(M):
    t = input()
    if t in S:
        ans+=1
print(ans)



#############################################

a=list(range(5))
print(a[0:4])

# 튜플은 읽기 전용 리스트
a=(10, 20, 30)
print(a)
del(a)

# 셋은 집합. 중복, 정렬 X, 리스트와 비슷한데 2개만 함수가 다름
a={1,2,3}
a.add()
a.clear()
'''
&: 교집합 |: 합집합 -: 차집합
'''

# 딕셔너리는 키가 있음
a={}
a=dict('키': '값')
'''
조회
a['키값']

키값찾는 함수
a.get('키')

키 값 출력(for문 사용 가능)
a.key()

값 출력
a.values()

값 지우기
a.clear()
'''

#############################################
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

print(N, M)
#############################################
score={}
score={'Alice':85, 'Bob':90,'Charlie':95}

score['David']=80
score['Alicd']=88
del(score['Bob'])

for i in score.keys():
    print(i, ":", score[i])
#############################################
d=[
    [10, 20],
    [30, 40],
    [50, 60]
]

print(d[1][1])

print(len(d))
print(len(d[0]))


for i in range(0, len(d)):
    for j in range(0, len(d[i])):
        print(d[i][j],end=' ')
    print()


for x, y in d:
    print(x, y)
#############################################
