#1. gloabal variable:The variable which is declared outside the function and accessible to all fun
# a=500   # This is global variable
def f1():
    a=333  # this is local variable
   #global a  #SyntaxError: name 'a' is assigned to before global declaration
    print("f1",a)

def f2():
    global a   # this is global keyword which shows the var a is now applicable for the all next functons
    a=222

    print("This is f2",a)

def f3():
    print("This is f3",a)
f1()
f2()
f3()