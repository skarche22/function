
n = int(input("Enter no.of record: \n"))
student_marks ={}
for i in range(n):
    name,*marks=input().split()
    student_marks[name]=marks
st=input("Enter name of student to calculate avarage:")
if (st in student_marks.keys()):
    print("Marks is:",*student_marks[st])
    values=student_marks[st]
    total=[float(x) for x in values]
    sub=len(total)
    total_mark=sum(total)
    res=total_mark/sub
    print("Percentage is :",res)