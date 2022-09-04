# x=10
# printer="Dell"
# print("I just printed %s pages to the printer %s" % (x, printer))
#
# ##OR
# print("I just printed {0} pages to the printer {1}".format(x, printer))
# print("I  just printed {x} pages to the printer {printer}".format(x=7, printer="Dell"))
#
# ### OR
# x=10
# printer="Dell"
# print(f"I just printed {x} pages to the printer {printer}")
#
# print("{:*^20s}".format("Geeks"))
#
# ## to showing temprature
# print("the current temp in pune {0:0f} ".format(29.33))
#
#
# ## Escape sequences
#
# print("The time is \tvaluable thing")
# print("The time is  \\valuable thing")
# print("dson\'t waste time it is valuable thing")
# print('it is so \"unreal\"')
# print('\a')


# organization of large data using format()

# def unorg(a,b):
#     for i in (a,b):
#         print(i,i**2,i**3,i**4)
#
# def org(a,b):
#     for i in (a,b):
#         print("{:5d} {:5d} {:5d} {:5d}".format(i,i**2,i**3,i**4))
#
# print("=====before org=====")
# unorg(3,10)
# print()
#
# print("=====After org=====")
# org(3,10)
# print()

# Using a dictionary for string formatting

Full_name="hello my name is {first} {middle} {last} and im working as {profession}"
info= {
    'first':"SANTOSH",
    "middle":"AJINATH",
    'last':"KARCHE",
    'profession':"WEB DEVELOPER"
}

print(Full_name.format(**info))

