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