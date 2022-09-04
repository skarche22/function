# slice operator
# s[:]=====forward direction
# s[:-1]===backwaard direction

# ##print the string index and element
#
# s=input("entr some str:")
# print(len(s))
# i=0
# while i<len(s):
#         print("index=:",i,end=" ")
#         print(" char at index =",s[i])
#         i+=1
#
# # reverse direction
#
# i=len(s)-1           ## upto last index of given str
#
# while i>=0:
#         print("index=:", i, end=" ")
#         print(" char at index =", s[i])
#         i-=1

# #FINDING THE SUBSTRING AVL IN MAIN STR
# m=input("enter main str:")
# s=input("enter the substr")
# count=0
# for i in range(len(m)):
#         if m[i]==s:
#                 print("found at index",i)
#                 count += 1
#         else: print("not found at index:",i)
#
# print("the index found %d no of times" %(count))
#


## find str at even position
#
# str="santosh karche"
# i=0
# while i< len(str):
#         print(str[i],end=" ")
#         i+=2

## find str at odd position

# str="santosh karche"
# i=1
# while i< len(str):
#         print(str[i],end=" ")
#         i+=2

## input
s=input("Enter some str:")
# s1=s.split()
a=[]
b=[]
for i in s:
        if i.isalpha():
                a.append(i)
        else: b.append(i)
print(sorted(a),sorted(b))







# # REMOVE DUPLICATES FROM STR
# str="mississippi"
# ###1
# print(set(str))
# ##@2
