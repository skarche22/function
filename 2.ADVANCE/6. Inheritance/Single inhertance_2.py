# 1. Single Inheritance:
# class P:
#     def m1(self):
#         print("Parent Method")
# class C(P):
#     def m2(self):
#         print("Child Method")
# c=C()
# c.m1()
# c.m2()



#1
class Shivaji:
    def maharaja(self):
        print("chatrapati")

class Sambhaji(Shivaji):
    def maharaj(self):
        print("Youvraj")

s = Sambhaji()
S= Shivaji()

S.maharaja()
s.maharaj()
