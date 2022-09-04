#class is mold or dye and the bucket= object
# class is blueprint of the object
##Physical instance of the class is obj


# class Santosh:
#     def __init__(self):
#         pass
#     def abc(self):
#         print("Hi my name is SANTOSH")
# o=Santosh()
# o.abc()
#
# class Car:
#     def __init__(self,n,y):
#         self.model_name=n
#         self.launch_year=y
#         print("y:",y,"n:",n)
#     def details(self,n,y):
#         print(n)
#         print(y)

# A=Car("swift",2001)
# A.details("Innove",2013)


# class Car:
#     def __init__(self,nm,yr):
#         self.model_name=nm
#         self.year=yr
#     def details(self):
#         pass
# swift=Car("swift",2011)
# print(swift.year)
# innova=Car("Innova",2020)
# print(innova.year)


#
# class Garware:
#     def __init__(self,n,y):
#         self.name=n
#         self.year=y
#     def details(self):
#         pass
# Dom=Garware("BTR",2019)
# print(Dom.year,Dom.name)
# Exp=Garware("Delu",2020)
# print(Exp.year,Exp.name)
#
# class Kls:
#     def __init__(self,ms,md,mb):
#         self.mesh_size=ms
#         self.mesh_depth=md
#         self.mesh_base=mb
# class Nylon:
#     def net(self,ms,md):
#         self.mesh_size=ms
#         self.mesh_depth=md
# class Dom:
#     def LMS(self,m,l,nf):
#         self.moisture=m
#         self.length=l
#         self.quality=nf
#
# salmar=Kls(80,200.5,0.05)
# print(salmar.mesh_size)
# BRSF=Kls(60,150,0.03)
# shednet=Kls(300,400.5,0.01)
# print(shednet.mesh_depth)
#
# hwd=Nylon()
# hwd.net(45,300.5)
# print(hwd.mesh_depth)
#
# pkg=Dom()
# pkg.LMS("below 7%","upto 60 mtr","checked")
# print("You can pack mtl: ",pkg.moisture,pkg.length)



# class Tb:
#     def course(self,p,s,j,m):
#         self.python=p
#         self.salesforse=s
#         self.java=j
#         self.mernstek=m
# sub=Tb()
# sub.course("dec 2022","sept 2022","aug2022","Feb 2023")
# print("The fullstack web developers batch place in month:",sub.python,"and mern batch will be placed on date",sub.mernstek)


# USE OF DOC STRING IN CLASS AND ACCESS

# class Pune:
#     ''' pune is the very useful in completing the the courses'''
#     def __init__(self):
#         print("Tell something about pune")
#     def info(self):
#         pass
# p=Pune()
# print(Pune.__doc__)
# help(Pune)     ## it provides complete information about class Pune
#
#
# f=open("class.txt",'w')
# f.close()


# Self varible:
# current object of the class
#
# class Empl:
#     ''' employee informaation '''
#     def __init__(self,en,enm,es,ed):
#         self.employee_no=en
#         self.emp_name=enm
#         self.emp_sal=es
#         self.emp_add=ed
#     def info(self):
#         print(f"the req info of the employee is {self.employee_no} , name is {self.emp_name}")
#         print(f"the salary is {self.emp_sal}, and adress is {self.emp_add}  ")
#
# d1=Empl(101,"santosh",10000,"satara")
# d1.info()


## instead of self we can use any variable
# class Swaraj:
#     def __init__(s,nm,h,c):
#         s.name=nm
#         s.height=h
#         s.character=c
#     def details(x):
#         print(f"the hindavi swraj was established by {x.name} the height is {x.height} ft and char is {x.character}")
#
# Sw=Swaraj("chatrapati Shivaji maharaj",6,"very good ")
# # Sw.details("chatrapati Shivaji maharaj",6,"very good ")
# Sw.details()

# Parameterized constructor?
class Addition:
    ans=0
    first = 0
    sedond = 0
    third = 0
    def __init__(self,a,b,c):
        self.first=a
        self.sedond=b
        self.third=c
        # self.ans=a+b+c
    def add(self):
        print(f"addition of three nos {self.first} + {self.sedond} + {self.third}  = {self.ans}")
    def calc(self):
        self.ans=self.first+ self.sedond + self.third
        print(self.ans)
x=Addition(100,200,300)
x.calc()
x.add()