import pandas as pd


num=1000
a=pd.DataFrame([num,2])
#print(a)

print(type(77))
print(type('s\'s'))
print(type("s"))
print(type(7.2))

a1=77
a2=7.2
print(type(a1+a2-0.2))
print(a1+a2-0.2)

#이스케이프 문자
print('s\'s')
print('111\t1111')

#print("'집가고싶다.'")
#print('"집가고싶다."')

num=10
num_b=0b1010
num_x=0xA

print(num, num_b, num_x)

print(bin(10))
print(hex(10))

#ASCII문자 값
print(ord('0'))
print(ord('A'))
print(chr(48))
print(chr(65))

#print(not 1!=1)

print(211.5//3)
print(211%3)
print(2**2)

print(1+2*-3**2)


print('빵의 개수 :',30//4)
print('남은 빵의 개수 :', 30%4)


