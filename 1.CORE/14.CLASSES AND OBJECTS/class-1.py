# from unicodedata import name

#Q== program to demonstrat execute cunstructor only once in program

class Family:
    def __init__(self):
        print("constructor execution")
    def m1(self):
        print("method execution")
t1=Family()
t2=Family()            
t3=Family()        
t1.m1()



#Q programme to create stu_class & creates an obj to it. call methods talk to display student details

class Student:
    def __init__(self,name,roll_no, marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def talk(self):
        print("hello my name is ", self.name)
        print("my roll no",self.roll_no) 
        print("My marks are",self.marks)   

    def display(self):
        print("Student Name:{}\n Roll no:{}\n Marks:{}".format(self.name,self.roll_no,self.marks))    
s1=Student("Santosh",95,91)
s1.talk()
s1.display()        
