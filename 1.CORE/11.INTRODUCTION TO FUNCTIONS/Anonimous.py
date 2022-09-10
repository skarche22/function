# The function without name is known as anonimous function
# the def keyword is used to define a normal function in Python.Similarly,
# the lambda keyword is used to define an anonymous function in Python.

# 1)If we want to pass function as argument to another function then lambda is used   f1=func(func,s)
# Sntax:   lambda arguments: expression

# This function can have any number of arguments but only one expression, which is evaluated and returned.

# str="santoshdadada"
# rev_upper=lambda str:str.upper()
# print(rev_upper(str))
#
# x=10
# # sq=lambda x:x*x
# # print(sq(x))
# s=(lambda x:x*x)
# print(s(x))

#2 lambda inputs: expression
# 1) lambda by using ternary operator
# d=lambda a,b: a if a>b else b
# print(d(200,400))
# print("The biggest val is{}:".format(d(20,30)))
# # 2 find sum
# sum=lambda a,b:a+b
# print(sum(100,300))

#
# ## Filter function is used for conditional check##   SYNTAX: filter(function,sequence)
# in filter the output will need not to same as length
# l=[0,2,3,4,5,6,7,89,4,7]
# l1=list(filter(lambda x:x%2==0,l))  # It checks True or False
# print(l1)
#
# Filter odd nos in sequence
# lst=[1,2,3,4,5,6,7,8,9,10]
# l1=list(filter(lambda n:n%2 !=0 , lst))
# print(l1)

#

# ## map function == it will work on each element of sequence
# # syntax::  map (function, sequence)  ## it will returns map obj and it req to typecast into list
# def double(x):
#     return x*2
# print(double(2))
#
# ##
# # def doubleit(x):
# #     return 2*x
# l=[2,4,6,8,10,12]
# # l1=list(map(doubleit,l))
#
# l1=list(map(lambda x:x*2 ,l))
# print(l1)
# #
# # Perform operations on two lists
# l1=[1,2,3,4,5,6,7]
# l2=[10,20,30,40,50,60,70]
# print(type(l2))            # it will returns sequence
# res= list(map(lambda a,b:a*b ,l1,l2))
# print(res)
#
# # #REDUCE === reduce(function, sequence)
# from functools import *
# l=[44,55,66,77,88,99,11]
# l1=reduce(lambda x,y:x+y ,l)
# print(type(l1))               # it will returns int val and which is single
# print(l1)
#
# #Addition of elements in sequence
# # by regular fun
# from functools import *
# l=[10,20,30,40,50]
# # def addition():
# #     res=0
# #     for i in l:
# #         res+=i
# #     return res
# # print(addition())
#
#
# # by lambda
# r=reduce(lambda x,y:x+y ,l)
# print(r)

























































































































































