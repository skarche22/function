# Python For Loops==sequential traversal i.e. it is used for iterating over an iterable like String, Tuple, List, Set or Dictionary.
# Note: In Python, for loops only implements the collection-based iteration.
# Using loops in Python automates and repeats the tasks in an efficient manner.
#
# # Python program to illustrate Iterating over a list
# l = ["santosh","ajinath",'karche','pune']
# for i in l:
#     print(i)
#
#
#
# # Iterating over dictionary
# print("Dictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#     print((i))

    
# # Iterating over a String
# print("String Iteration")
# s = "MOTHER AND FATHER"
# # for i in s:
# #     print(i,end="+")
#
#
# # Prints all letters except 'e' and 's'
# s='geeksforgeeks'
# i=0
# for letter in s:
#     if letter == 'e' or letter == 's':
#         continue
#     i+=1
#
#     print('The chr present at index ',i,"is",letter)
#     print('Current Letter :', letter)


# Break Statement in Python
# Python break is used to terminate the execution of the loop. 
#
# num = 0
# for i in range(10):
#     num += 1
#     if num == 8:
#         break
#     print("The num has value:", num)
# print("Out of loop")

# By using While loop
# num = 0
# while (num<=10):
#     num+=1
#     if num == 5:
#         break
#     print(num)



# Looping Techniques in Python
# A lot of time and memory space is been saved as there is no need to declare
# the extra variables which we declare in the traditional approach of loops.
# This can also be used in instances to save time.

# Using enumerate():printing the index number along with the value present in that particular index.
##1
# for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
#     print(key, value)
#     # print(value, end=' ')

##2
# a="santosh"
# for i,j in enumerate(a):
#     print(i,j)

##3
# a="my name is santosh"
# for i,j in enumerate(a):
#     print(i,j)
#
# for k,v in enumerate(['my','favourit','web','developement','program','in','python']):
#     print(k,v)

# Using zip(): zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially.    
##1
# questions = ['name', 'colour', 'shape']
# answers = ['apple', 'red', 'a circle']
#
# for question, answer in zip(questions, answers):
#     print('What is your {0}?  I am {1}.'.format(question, answer))
#
# 2
# lang=['python','mysql','git']
# use=['program','RDBMS','version control']
#
# for lang,use in zip(lang,use):
#     print('which software lang {0}? and used for {1}'.format(lang,use))

##3
# key= [1,2,3,4,5,6]
# val=['TCS','INFO','PER','COGN','GDF','FRT']
# for a,b in zip(key,val):
#     print(f"the compay is leading in no ({a}) and the name is: {b}".format(key,val))

##3.1
# key= {1,2,3,4,5,6}
# val={'TCS','INFO','PER','COGN','GDF','FRT'}
# for a,b in zip(key,val):
#     print(f"the compay is leading in no ({a}) and the name is: {b}".format(key,val))


# Using sorted():  sorted() is used to print the container is sorted order.
lis = [1, 3, 5, 6, 2, 1, 3]
 
# using sorted() to print the list in sorted order
print("The list in sorted order is : ")
for i in sorted(lis):
    print(i, end=" ")
 
print("\r")
print("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
    print(i, end=" ")

# Using reversed(): reversed() is used to print the values of the container in the reversed order. 
# It does not reflect any changes to the original list
lis = [1, 3, 5, 6, 2, 1, 3]
 
 
# using reversed() to print the list in reversed order
print("The list in reversed order is : ")
for i in reversed(lis):
    print(i, end=" ")    
print("range")
for i in reversed(range(1, 10, 3)):
    print(i)    

    