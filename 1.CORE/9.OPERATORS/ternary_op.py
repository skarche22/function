
# Ternary operators==
a=int(input("enter first no:"))
b=int(input("enter sec no:"))

# min=a if a<b else b  ## by using ternry op
# print(min)

# nORMAL
if a != b:
    if a>b:
        print("a is greater",a)
    else: print("b is greater",b)

else: print("both are equal")

## BY USING TERNARY

print(a if a>b else b )
