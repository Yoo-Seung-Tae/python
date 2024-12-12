# n=1

# with open('./output/member.txt','w') as f:
#     while n<=3:
#         text=input(f'이름 입력({n})번째: ')
#         f.write(text+' ')
#         text=input(f'비번 입력({n})번째: ')
#         f.write(text+'\n')
#         n+=1

# with open('./output/member.txt','r') as f:
#     a=input('이름을 입력하시오.: ')
#     info = f.read().split()
#     c=0
#     for i in range(3):
#         if a==info[2*i]:
#             b=input('비밀번호를 입력하시오.: ')
#             if b==info[2*i+1]:
#                 print('로그인 성공')
#                 c+=1
#     if c==0:
#         print('로그인 실패')

n=0
with open('./output/member.txt','r') as f:
    a=input('이름을 입력하시오.: ')
    b=input('비밀번호를 입력하시오.: ')
    info = f.read().split()
    if a in info and info.index(a)%2==0:
        if b==info[info.index(a)+1]:
            print('로그인 성공')
            n+=1
        else:
            print('로그인 실패')
    else:
        print('로그인 실패')

if n==1:

    c=input('전화번호를 입력하시요.: ')


    with open("./output/member_tel.txt", 'r') as f:
        g=f.read()
        if a in g.split():
            for line in f:
                n, p = line.split()
            t={}
            t[n]=p
            print(t)
            f[a] = c
        else:
            f[a]=c


    with open("./output/member_tel.txt", 'w') as f:
        e=str(f)
        print(e)
        f.write(e)



















