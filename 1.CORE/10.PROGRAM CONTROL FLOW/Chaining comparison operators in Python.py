# Chaining comparison operators in Python

# List of comparison operators in Python:">" | "<" | "==" | ">=" | "<=" | "!=" | "is" ["not"] | ["not"] "in"

# Python code to illustrate chaining comparison operators
x = 5
print(1 < x < 10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)


a, b, c, d, e, f = 0, 5, 12, 0, 15, 15

d is not e is f
exp2 = a is d & f is not c
 
print(exp2)

