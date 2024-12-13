with open('./output/data.bin','wb') as f:
    txt='안녕'
    f.write(txt.encode())

with open('./output/data.bin','rb') as f2:
    data2=f2.read()
    print(data2)
    print(data2.decode())
#############################################
with open('./output/capture.jpg','rb') as f3:
    img=f3.read()

with open('./output/capture2.jpg','wb') as f4:
    f4.write(img)
#############################################
try:
    num=int(input('정수입력: '))
except ValueError:
    print('정수를 입력하세요.')


try:
    num=int(input('정수입력: '))
except ValueError as msg:
    print(msg)


try:
    num=int(input('정수입력: '))
except:
    print('정수를 입력하세요.')


try:
    num=int(input('정수입력: '))
except Exception as msg:
    print(msg)


try:
    num=int(input('정수입력: '))
except ValueError as msg:
    print('정수를 입력하세요.',msg)
except Exception as msg:
    print(msg)
else:
    print('예외 없음')
#############################################
def a():
    try:
        b=int(input('숫자 입력: '))
        print('정수 입력 성공:',b)
    except ValueError:
        print('정수가 아님! 정수를 입력해주세요!')
        a()
    finally:
        print('반드시 실행되는 것')
a()
#############################################
a=1
try:
    a+=1
    raise NotImplementedError
    a+=2
    print("a",a)
except:
    print('error',a)


class Animal:
    def breath(self):
        print('숨쉰다.')
    def cry(self):
        raise NotImplementedError


class dog(Animal):
    def cry(self):
        print('멍멍')


Dog=dog()
Dog.cry()
#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

#############################################

