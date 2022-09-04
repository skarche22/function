#1.  Instance variables(Object Level Variables)
# for every object seperate copy of instance variables will be created
# A]]==DECLARATION`===
# 1] INSIDE CONSTRUCTOR BY USING SELF KEYWORD`
class Employee:
    def __init__(self):
        self.eno=100
        self.ename="sk"
        self.esal=1000000

e=Employee()   
print(e.__dict__)     


# 2] INSIDE INSTANCE METHOD BY USING SELF KEYWORD`
class Test:
    def __init__(self):
        self.a=100
        self.b=200

    def m1(self):
        self.c=300

x=Test()   
x.m1()
print(x.__dict__)

# 3] Outside of class using Object reference variable
class Test:
    def __init__(self):
        self.a=100
        self.b=200

    def m1(self):
        self.c=300

x=Test()   
x.m1()
x.d=400
print(x.__dict__)


# B]] Access the Instance Variable==Within class by using self variable and outside of class by using obj ref var

class Test:
    def __init__(self):
        self.a=100
        self.b=200

    def m1(self):
        print(self.a)
        print(self.b)
x=Test()   
x.m1()
print(x.a,x.b)

## C]] Delete instance variable from the obj==
# a]] within the class ==   del self.variableName
# b]] outside the class==   del objectreferance.variableName

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self): 
        del self.c

q=Test()
q.m1()
del q.b
print(q.__dict__)

# NOTE== the insatance variable which is deleted from one object, will not be delete from another obj
## change values of instance var of one obj then those changes wont be reflected to anoter obj
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self): 
        del self.c

q=Test()
q.m1()
del q.b
print(q.__dict__)