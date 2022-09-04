# # Python File Handling Programs:
# # 1. Python program to read file word by word
# f=open("abc.txt",'r')
# list1=f.readlines()
# for line in list1:
#     word_list=line.split()
#     for w in word_list:
#         print(w)


# # 2. Python program to read character by character from a file
# f=open("abc.txt",'r')
# data=f.read()
# print(data)
# for letter in data:
#    print(letter)


# 3. Python – Get number of characters, words, spaces and lines in a file
f=open("abc.txt",'r')
z1=f.readlines()
count_lines=0
for l in z1:
    count_lines +=1
print("No of lines in a file:",count_lines)
wcount=0
for l in z1:
    word=l.split()
    for w in word:
        wcount +=1
    print("No of words present:",wcount)

f=open("abc.txt",'r')
z2=f.read()
ccount=0
for i in z2:
    ccount+=1
print("No of char in file:",ccount)


# 4. Python | Finding ‘n’ Character Words in a Text File
# 5. Python Program to obtain the line number in which given word is present
# 6. Count number of lines in a text file in Python
# 7. Python Program to Eliminate repeated lines from a file
# 8. Python – Append content of one text file to another
# 9. Python program to copy odd lines of one file to other
# 10. Python Program to merge two files into a third file
# 11. Python program to Reverse a single line of a text file
# 12. Python program to reverse the content of a file and store it in another file