# function decorator is take function as argument and extend its functionality and returns modified function with extended functionality
# main objective of dec:extend functionality of existing fun without modifies that function


# def decor(func):
#     def inner(name):
#         if name=="Nitin":
#             print("Not my best friend now",name)
#         else:
#             func(name)    
     
#     return inner 
# @decor
# def wish(name):
#     print("my best frind:",name)

# wish("Ajit") 
# wish("pramod")
# wish("Nitin")

##2 modifications req in func

def decor(func):
    def inner(number):
        print(number+5)
        # number()
    return inner    

@decor
def number():
    return 10

f1=number(10)   
# f1()