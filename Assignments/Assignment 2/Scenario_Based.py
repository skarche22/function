# Scenario Based Programs:
# 1. Python Program for Linear Search
# def linier_srch(lst,n,key):
#     for i in range (n):
#         if lst[i]==key:
#             print(i)
#             return i
#
# lst=['vijay','Arjun','Santosh','Nishikant']
# n=len(lst)
# # key=("Santosh")
# key=("santosh")
# res=linier_srch(lst,n,key)
# if res==None:
#     print("Not found")
# else: print("Found at", res)

# ##2
# def linier_srch(lst,n,key):
#     for i in range (n):
#         if lst[i]==key:
#             print(i)
#             return i
#     else:
#         return 0
#
# lst=['vijay','Arjun','Santosh','Nishikant']
# n=len(lst)
# # key=("Santosh")
# key=("santosh")
# res=linier_srch(lst,n,key)
# if res:
#     print("Not found")
# else: print("Found at", res)


# 2. Python Program for Binary Search (Recursive and Iterative)
## it will work if and only if the list is already sorted
def Binary_srch(lst,key):
    for i in range (0,len(lst)):
        low=0
        high=len(lst)-1
        mid=0
        while low<=high:
            mid=(low + high)//2
            if lst[mid]<key:
                low=mid+1
            elif lst[mid]>key:
                high=mid-1
            else:
                return mid
        return -1

lst=[12,24,36,48,60,72]
n=len(lst)
# key=("Santosh")
key=48
res=Binary_srch(lst,key)
if res==-1:
    print("Not found")
else: print("Found at", res)


# 3. Python Program for Bubble Sort
# 4. Write a python program for string that will print out char with char count.
# E.g. words = 'aaaabahhhhhaaa' Output should be a4b1a1h5
# 5. Write a python program to take command line arguments. (using docopt and other
# libraries). Two or more programs.
# 6. Write a python program to take input date string, time string is in UTC format we need to
# convert it into PST and print converted date time. E.g. input: “2023-02-13 18:10:27”
# 7. write a program for character count string "aaabbbccaa" for output:a5b3c2
# 8. Write a decorator for calculating execution time of any python function.
# 9. Problem: Remove specified characters in a string irrespective of the
# case.char_to_remove =['A','N'] string= 'Think Analytics'
# 5.Problem: Perform below task
# 1) Create a list of 10 even numbers using list comprehension.
# 2) Create a list of 10 odd numbers using list comprehension.
# 3) Multiply and sum them up while iterating over once.
# x = x1 + x2 + x3 + ....... + x9 + x10
# y = y1 + y2 + y3 + ....... + y9 + y10
# z = x1y1 + x2y2 + x3y3 + ....... + x9y9 + x10y10
# 10. create decorator for function which prints its arguments. decorator should check if
# argument divided by 2. if it is then only run the function.
# 11. Student management system in Python( Using Class and Object)
# Problem Statement: Write a program to build a simple Student Management System
# using Python which can perform the following operations:
# Accept, Display, Search, Delete, Update
# Accept – This method takes details from the user like name, roll number, and marks for
# two different subjects
# Search – This method searches for a particular student from the list of students. This
# method will ask the user for roll number and then search according to the roll number
# Delete – This method deletes the record of a particular student with a matching roll
# number
# Update – This method updates the roll number of the student. This method will ask for
# the old roll number and new roll number. It will replace the old roll number with a new roll
# number.
# # 12. Write a program to convert json file to csv file