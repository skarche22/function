# class Duck:
#     def talk(self):
#         print("quak_quak")
#
# class Dog:
#     def talk(self):
#         print("Bho_bho")
#
# def abc(obj):
#     obj.talk()
#
# o1=Duck()
# o2=Dog()
# abc(o1)
# abc(o2)


class Duck:
    def talk(self):
        print("quak_quak")

class Dog:
    def walk(self):
        print("Bho_bho")

def abc(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"walk"):
        obj.walk()


o1=Duck()
o2=Dog()
abc(o1)
abc(o2)
