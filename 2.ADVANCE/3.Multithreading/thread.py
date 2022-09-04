import threading
from threading import*

# class Test:
#     def m1(self):
#         for i in range(5):
#             print("hello")
#
# ob=Test()
# ob.m1()
# for i in range(5):
#     print("By")

# class Test:
#     def m1(self):
#         for i in range(2):
#             print("hello")
#
# ob=Test()
# t1=Thread(target=ob.m1)
# t1.start()
# for i in range(2):
#     print("By")
#
##2. Create thread using fun

# def myfun():
#     for i in range(2):
#         print(i)
#
# t1=Thread(target=myFun())
# t1.start()
# for i in range (2):
#     print("Good bye")


# ##3. create thread using extend thread class
# class Test(Thread):
#     def m1(self):
#         for i in range(1,3):
#             print("class thread:",i)
# ob=Test()
# ob.m1()
# ob.start()
# ob2=Test()
# ob2.m1()
# ob2.start()
#
# for j in range(11,13):
#     print("main thread:",j)
# print("Active thread count is:",active_count())
# # time.sleep(2)

##4.
#
# class Test(Thread):
#     def m1(self):
#         for i in range(1,6):
#             print("class threds",i)
# ob=Test()
# t1=thread(target=ob.m1())
# t1.start()
#
# for j in range(11,16):
#     print("main Thread",j)
#
# print("Active thread count",active_count())


# def myfun1():
#     for i in range(2):
#         print('tread of myfun',i)
#
# t1=Thread(target = myfun1())
# t1.start()
# def myfun2():
#     for i in range(2):
#         print("main thread",i)
# myfun2()
import time
class Test():
    def m1(self):
        for i in range(1,6):
            time.sleep(3)
            print("class thread",i)
ob=Test()
t1=Thread(target= ob.m1)
t1.start()

t2=Thread(target= ob.m1)
t2.start()

print("@ Active thread count is ",active_count())

t3=Thread(target= ob.m1)
t3.start()

t4=Thread(target= ob.m1)
t4.start()
print("@ Active thread count is ",active_count())