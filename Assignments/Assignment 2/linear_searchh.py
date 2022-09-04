# lst=[10,20,40,30,29,30]
# c=int(input("the no is req to search:"))
# for i in lst:
#     if i==c:
#         print("elemet found",i)
#     else:
#         pass


#
# lst=[10,20,40,30,29,30]
# c=int(input("the no is req to search:"))
# for i in range(len(lst)):
#     if lst[i]==c:
#         print(i)
#     else: continue


lst=[10,20,40,30,29,30]
c=int(input("the no is req to search:"))

try:
    n=lst.index(c)
except ValueError:
    print("not found")
else:
    print("found",n)
