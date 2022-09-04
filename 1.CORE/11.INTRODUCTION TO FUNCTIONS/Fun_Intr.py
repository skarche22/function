# Introduction to fun
#the main adv of fun is code reusbility

# #try the fun should be in camelcase

# # syntax   == 

# # def function_name(parameter):
# #     """docstring"""
# #     statement(s)
# #     return expression


# # A simple python function
#
# def funHello():
#     print("Welcome to team braiworks")
#
# funHello()

# def sum(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y
#
# x=int(input("enter 1st no:"))
# y=int(input("enter second no:"))
#
# print(sum(x,y),sub(x,y),mul(x,y),div(x,y))
# print(sub(x,y))
# print(mul(x,y))
# print(div(x,y))
# ##Function to check evenodd(how to pass arg and call it)

# def evenOdd(x):
#     '''fun to check if no is even or odd'''
#     if (x%2==0):
#         print("even:",x)
#     else:
#         print("odd:",x)
# n=int(input("Enter the number to find result:"))
# print(evenOdd.__doc__)
# for i in range(n):
#     evenOdd(i)
#
## python programme to demonstrate the default argument==
# def myFun(x,y=50):
#     print("x:",x,"y:",y)
#
# myFun(20)

# ## python programme to demonstrate the keyword argument==
# def user(fname,lname):
#     print(fname,lname)
#
# user(lname='karche',fname='santosh')

# ## variable len non-keword arg
# def fun(*args):
#     for arg in args:
#         print(arg)
# fun('Hello','Welcome','to','Team','brainworks')

# ##
# def fun(*argv,x):
#     for arg in argv:
#         print(arg)
#     print(x)
# fun('Hello','Welcome','to','Team','brainworks',x=10)

