# function decorator is take function as argument and extend its functionality and
# returns modified function with extended functionality
# main objective of dec:extend functionality of existing fun without modifies that function


# def decor(func):
#     def inner(name):
#         if name=="Nitin":
#             print("Not my best friend now",name)
#         else:
#             func(name)
#
#     return inner
# @decor
# def wish(name):
#     print("my best frind:",name)
#
# wish("Ajit")
# wish("pramod")
# wish("Nitin")

##2 modifications req in func
#
# def decor(func):
#     def inner(number):
#         print(number+5)
#         # number()
#     return inner
#
# @decor
# def number():
#     return 10
#
# f1=number(10)
# f1()

# s={1,2,3,4,5,6}
# s.add(10)
# s2=[33,44,55]
# s3={34,46,56}
# s4=(35,47,57)
# s.update((111,232))
# # s.add([232,3334])    TypeError: unhashable type: 'list'
# s.update([232,3334])   #possible
# s.update(s2,s3,s4)
# print(s)

#
# def decor(func):
#     def change():
#         print("new num to addition to add fun")
#         x=add()
#         print(x+300)
#         return x+300
#     return change
# @decor
# def add():
#     return 10
# add()

# rec=decor(add)
# print(rec())


# def dec1(num):
#     def inner():
#         b=num()
#         mul=b*10
#         return mul
#     return inner
#
# def dec2(num):
#     def inner2():
#         a=num()
#         add=a+555
#         return add
#     return inner2
#
# # @decor1
# def num():
#     return 10
# num1=dec2(dec1(num))
# print(num1())


# def dec(func):
#     def inner(a,b):
#         print("try div of a and b")
#         if b==0:
#             return "pl give valid input"
#         else:
#             return(a/b)
#     return inner
# @dec
# def divs(a,b):
#     return a/b
# print(divs(200,0))


##@@@ Problem of dec @@###
#
# import time
# def cal_sq(nos):
#     start=time.time()
#     res=[]
#     for i in nos:
#         res.append(i*i)
#     end=time.time()
#     print("To calc square it took"+ str((end-start)*1000)+"time")
#     return res
#
# def cal_cube(nos):
#     start = time.time()
#     res=[]
#     for i in nos:
#         res.append(i*i*i)
#     end = time.time()
#     print("To calc cube it took" + str((end-start)*1000) + "time")
#     return res
# array=range(1,100)
# print(cal_sq(array))
# print(cal_cube(array))

 ##  in above eg it seems that the fun take much time to execute
 # it seems that the complex code and less redability
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
# def cal_cube(nos):
#     res=[]
#     for i in nos:
#         res.append(i*i*i)
#     return res
#
# array=range(1,10)
# print(cal_sq(array))
# print(cal_cube(array))


#ex 1.
def dec_fun(func):
    def wrapper(*args,**kwargs):
        print("Wrapper executed this before {}".format(func.__name__))
        return func(*args,**kwargs)
    return wrapper


@dec_fun
def display():
    print("Display fun run")
display()

@dec_fun
def display_info(name,age):
    print("display_info ran with arg ({} , {})".format(name,age))
display_info("SANTOSH",30)