class Maharashtra:
    def __init__(s,a,b):
        print("constr execution")
        s.state=a
        s.terret=b
    def dt(x):
        print("Method execution s")
        print(x.state)
        print(x.terret)
        print("Method execution c")

ob=Maharashtra("36 states","7 terretories")
ob.dt()