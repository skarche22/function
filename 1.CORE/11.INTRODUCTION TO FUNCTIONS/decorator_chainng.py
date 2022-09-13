# def dec(func):
#     def inner():
#         print("@@@@@@@@@@@@@ Started @@@@@@@@@@@")
#         print(func())
#         print("@@@@@@@@@@@@ Ended @@@@@@@@@@@@@@")
      
#     return inner()

# @dec
# def welcome():
#     return "Welcome to python decorator"
  
# def dec(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)            
#     return inner

# @dec
# def div(a,b):
#     return(a/b)
# print(div(2,4))    




# ## Apply more than one decorator is dec chaining 



# def startwice(func):
#     def inner(*args,**kwargs):
#         print("**")
#         func(*args,**kwargs)
#         print("**")
#     return inner

# def starthrice(func):
#     def inner(*args,**kwargs):
#         print("***")
#         func(*args,**kwargs)
#         print("***")
#     return inner


# @startwice
# @starthrice
# def simple_fun(mymsg):
#     print(mymsg)
# if __name__=='__main__':
#     simple_fun("Python is best")



## take a one str and convert into upper and split

# def upper_d(func):
#     def inner():
#         str1=func()
#         return str1.upper()
#     return inner

# def split_d(func):
#     def inner():
#         str2=func()
#         return str2.split()
#     return inner 

# @split_d
# @upper_d
# def simple():
#     return "good morning"
# print(simple())          


# import time
# def timeit(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result=func(*args,**kwargs)
#         end = time.time()
#         print(func.__name__+"took" + str((end-start)*1000) + "time in millisec")
#         return result
#     return wrapper
# @timeit
# def cal_sq(nos):
#     res=[]
#     for i in nos:
#         res.append(i*i)
#     return res
# @timeit    
# def cal_cube(nos):
#     res=[]
#     for i in nos:
#         res.append(i*i*i)
#     return res

# array=range(1,10)
# print(cal_sq(array))
# print(cal_cube(array))