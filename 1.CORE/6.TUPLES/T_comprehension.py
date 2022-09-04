
# TUPLE COMPREHENSION:


t=(x**2 for x in range(1,6))  ## Tuple comprehension is not possible
print(type(t))    ## It will returns the generator obj


for x in t:     ## To get output use for loop and we can access the elen=ments
    print(x)


