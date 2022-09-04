##Method overriding
#Overriding class is applicable to both constructor and methods also;

class A:
    def add(self):
        print("My hobby is cricket")

class B(A):
    def add(self):
        print("sachin want football")
obj=B()
obj.add()

##Method 2 By using super keywords we can call parent class in child class

class A:
    def add(self):
        print("My hobby is cricket")

class B(A):
    def add(self):
        super().add()
        print("sachin want football")
obj=B()
obj.add()