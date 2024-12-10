class supermarket:
    count=0
    def __init__(self, location, name, product, customer):
        self.__location=location
        self.__name=name
        self.__product=product
        self.__customer=customer
        supermarket.count+=1

    def print_location(self):
        print(self.__location)

    def change_category(self, product):
        self.__product=product

    def show_list(self):
        print(self.__product)

    def enter_customer(self):
        self.__customer+=1

    def show_info(self):
        print(self.__name)
        print(self.__location)
        print(self.__product)
        print(self.__customer)

    def show_supermarket_count(self):
        print(supermarket.count)

a=supermarket('lo_aa','na_aa','pr_aa',6)
b=supermarket('lo_bb','na_bb','pr_b',10)

a.print_location()
a.change_category('pr_bb')
a.change_category('pr_cc')

a.show_list()
a.enter_customer()
a.enter_customer()
a.show_supermarket_count()

a.change_category('bb')
a.show_info()

print(supermarket.count)
# print(a.location)
#############################################
class country:
    def __init__(self):
        self.name='나라이름'
        self.population='인구'
        self.capital='수도'

    def show(self):
        print('국가 클래스의 메소드')

class korea(country):
    def __init__(self, name):
        self.name=name

    def show(self):
        print('국가 이름: ', self.name)

country=korea('대한민국')
country.show()
print(country.name)
country.show()
#############################################
class Calculator:
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value

class MinLimitCalculator(Calculator):
    def sub(self, value):
        self.value -= value
        self.value = max(0, self.value)

#        if self.value<0:
#            self.value=0

cal=MinLimitCalculator()

cal.sub(20)
cal.sub(30)
cal.sub(10)

print(cal.value)
#############################################
import calc_module
from calc_module import add
import calc_module as cm

print(calc_module.add(2,3))
print(calc_module.sub(2,3))
print(calc_module.mul(2,3))
print(calc_module.div(2,3))

print(cm.add(223,4))
#############################################
import math

print(math.floor(4.22))
print(math.ceil(1.22))
print(math.sqrt(3))

from math import floor, ceil
print(floor(5.11))
print(ceil(3.122))

import random
print(random.randint(1,100))
print(random.uniform(1,100))
print(random.random())
print(random.randrange(1,6,2))
#############################################
import random

num=random.randint(1,100)
score=100
count=1
mi=0
ma=100
a=int(input('숫자를 입력하시오.: '))

while num!=a and score!=0:
    try:
        if num>a:
            mi=max(mi, a)
            a=int(input(f'랜덤수 보다 작습니다. [{count}]회 {mi}~{ma}, 다시 입력하세요.'))
        else:
            ma=min(ma, a)
            a=int(input(f'랜덤수 보다 큽니다.  [{count}]회 {mi}~{ma}, 다시 입력하세요.'))
        score-=10
        print(score)
        count+=1

    except ValueError:
        print('숫자만 입력 가능합니다.')

if score==0:
    print(f'패배입니다. 점수: {score}')

else:
    print(f'정답입니다. 점수: {score}')
#############################################
import random

a=set()

while len(a)!=6:
    num=random.randint(1,46)
    a.add(num)

a=list(a)
a.sort()
print(a)
#############################################
lotto = random.sample(range(1,46), 6)
print(sorted(lotto))
#############################################
import datetime

now=datetime.datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)


age=int(input('나이 입력: '))
result=now.year+100-age
print(f'100세가 되는 해는 {result}년 입니다.')
#############################################
import datetime

today=datetime.date.today()

print('지금까지 며칠이 지났는가')
first_day=datetime.date(2024,11,25)
passed_time=today-first_day
print(passed_time)
#############################################

#############################################


