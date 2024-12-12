#############################################
f4=open('test.txt')
print(f4.readlines())
f4.close()
#############################################
f5 = open('./test.txt','r+')
print(f5.read())

print(f5.tell())
f5.seek(0)
print(f5.read())

f5.seek(4)
print(f5.read())

print(f5.write("8"))
f5.close()
#############################################
f6 = open('./test.txt','r+')
str6=f6.read()
print(f6.tell())
f6.seek(str6.find('o'))
print(f6.write('8'))
f6.close()
#############################################
with open('./test.txt','r+') as f7:
    str6=f7.read()
    print(f7.tell())
    f7.seek(str6.find('o'))
    print(f7.write('8'))
#############################################
with open('./word.txt','w') as f8:
    word=['sky','earth','water','fire','air']
    for i in word:
        f8.write(i+' ')

with open('./word.txt','r') as f:
    data=f.read().split()
    word=random.choice(data)
    print(word)
#############################################
import random
import time
import sys
import os

# if os.path.exists('word.txt'):
#     with open("word.txt", 'r') as f:
#         # 전역변수
#         word = f.read().split()


try:
    with open("word.txt", 'r') as f:
        # 전역변수
        word = f.read().split()

except:
    print('파일이 없습니다.')
    sys.exit(0)

word2=word.copy()
n=0

input('[타자 게임] 준비되면 엔터!')
start=time.time()

while n<len(word): 
    ques=random.choice(word2)  
    print(ques, end='')
    ans=input(' ->')
    if ans==ques:
        word2.remove(ques)
        n+=1

end=time.time()

print(f'걸린시간: {end-start}초')
#############################################
n=1

with open('./output/member.txt','w') as f:
    while n<=3:
        text=input(f'이름 입력({n})번째: ')
        f.write(f'순번 {n} 이름: {text} ')
        text=input(f'비번 입력({n})번째: ')
        f.write(f'비밀번호: {text} \n')
        n+=1

with open('./output/member.txt','r') as f:
    print(f.read())
#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

