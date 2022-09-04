# ## Apply more than one decorator is dec chaining 
# ## 


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

def upper_d(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(func):
    def inner():
        str2=func()
        return str2.split()
    return inner 

@split_d
@upper_d
def simple():
    return "good morning"
print(simple())          
