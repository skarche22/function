# Flowchart of Python Nested if Statement
# Nested if statements mean an if statement inside another if statement.
# i.e, we can place an if statement inside another if statement.

# Syntax: 

# if (condition1):
#    # Executes when condition1 is true
#    if (condition2): 
#       # Executes when condition2 is true
#    # if Block is end here
# # if Block is end here

i = 10
if (i == 10):
    
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")
          
    # Nested - if statement Will only be executed if statement above it is true
    if (i > 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 1 to 9")

# if-elif-else ladder==The if statements are executed from the top down. 
# # Syntax: 

# if (condition):
#     statement
# elif (condition):
#     statement
# .
# .
# else:
#     statement  
      
x=int(input("value of x:"))
if (x==150):
    print("x is greater than 100")
elif(x==98):
    print("x is less than 100") 
elif(x==100):
    print("value is 100")    
else:
    print("value of x is not matching")


    