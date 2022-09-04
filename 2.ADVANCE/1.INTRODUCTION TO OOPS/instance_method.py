
##Instance method==
# class Car:
#     def __init__(self,nm,yr):
#         self.modle_name=nm         ## instance varibles(inside constructor by using self variable)
#         self.year=yr
#
#     def details(self,n,y):
#         self.mode_name=n          ## inside static method by using self
#         self.yer=y
#         print(self.mode_name)
#         print(self.yer)
#
# Toyota=Car("Etios",2016)
# print(Toyota.year,Toyota.modle_name)
#
# Tata=Car("Nano",2011)
# print(Tata.year,Tata.modle_name)
#
# Fiat=Car("jEEP",1998)
# print(Fiat.year,Fiat.modle_name)
#
# # Toyota.details()
# Toyota.details("truck",2022)
#



class A:

    def __init__(self,a,b):
        self.distance=a
        self.time=b
        self.velo = (a / b)
    def vel(self,s):
        self.speed=s         ## inside instance method by using self keyword
        print(f" the velocity is: {self.velo} and speed is {self.speed} ")

s1=A(100,5)             ## first object
s1.vel(200)
s1.acc=4                ## by using obj referrence variable outside of the class
print(s1.__dict__)

s2=A(500,10)           ## Second obj
s2.vel(300)
print(s2.__dict__)
print(s1.speed,s1.distance)    ## Accessing the instance var outside of class by using obj ref var

# delete instance var
del s1.time
print(s1.__dict__)