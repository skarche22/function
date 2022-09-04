# # ## Find the correct age by using classmethod even input is wrong
#
# from datetime import date
# class Stud:
#     def __init__(self,nm,yr):
#         self.name=nm
#         self.age=yr
#     def details(self):                 ## Here input given in year and print as it is
#         print(f"the name of student is {self.name}, and age is {self.age}")
#
#
#     @classmethod                       ## Here input is same as above but op is as per developer
#     def input_details(cls,nm,age):     ## we developed cls method to correct op if user given iwrong ip
#         age=date.today().year-age
#         cls.name=nm
#         cls.age=age
#         return cls(nm,age)
#
#
# obj=Stud("Santosh",1992)
# obj.details()
#
# real=Stud.input_details("Santosh",1992)
# real.details()
#
#
#
# # ### We got independance from british
# # from datetime import date
# # class Freedom:
# #     def __init__(self,n,yr):
# #         self.year=yr
# #         self.nationality=n
# #     def independance(self):
# #         print(f"We are {self.nationality} and got freedom from british empire {self.year} year ago")
#
# #     @classmethod
# #     def free(cls,n,time):
# #         time=date.today().year-time
# #         return cls(n,time)
#
# # F=Freedom("Indian",1947)
# # F.independance()
#
# # F_Act=Freedom.free("Indian",1947)
# # F_Act.independance()
#
#
# from datetime import date
# class Car:
#     model_name=""
#     fuel_type=""
#     color=""
#     year=""
#     def __init__(self,nm,yr,c):
#         self.year=yr
#         self.model_name=nm
#         self.color=c
#
#     def details(self):
#         print(f"The car {self.model_name} is manufactured {self.year} yrs Ago and colour is  {self.color}")
#
#     @classmethod
#     def act_details(cls,nm,time,clr):
#         time=date.today().year-time
#         return cls(nm,time,clr)
#
#
# Toyota=Car("i20",2018,"black")
# Toyota.details()
#
# Tata=Car.act_details("nano",2001,"silver white and red")
# Tata.details()

## class var or static variable
class Test:
    a=10            ##within classname but outside the methods

    def __init__(self):
        Test.b=20   ##Inside the construcctor by using classname
    def m1(self):
        Test.c=30    ## inside instance method by using classname

    @classmethod
    def m3(cls):
        cls.d=40     ##By using cls var
        Test.e=50     ## inside classmethod by using classname

    @staticmethod
    def m4():
        Test.f=60    ## inside static method by usin classname

Test.g=70
print(Test.__dict__)  ## o/p is only 2 static var shows ...other will be obj
t=Test()
t.m1()
t.m4()
t.m3()




