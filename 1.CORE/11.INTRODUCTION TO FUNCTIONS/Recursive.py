#The function that calls itself is called recursive function
# advantages 1.Reduces the length of code and improves the readability .2)complex problems solve easily
def fact(n):
    if n==0:
        result= 1
    else:
        result =n * fact(n-1)
    return result
print(fact(5))
print(fact(0))
