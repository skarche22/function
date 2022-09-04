# python bydefault latest method considedrr
#
# class A:
#     def abc(self,a):
#         print(a)
#     def abc(self,a,b):
#         print(a)
#     def abc(self,a,b,c):
#         print(a)
#
# o=A()
# # o.abc(5)
# # o.abc(5,10)
# # o.abc(5,10,15)
#
#
# # By using var length arg
# class A:
#     def abc(self,*x):
#         print(sum(x))
#
#
# o=A()
# o.abc(5)
# o.abc(5,10)
# o.abc(5,10,15)
# #
# # ## By using default argument
# #
# # class A:
# #     def abc(self,a=5,b=10,c=15):
# #         print(a+b+c)
# #
# # o=A()
# # o.abc()
# # o.abc(5)
# # o.abc(5,1)
# # o.abc(5,100,150)
#
# ##Method 1
# class A:
#     def abc(self,a=0,b=0,c=0):
#         print(a+b+c)
# o=A()
# o.abc()
# o.abc(5)
# o.abc(5,1)
# o.abc(5,100,150)
#
# ##Method 2
#
# class A:
#     def abc(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and c!=None:
#             print(a+c)
#
# o=A()
# o.abc()
# o.abc(5)
# o.abc(5,1)
# o.abc(5,100,150)


## Operator Overloading
## Concatinate
# class A:
#     def abc(self):
#         a=10
#         b=20
#         print(a+b)
#         a=input("enter the name:")
#         b = input("enter the name:")
#         print(a+b)
#
# o=A()
# o.abc()

## Multiplier
# class A:
#     def abc(self):
#         a=10
#         b=20
#         print(a*b)
#         a=input("enter the name:")
#         b = int(input("enter multiplier:"))
#         print(a*b)
#
# o=A()
# o.abc()

## constructor overloading
#
# class A:
#     def __init__(self):
#         a=10
#         b=20
#         print(a+b)
#
#     def abc(self):
#         c=30
#         d=40
#         print(c+d)
# o=A()
# o.abc()