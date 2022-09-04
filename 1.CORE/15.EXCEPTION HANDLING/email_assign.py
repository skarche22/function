# print("hello santosh")
#
# def factorial(x):
#     if x==1:
#         return x
#     else:
#         return (x * factorial(x-1))
# a=factorial(5)
# print(a)
#
# #Factorial Without recursion
# def fact(n):
#     result=1
#     for i in range(n):
#         result*=n
#         n=n-1
#     print(result)
# fact(5)

email=input("enter yur email :")  # eamil closes conditiom (g@g.in)
k,j,d=0,0,0
if len(email)>=6:   #(nikhil@gmail.com)  # email len is 6 ,nmore than 6 char so else is run (wrong email 1 is print)
    if email[0].isalpha():  #  in eamil 1 char is alphabhate . eg (nik@gamil.com)
        if ("@" in email) and (email.count("@")==1): # in mail @ are present or not to chek first condtion and in prest to chek how many time present in email
            if (email[-4]==".") ^ (email[-3]=="."):   # (^)in given  condtion both one condtion True so uotput is TRUE (check (.) postion in mail)
                for i in email:
                    if i==i.isspace():   # chek not space allowd in givin email #space condition
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():  #givaen mail is chek digit is present or not
                        continue
                    elif i=="_" or  i=="." or i=="@":   # to check all condition in mail
                        continue
                    else:
                        d=1   #  any spical symbol are used to print wrong mail


                if k==1 or j==1 or d==1:
                    print("wrong email 5")
                else:
                    print("Santosh you input mail is rigt )")
            else:
                print("wrong email 4")
        else:
            print("wrong eamil 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")