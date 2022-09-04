##FUNCTION ALIASING

# # we can give another name to existing function 
# def god(name):
#     print("The favorite god of maharashtra",name)

# vidhata=god
# vidhata("Shri Ganesha")
# god("Shri krishna")

# print(id(vidhata))
# print(id(god))

# ## Same ids is for aliasing and main function which is assigned for same obj


# del god
# print(id(god))       ##Here NameError: name 'god' is not defined


##NESTED FUNCTION

#we can declare function inside the function

def outer():
    print("outer function is started")
    def inner():
        print("inner fun execution")
    print("outer fun calling inner fun")
    inner()
    inner()        ## here inner function is local to outer fun so not possible to call from outside the outer
f1=outer()         
# f1()             #TypeError: 'NoneType' object is not callable


def outer():
    print("outer function is started")
    def inner():
        print("inner fun execution")
    print("outer fun calling inner fun")
    return inner                         ## function can return another function
f1=outer()                               ## we calling outer fun which returns inner fun
f1()                                      ##for inner fun we are providing another name 