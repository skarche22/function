# Default except block:
# We can use default except block to handle any type of exceptions.
# x=555
# y="hundred"
# try:
#   c=x/y
#   print(c)


# except ZeroDivisionError:
#     print("can't devide with zero")

# except Exception as e:               ## default exception block
#     print("Provide : ",e," to avoid the error")


## By giving user input

n1=int(input("Enter 1st num:"))
n2=int(input("Enter 2nd no:"))
try:
    c=n1/n2
    print(c)
except ZeroDivisionError:
    print("provide denominator to devide ")

except:
    print("Error other than zerodiv")    

else:
    print("This programme executed successfully")    


