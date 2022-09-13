import math
num=int(input("enter the number to find fact:"))
try:
    result=math.factorial(num)
    print(result)
except:
    print("cannot compute the fact of negative nos")    