# 51. Python | Find all close matches of input string from a list
# 52. Python program to find uncommon words from two Strings
#without using inbuilt functions
# str1=input("string 1:")
# str2=input("string 2:")
# str3=''
# for word1 in str1:
#     if word1 not in str2:
#         str3 +=word1
# for word1 in str2:
#     if word1 not in str1:
#         str3 += word1
# print(str3)

#with using  inbuilt fun @@@ Not solved corr
# a=input("string 1:")
# b=input("string 2:")
# a=a.split
# c=set(a)
# print(c)
# d=set(b.split)
#
# e=c.difference(d)
# f=d.differece(c)
#
# g=e.union(f)
# print(g)
#
#
# # 53. Python | Swap commas and dots in a String
# a="Hi,i am santosh.replacing, comma by dot."
# b=[]
# for i in a:
#     if i==",":
#         b.append(".")
#     elif i==".":
#         b.append(",")
#     else:
#         b.append(i)
#
# c="".join(b)
# print(c)
#
# ##method 2
# str="1,2,3,4.5,6,7,8.9,9.6"
# def Replace(str):
#     str=str.replace(",","temp")
#     str=str.replace(".",",")
#     str = str.replace("temp",".")
#     return str
#
# print(Replace(str))
#
#
#
# # 54. Python | Permutation of a given string using inbuilt function
# from itertools import permutations
# import string
# a="python"
# b=permutations(a)
# c=[]
# for i in b:
#     d="".join(i)
#     c.append(d)
# print(c)             # It takes as per factorial no of the given str
# print(len(c))
#
#
# ## Second method
#
# # 55. Python | Check for URL in a String Execute a String of Code in
#
#
# # 56. Python String slicing in Python to rotate a string
# # 57. String slicing in Python to check if a string can become empty by recursive deletion
# a="my name is santosh"
# a*=0
# print(a)
# # 58. Python Counter| Find all duplicate characters in string Dictionary Programs:

# 59. Python | Sort Python Dictionaries by Key or Value Handling missing keys in
# 60. Python dictionaries Python dictionary with keys having multiple inputs
# 61. Python program to find the sum of all items in a dictionary
# 62. Python | Ways to remove a key from dictionary Ways to sort list of dictionaries by values in
# 63. Python – Using itemgetter Ways to sort list of dictionaries by values in Python – Using lambda
# function
# 64. Python | Merging two Dictionaries Program to create grade calculator in Python
# 65. Python | Check order of character in string using OrderedDict( )
# 66. Python Counter to find the size of largest subset of anagram words
# 67. Python | Remove all duplicates words from a given sentence
# 68. Python Dictionary to find mirror characters in a string Counting the frequencies in a list using
# dictionary in Python
# 69. Python | Convert a list of Tuples into Dictionary
# 70. Python counter and dictionary intersection example (Make a string using deletion and
# rearrangement)
# 71. Python dictionary, set and counter to check if frequencies can become same Scraping And
# Finding Ordered Words In A Dictionary using Python Possible Words using given characters in
# Python
#
# Input = "Djka1sjsjs2anns4ksmsm3"
# store=""
# for i in Input:
#     if (i=="1")| (i=="2")|(i=="3")|(i=="4")|(i=="5")|(i=="6")|(i=="7")|(i=="8")|(i=="9")|(i=="0"):
#         store=store+i
# for j in Input:
#     if (j!="1")& (j!="2")&(j!="3")&(j!="4")&(j!="5")&(j!="6")&(j!="7")&(j!="8")&(j!="9")&(j!="0"):
#         store=store+j
#
# print(store)


# s=set()
# s.add(15)
# print(s)
# s.add(33)
# s.update([33])
# print(s)
### Method 2)
s="sf3loih2jdcx1hdus4owp"
# O/p=>1234<alphabets
a=[]
b=[]
for i in s:
    if i.isalpha():
        a.append(i)
    else:
        b.append(i)

result=" ".join(sorted(b)+sorted(a))
print(result)