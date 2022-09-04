## Anonymous function
##fn declare without any name is lambda fn
# syntax== lambda arg_list: Expression
# lambda n:n*n
# By using lambda fn we can write very concise code so that readability of code will be improved 

## Q. Write a program to create a lambda function to find square of given number?

sq=lambda x:x**2
print(sq(10))

## Q.Lambda Function to find biggest of given values.
y=lambda a,b: a if a>b else b
print(y(200,100))
print("The biggest value is:", y(500,300))



# Note:
# Lambda Function internally returns expression value and we are not required to write return statement explicitly.
# We can use lambda functions very commonly with filter(),map() and reduce() functions,b'z these functions expect function as argument.

# filter() function:
# We can use filter() function to filter values from the given sequence based on some condition.
# #@@ SYNTAX==== filter(function,sequence)
#  where function argument is responsible to perform conditional check sequence can be list or tuple or string.

##Q.Q. Program to filter only even numbers from the list by using filter() function?

##@ 1.Filter functiom



# syntax==
# filter(function,sequence)====function can applies for every elements in sequence
##===Filter is used to filter the values based on condition in given sequence (True(considers value) and false(ignore value) conditions we are mostly using)

def iseven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
l1=list(filter(iseven,l))
print(l1)               # in filter we get output nunber is not same
## By using lambda function filter odd values
s=list(filter(lambda x:x%2!=0,l))
print(s)

## @@@ Map Function===To perform some business logic / perform the operations 
## 0n every element present in sequence 
# For every element present in the given sequence,apply some functionality and generate new element with the required modification. For this requirement we should go for 
# map() function.  SYNTAX==== map(function,sequence)
def double(x):
    return 2*x
l=[0,5,10,15,20,25,30]
l1=list(map(double,l))
print(l1) 
## By using lambda with map
s=list(map(lambda x:2*x,l))
print(s)
## By using lambda with map find square

square=list(map(lambda x:x*x,l))
print(square)

## By using the map fn multiply elements from two lists...(both list should have same length then only possible)
l1=[1,2,3,5,6,7]
l2=[1,2,3,5,6,7]
s=list(map(lambda x,y:x*y,l1,l2))
print(s)

# reduce() function:reduce() function reduces sequence of elements into a single element by applying the specified function.
# ##@@  SYNTAX=== reduce(function,sequence)
# reduce() function present in functools module and hence we should write import statement.
from functools import*
l1=[1,2,3,5,6,7]
r=reduce(lambda x,y:x+y,l1)
print("after using reduce fun",r)


p=reduce(lambda x,y:x*y*10,l1)
print(p)

result=reduce(lambda x,y:x+y,range(1,100))
print(result)



##WE CAN PASS FUNCTION AS ARGUMENT TO ANOTHER FUNCTION

# 1.filter(function,sequence)
# 2.map(function,sequence)
# 3.reduce(function,sequence)