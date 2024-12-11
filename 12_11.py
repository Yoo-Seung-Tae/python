import calendar

# calendar.prcal(2024)
# calendar.prmonth(2024,11)
# print(calendar.weekday(2024,11,10))

import datetime

a=['월', '화', '수', '목', '금', '토', '일']

weekday=datetime.date.today().weekday()
print(f'오늘은 {a[weekday]}요일 입니다.')

day=datetime.date(2024, 12, 25).weekday()
print(f'크리스마스는 {a[day]}요일 입니다.')
#############################################
import time

a=time.time()
time.sleep(2)
b=time.time()

print(time.localtime())

time_str=time.localtime()
print(time_str.tm_year)

print(time.ctime())
print(time.ctime(a))
print(time.ctime(b))
#1970. 1. 1. 기준
year=round(time.time()/(365*24*60*60))
day=round(time.time()/(24*60*60))
print(year)
print(day)
#############################################
import time

def a():
    for i in range(5):
        time.sleep(1)
        print(i)

def check_time(func):
    start=time.time()
    func()
    end=time.time()
    print(end-start)

check_time(a)
#############################################
import sys

args=sys.argv[1:]
sum=0

for i in args:
    sum+=int(i)

print(sum)
#############################################
import sys

args=sys.argv[1:]

if len(args)!=3:
    sys.exit(0)

if args[0]=='mul':
    print(int(args[1])*int(args[2]))
elif args[0]=='add':
    print(int(args[1])+int(args[2]))
else:
    print('입력오류')
#############################################
import os

os.chdir('c:/Users/Administrator/python')

dir =os.popen('git status')
print('------------------------------------------------------------')
print(dir.read())
print('------------------------------------------------------------')
print(os.listdir())
print('------------------------------------------------------------')
dir =os.popen('dir')
print(os.listdir())
print('------------------------------------------------------------')

#############################################
import random
import time

word1=['sky','earth','water','fire','air']
word2=word1.copy()
n=0

input('[타자 게임] 준비되면 엔터!')
start=time.time()

while n<len(word1): 
    ques=random.choice(word2)  
    print(ques, end='')
    ans=input(' ->')
    if ans==ques:
        word2.remove(ques)
        n+=1

end=time.time()

print(f'걸린시간: {end-start}초')
#############################################
from modules.mylib import food
print(food.name)
food.cook()
food.eat()

from modules.mylib.food import cook
cook()

#from bbb import b
import bbb.b as b
b.bbb()
b.add(3,5)
#############################################

#############################################

#############################################

#############################################