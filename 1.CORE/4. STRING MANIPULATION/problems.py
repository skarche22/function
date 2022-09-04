##seperate the alphabets and dig and show in str format in sorted way***
#
# s=input("enter the str:")
#
# Alphabet=Digits=other=oup=""
# for i in s:
#     if i.isalpha():
#         Alphabet+=i
#     elif i.isdigit():
#         Digits += i
#     else: other+=i
# print(Alphabet," ",Digits," ",other)
# print("THE OUPUT",oup)
# for x in sorted(Alphabet):
#     oup +=x
# for y in sorted(Digits):
#     oup+=y
# for z in other:
#     oup+=z
# print(oup)    ## It willl be shows op in  str format

#
#
# ## If str multiplication req
#
# s=input("enter a input")
# op=""
# for i in s:
#     if i.isalpha():
#         op+=i
#         prev=i
#     else:
#         op=op+prev*(int(i)-1)
# print(op)

##2

# s=input("enter a input")
# op=""
# for i in s:
#     if i.isalpha():
#         x=i
#
#     else:
#         op=op+x*int(i)
# print(op)

#
# # Q. find a4=a...e==ae
# s=input("enter str")
# res=""
# for i in s:
#     if i.isalpha():
#         res=res+i
#         x=i
#     else:
#         newchar=chr(ord(x)+int(i))
#         res=res+newchar
# print(res)


#@## find output two str of alternative char
# s1=input("enter first str:")
# s2=input("enter second str:")
# op=''
# i=j=0
# while i<len(s1) or j<len(s2):
#     op=op+s1[i]+s2[j]
#     i+=1
#     j+=1
# print(op)   ##IF STRINGS ARE DIFF LENGTH GIVES INSEX ERROR

##@@@## FOR DIFFRERENT LENGTH OF STR
s1=input("enter first str:")
s2=input("enter second str:")
op=''
i=j=0
while i<len(s1) or j<len(s2):
    if i< len(s1):
        op=op+s1[i]
        i+=1
    if j< len(s2):
        op=op+s2[j]
        j+=1
print(op)
