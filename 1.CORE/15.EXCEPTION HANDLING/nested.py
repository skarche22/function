# #loops in else
# for x in range(10):
#     print ("the value of x is",x)
# else:
#     print("your program successfully executed")
#
# print(" 2> By using if inside the block")
# for x in range(10):
#     if x>5:
#         break
#     print ("the value of x is",x)
# else:
#     print("your program successfully executes")


##Else  block with Try -Except -Finally

#
# try:
#  Risky Code
# except:
#  Handling Code
# finally:
#  Cleanup code

#
# try:
#     print('try')
# except:
#     print('except')
# else:
#     print('else')
# finally:
#     print('finally')

## When the exception ind=side try block
#
# else block with try-except-finally:
# We can use else block with try-except-finally blocks.
# else block will be executed if and only if there are no exceptions inside try block.
# try:
# Risky Code
# except:
# will be executed if exception inside try
# else:
# will be executed if there is no exception inside try
# finally:
# will be executed whether exception raised or not raised and handled or not
# handled

try:
    print('try')
    print(10/0)
except:
    print('except')
else:
    print('else')
finally:
    print('finally')

