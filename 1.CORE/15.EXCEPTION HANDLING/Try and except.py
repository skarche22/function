# try:
#  Risky Code
# except XXX:
#  Handling code/Alternative Code
#
# try:
#     a=int(input("enter 1st no:"))
#     b=int(input("enter 2nd  no:"))
#     print(a/b)
#     print(a.__class__.__name__)
# except Exception as msg:
#     print("Exception type:",type(msg))
#     print("Exception type:", msg.__class__)   ##obj return
#     print("Exception class name:", msg.__class__.__name__)  ## str returns
#     print("Exception Discription:", msg)


## Try with multiple exception block

# try:
#     a=int(input("enter 1st no:"))
#     b=int(input("enter 2nd  no:"))
#     print(a/b)
#
# except (ZeroDivisionError) as msg:
#     print("the rise Exception:", msg.__class__.__name__)
#     print ("the discription of exception:",msg)
#     print("please provide valid input only")
#
# except ValueError:
#     print("pl provide valid input")


