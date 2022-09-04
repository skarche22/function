# Generator: Without taking any input generator generates sequence of values(Yield keyword used)
# Helpful in memoryb utilization ==because it generates values but not store inside the memory

##@ by using generator  we can find fiboncci number

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b

# for f in fib():
#     if f>100:
#         break
#     print(f)




import sys
x=[1,2,3,4,5,6,7,8,9,10]
y=map(lambda x:x**2,x)
print(y)            ## Only obj map object at <0x000002208CCBF0A0>    
# print(list(y))      ## Stored inside list
print(next(y))
print(next(y))
print(y.__next__())

print("for loop starts which will print rest of the sequence")
for i in (y):        ## dont use range because map obj cant take as int
    print(i)


