a=input('숫자입력(숫자간 space바 입력, 3개 이상 입력): ')

data=a.split()
data = list(map(int, data))

print('가장 큰 수: ', max(data))
print('가장 작은 수: ', min(data))
data.remove(max(data))
data.remove(min(data))

print('평균 값: ',(sum(data)/len(data)))


#c=list(map(int, input().split))

a = list(i for i in range(5))
print(a)
b = [i for i in range(5)]
print(b)
c = list(map(int, ["1","2","3"]))
print(c)
c = list(map(int, input().split()))
e = list(map(str, (1,2,3)))
print(e)
d = [i for i in map(int, ["1","2","3"])]
print(d)