# f=open("abc.txt",'r')
# # print(f.read())
# # print(f.readline())
# # print(f.readlines())
# f.close()


# # Write W
# f1=open("xyz.txt",'w')
# f1.write("India is my country\n")
# f1.write("India is my best country\n")
# f1.write("which is my country\n")
# print("file created")
# f.close()


# #Append "A"
# with open("xyz.txt",'a') as f:
#     f1.write("I am appending data after country  data\n")
#     f1.write("I am appending 2n d line data after country  data\n")
#     print("data append successful")
#     print("data append")
#
# #
# f=open("pqr.txt","w")
# f.write("Ternary operators program\n")
# f.write("assert used for validation")
# print("file name",f.name)
# print("mode ",f.mode)
# print("file is readable",f.readable())
# print("file is writable",f.writable())
#
# # f.close()
#
#
# # W+ == file preferences firsrt write and then read the file(Ovrriding the data)....
#
# f=open("pqr.txt","w+")
# f.write("Ternary operators program\n")
# f.write("assert used for validation")
# print(f.read())
# print("file name",f.name)
# print("mode ",f.mode)
# print("file is readable",f.readable())
# print("file is writable",f.writable())
#
# f.close()


## Append A+

f=open("pqr.txt","a+")
f.write("Ternary operators program\n")
f.write("assert used for validation\n")
print(f.read())
print("file name",f.name)
print("mode ",f.mode)
print("file is readable",f.readable())
print("file is writable",f.writable())

f.close()