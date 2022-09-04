# x=[10,20,[30,40],50]
# print(x[2][0])

## print in matrix form
#
# lst=[[10,20,30],[40,50,60],[70,80,90]]
# for i in range(len(lst)):
#     for j in range (len(lst[i])):
#         print(lst[i][j],end=" ")
#     print("ok")


# List comrehension
## Regular
# l1=[]
# for i in range(1,11):
#     l1.append(i**2)
#     print(l1)
## By list comprehension
# list=[Expression for x in sequence]  ## syntax
#
# l1=[x**2 for x in range(1,11)]
# print(l1)


## # list=[Expression for x in sequence if condition]    ## syntax

# l2=[x for x in range(1,20) if x%2==0]
# print(l2)

# for x in range (1,11):
#     if (x**2)%2 !=0:
#         print(x**2,end=" ")
#
# ##By using list comprehension
# l3=[x**2 for x in range(1,11) if (x**2)%2 != 0]
# print(l3)

w=['SANTOSH','KARCHE','TEAM','BRAINWORKS','sai','wai']
l=[x for x in w ]
print(l)

l1=[x for x in w if len(x)>=5]
print(l1)

l1=[[x.lower(),len(x)] for x in w if len(x)>=4]
print(l1)
