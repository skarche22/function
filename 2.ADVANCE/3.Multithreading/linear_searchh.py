# lst=[10,20,40,30,29,30]
# c=int(input("the no is req to search:"))
# for i in lst:
#     if i==c:
#         print("elemet found",i)
#     else:
#         pass


#
# a=[10,20,40,30,29,30]
# b=int(input("the no is req to search:"))
# c=len(a)
# for i in range (len(a)):
#     if a[i]==b:
#         print("found")
#         break
#     else:
#         if (c-1)==i:
#             print("not found")


# Using try except
# lst=[10,20,40,30,29,30]
# c=int(input("the no is req to search:"))
#
# try:
#     n=lst.index(c)
# except ValueError:
#     print("not found")
# else:
#     print("found",n)


l=[1,2,3,4,5,6,7]
a=int(input("Enter no:"))
count=0
res=1
for i in range (len(l)):
    if l[i]==a:
        res=f"the index{i}, number {a} is found"
    count+=1
if len(l)==count and a in l:
    print(res)
else: print("Not found")
