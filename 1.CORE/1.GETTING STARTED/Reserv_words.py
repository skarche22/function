# import keyword
# k=keyword.kwlist
# print(k)
# print(len(k))
#
# x=10
# print(bin(x))
# print(oct(x))
# print(hex(x))
# print(x)
# #
# # ##Complex Data types
# #
# # y=10+20j
# # print(y)
# # a=0B1111+20.3j
# # print(a)
# # z=30+50j
# # print(y+z)
# # print(z.real)
# # print(z.imag)
#
# ## Boolean Data types==true and false
# a=True
# b=False
# print(a+b)
# print(a**5)
# print(a*5)
# print(a-b)
# print(b-a)

##types casting
## InT Data type
print(int(10.123))
int(True)
print(int("10"))

## Float DATA TYPES
print(float(10))
print(float(True))
print(float(10.5))

##Complex Data Types
print(complex(10))
print(complex(20,30))
print(complex(True))
print(complex(False))
complex('10')

## Bool Function
print(bool(0))    # 0 will take false
print(bool(10))    # Non zero will take true
print(bool(-10))  # non zero will be True

print(bool(0.1))
print(bool(4.5))
print(bool('Santosh'))  # Bool with str returns true
print(bool(" "))
print(bool(""))     ## Bool with empty str returns False


## Str functionm
print(str(10+20j))
print(str("10+20j"))
