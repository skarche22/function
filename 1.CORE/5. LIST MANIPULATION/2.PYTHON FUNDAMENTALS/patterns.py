# for i in range(5):
#     print("@",end="*")
#
#
# n=int(input("enter the no of rows:"))
# for i in range(n):
#     print("@"*n)

# n = int(input("enter the no of rows:"))
# for i in range(n):
#     print("@" * i)


# n = int(input("enter the no of rows:"))
# for i in range(1,n+1):
#     print("@" * i)


n = int(input("enter the no of rows:"))
for i in range(1,n+1):
    print("@" * i)


n = int(input("enter the no of rows:"))
for i in range(1,n+1):
    for j in range(i+3):
        print("@" * j,end=" ")
    print()