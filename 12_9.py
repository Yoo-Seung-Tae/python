a=dict()
b=set()

class b():
    pass

c=b()

class Movie:
    title='aa'

mov1=Movie()
mov2=Movie()
mov3=Movie()

print(mov1.title)
print(mov2.title)


mov1.title='bb'
print(mov1.title)
print(mov2.title)


mov1.score=1
print(mov1.score)
#print(mov2.score)
#############################################
class Movie:
    name=' '
    def print_msg(msg):
        print(msg)
    def modify(self, movie):
        self.name=movie
    def print_name(self):
        print(self.name)

movie1=Movie()
movie2=Movie()

Movie.print_msg('Print하기')
#Movie.modify(movie1, 'Print하기')
movie1.modify("프린트하기")
movie1.print_name()
movie2.modify('프린트하기')
print('movie2.name', movie2.name)
#############################################
class Movie:
    def __init__(self):
        print('hello')

movie=Movie()
#############################################
class Movie:
    count=0

    def __init__(self, title, audience):
        self.title=title
        self.audience=audience

movie1=Movie('파묘',100)
movie2=Movie('파묘2',200)

print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)
#############################################
class Movie:
    count=0

    def __init__(self, title, audience):
        self.title=title
        self.audience=audience
        Movie.count+=1

movie1=Movie('파묘',100)
print(Movie.count)
movie2=Movie('파묘2',200)

print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count+=1
print(movie1.count)
print(movie2.count)
print(Movie.count)
#############################################
class Movie:
    count=0

    def __init__(self, title, audience):
        self.title=title
        self.audience=audience
        Movie.count+=1

    def get_title(self):
        return self.__title
    

    def set_title(self, title):
        self.__title=title

    def get_audience(self):
        return self.get_audience


movie1=Movie('파묘', 100)
#print(movie1.get_title())
movie1.__title='오겜'

print(movie1.get_title())
print(movie1.get_audience())
#############################################
class MyAdd:
    __a = 1
    __b = 2

    def sum(self):
        return self.__a+self.__b

#    def get_a(self):
#        return self.__a
    
    def set_a(self, a):
        self.__a=a




a = MyAdd()
print(a.sum()) # 3

a.set_a(3)
print(a.sum()) # 5
#############################################
class Health:
    def __init__(self,name):
        self.__name=name
        self.__hp=100


    def get_name(self):
        return self.__name
    
    def set_hp(self, hp):
        hp=max(hp,0)
        hp=min(hp,100)
        self.__hp=hp
    
    def get_hp(self):
        return "hp: " + str(self.__hp)
    
    def exercise(self, hours):
        self.set_hp(self.__hp+hours)
        print("{}시간 운동하다.".format(hours))

    def drink(self, cups):
        self.set_hp(self.__hp-cups)
        print("술을 {}잔 마시다.".format(cups))


ad=Health('aaaa')
ad.set_hp(50)
print(ad.get_hp())
print(ad.get_name())
ad.drink(10)
#############################################
class cal:
    def __init__(self,a, b):
        self.__a=a
        self.__b=b

    def add(self):
        return self.__a+self.__b
    def sub(self):
        return self.__a-self.__b
    def mul(self):
        return self.__a*self.__b
    def div(self):
        if self.__b==0:
            return None
        else:
            return self.__a/self.__b
    
a=cal(4,0)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

a=[print(a.add()),print(a.sub())]
#############################################
class Employee:
    num=1000

    def __init__(self, name):
        Employee.num+=1
        self.id=Employee.num
        self.name=name

    def __str__(self):
        return f'사번 : {self.id}, 이름: {self.name}'
    
e1=Employee('최사원')
print(e1)

e2=Employee('최사원')
print(e2)

e3=Employee('박사원')
print(e3)

employee=[Employee('구름'),Employee('별'),Employee('행성'),Employee('달')]
print(employee[0])
print(employee[1])
#############################################


