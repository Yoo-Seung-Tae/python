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
import sys

def successLogin(name, pw):
    dictUser = {}
    with open("member.txt", 'r') as f:
        for line in f:
            n, p = line.split()
            dictUser[n] = p

    print(dictUser)

    return pw == dictUser.get(name)
    
name = input("이름을 입력하세요: ")
pw = input("비밀번호를 입력하세요: ")
    
if not successLogin(name, pw):
    print("로그인 실패")
    sys.exit(0)

print("로그인 성공")
phone = input("전화번호를 입력하세요.: ")

with open("member_tel.txt", "r") as f:
    m_tel_list = f.readlines()
    print(m_tel_list)

user_tel = name + " " + phone + "\n"

with open("member_tel.txt", "w") as f:
    write = False
    for i in m_tel_list:
        if i.split()[0] == name:
            f.write(user_tel)
            write = True
        else :
            f.write(i)
    if not write:
        print("not write", user_tel)
        f.write(user_tel)
#############################################



