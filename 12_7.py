l=['s','s','s','s','s','s']

print(''.join(l))
#############################################
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    answer.sort()
            
    if len(answer)==0:
        answer.append(-1)
    return answer

print(solution([5,9,7,10],5))
print(solution([2,36,1,3],1))
print(solution([3,2,6],10))
#############################################
def solution(numbers):
    answer = []
    set_a=set()
    for i in range(len(numbers)-1): #0 1 2
        for j in range(1, len(numbers)-i):
            set_a.add(numbers[i]+numbers[j+i])
    answer=list(set_a)
    return answer


print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))
#############################################
def solution(x):
    answer = True
    k=list(str(x))
    a=0
    for i in range(len(k)):
        a+=int(k[i])
    if x%a!=0:
        answer=False
    return answer

print(solution(13))
#############################################
def solution(s):
    answer = ''
    a=list(s)
    a.reverse()
    answer=''.join(a)
    return answer


print(solution('Ddsfw'))
#############################################
def solution(name, yearning, photo):
    answer = []
    yearn=dict(zip(name, yearning))
    print(yearn['may'])
    print(len(photo[:]))

    for i in range(len(photo[:])):
        score=0
        for j in range(len(photo[i][:])):
            if photo[i][j] in name:
                score+=yearn[photo[i][j]]
        answer.append(score)
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
#############################################
def solution(numlist, n):
    numlist_s=numlist.copy()
    answer = []
    for i in range(len(numlist)):
        numlist[i]-=n
        numlist[i]=abs(numlist[i])

    numlist.sort()
    #print(numlist)

    for i in range(len(numlist)):
        numlist[i]+=n
    for i in range(len(numlist)):
        if numlist[i] in numlist_s and numlist[i-1]!=numlist[i]:
            answer.append(numlist[i])
        else:
            answer.append(2*n-numlist[i])

    return answer


print(solution([1,2,3,4,5,6],4))
print(solution([10000,20,36,47,40,6,10,7000],30))
#############################################
def solution(t, p):
    answer = 0
    k=len(p)
    p=int(p)

    for i in range(len(t)-k+1):
        if int(t[i:k+i])<=p:
            answer+=1
    return answer
#############################################
answer = []

def solution(n):
    if n==1:
        answer.append(n)

    elif n%2==0:
        answer.append(n)
        n=n//2
        solution(n)

    else:
        answer.append(n)
        n=3*n+1
        solution(n)
    return answer

print(solution(100))
#############################################

#############################################

#############################################

#############################################


