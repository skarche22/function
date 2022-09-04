# TUPLE PACKING AND UNPACKING:
#
# PACKING TUPLE:

a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)

# UNPACING TUPLE:

t=(10,20,30,40)
a,b,c,d=t
print("a=",a,"b=",b,"c=",c,"d=",d)

#
#
# import sys
# t=()
# print(f"no of elements: {0}, size{sys.getsizeof(t)}, diff:{0}")
# pre=40
#
# for i in range(1,20):
#     t=tuple(range(1,i+1))
#     print(t)
#     temp=sys.getsizeof(t)
#     diff,pre=temp-pre ,temp
#     print(f"no of elements:{i}, size{sys.getsizeof(t)}, diff:{diff}")