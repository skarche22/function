# Control Flow in Python
# Decision-making statements in programming languages decide the direction of the flow of program execution. 
# In Python, if-else elif statement is used for decision making./
# i.e if a certain condition is true then a block of statement is executed otherwise not.
# if condition:
   # Statements to execute if
   # condition is true
#
# i = 10
#
# if (i > 15):
#     print("10 is less than 15")
# print("I am Not in if")

# python program to illustrate If else statement

  
# i = 20
# if (i < 15):
#     print("i is smaller than 15")
#     print("i'm in if Block")
# else:
#     print("i is greater than 15")
#     print("i'm in else Block")
# print("i'm not in if and not in else Block")
# print("statement executed")

## find the bigger no from given nos.
# n1=int(input("Enter first no:"))
# n2=int(input("Enter second no:"))
# n3=int(input("Enter Third no:"))
# #
# n1=eval(input("Enter first no:"))
# n2=eval(input("Enter second no:"))
# n3=eval(input("Enter Third no:"))
# if n1>n2 and n1>n3:
#     print("biggest no is:",n1)
#
# elif  n2>n3:
#     print("n2 is bigger")
#
# else: print("Biggest no is n3:",n3)

## no to check no is bet 1 to 100

n=int(input("enter the no:"))
if n>=1 and n <=100:
    print("no is in between  1to100")
else: print("no is out of range")

