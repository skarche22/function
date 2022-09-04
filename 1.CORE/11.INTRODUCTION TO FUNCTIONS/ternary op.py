# from multiprocessing.sharedctypes import Value
# from optparse import Values


# ~a==unary operator taken only one Value
# a+b==Binary aoperator=-- contains two Values
# a,b,c==ternary op==contains 3 variables or 3 Values

## Ternary operator is only one : i.e.  Conditional operator

# Syntax: op= first_value if a<b else sec_value

a=100
b=20
c=30 if a<b else 40
print(c)

# Read Two int value from leyboard & print min value

a=int(input("enter 1st no:"))
b=int(input("enter second no:"))
min=a if a<b else b
print("The minimum value is:",min)



