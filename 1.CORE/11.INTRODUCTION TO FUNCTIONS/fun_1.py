# def fun(name):
#     print("Test the function",name)
# fun("Santosh")
#

# def test_Evenodd(n):
#     if n%2==0:
#         print("The no {} is even".format(n))
#     else:
#         print("The no {} is odd".format(n))
# test_Evenodd(32)

# find factorial of the given no
# by using for loop
# n=int(input("enter the no:"))
# fact=1
# for i in range(n):
#     fact=fact*n
#     n=n-1
#     print(fact)



# by using function
# # by using while loop`
# def fact(num):
#     fact = 1
#     while num >= 1:
#         fact = fact * num
#         num = num - 1
#     return fact
# print(fact(5))
# print(fact(7))
#
# # by using for loop`
# def fact(num):
#     fact = 1
#     for i in range(num):
#         fact = fact * num
#         num = num - 1
#     return fact
# print(fact(5))
# print(fact(7))

## Tee return value has a type of tuple:
#
# def calc(x,y):
#     sum= x+y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     return sum,sub,mul,div  # returned value is in tuple format
# print(calc(10,20))

# types of arguments:
# 1.Positional arguments
#
# def calc(a,b):
#     sub=a-b
#     return sub
#
# print(calc(50,30))
# print(calc(30,50))  # if we change the position of arguments result will be change
# print(calc(50,30,40)) #TypeError: calc() takes 2 positional arguments but 3 were given

# 2.keyword arguments

# def calc(a,b):
#     sub=a-b
#     return sub
#
# print(calc(a=50,b=30))  # declared as keyword
# print(calc(b=30,a=50))  # if we change the position of arguments result will not change
# print(calc(a=50,b=30,c=40))  # TypeError: calc() got an unexpected keyword argument 'c'


# 3.Default Argument
def calc(b,a=500):     # non default argument followed by default arg
    sub=a-b
    return sub

print(calc(a=50,b=30))  # declared as keyword
print(calc(300,a=50))  # The positional arguments followed by keyword arg
# print(calc(a=50,300))  #SyntaxError: positional argument follows keyword argument
print(calc(222,111))

# #4. Variable length arguments (*args)
# def calc(*q):
#     sum=0
#     for i in q:
#         print(type(q))
#         sum +=i
#         print("The sum is:",sum)
#
# print(calc(10,20,30,40,50))
# print(calc(10,20))
# print(calc())

# #5. Variable length Keywords length arguments (**kwargs)
#
# def calc(**kwargs):
#
#     for i,j in kwargs.items():
#        print("the key is {} and values {} a".format(i,j))
# calc(name="santosh",age=30,marks=98,game="TT")
# calc(name="sai",brand1="RC",brand2="KF")
# calc()
