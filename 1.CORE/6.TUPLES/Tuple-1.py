# #empty tuple
# t=tuple()
# print(t)
# print(type(t))
# T=()
# print(type(T))

# x=eval(input("enter:"))
# print(x)
# print(type(x))

#Accessing the elements from tuple
# by their indexes

#
# T=(11,22,33,44,55,66)
# print(T[-2])
# print(T[2])

#Traversing == traversal of sequence means accessing & processing each elements of it.
# T=(11,22,33,44,55,66)
# for i in T:
#     print(i)
#
# for i in range (len(T)):
#     print(i)

# similarity with str & list
# len(), Indexing, slicing
# Membership operators(in & not in) 
# Concatenation operators (+ AND *) 
#
# T=(11,22,33,44,55,66)
# # print(T[2:])
# # print(44 in T)
# # print(100 in T)
# #
# T1=(12,22,44,55,77,88)
# print(T1[-1])
# print(T1>T)
# print(T>=T1)
# print(T!=T1)
# print(T==T1)
# T2=('A','B','C','D')
# print(T1!=T2)
#
# # # Tuple operations =
# # 1.Concatenation(+)
# # print(T1+T2)
#
# # T1.extend(T2)    ###AttributeError: 'tuple' object has no attribute 'extend'
# # print(T1)
#
# # 2.Replications(*)
# # print(T1*2)
#
# l=[]
# for i in range (len(T1)):
#     x=T1[i] * 2
#     l.append(x)
# print(l)


t=eval(input("enter the tuple of elemets:"))
c=0
sum=0
for i in t:
    c+=1
    sum+=i
print("The sum of elements",sum)
print(c)
print("The average of elements",sum/c)