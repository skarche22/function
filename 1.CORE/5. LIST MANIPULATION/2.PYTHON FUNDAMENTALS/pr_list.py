## 1.Addition of elements in list
#
# lst=[10,20,30,40]
# a=(range(len(lst)))
# res=0
# print(a)
# for i in a:
#     res=res+lst[i]
# print(res)

##2.
# l=["santosh",'karche','team','brainworks','python']
# x=len(l)
# print(x)
# for i in range(x):
#     print("the index is ",i, "and element is", l[i])

##syntax===('string'.join(iterable))
#
# t=('Team','Brainworks','Pune')
# x=("#".join(t))       ###joined bet # char
# print(x)
# print(type(x))
#
# d={'city':'pune','population':'25 lakhs','edu':'good'}
# y=("@".join(d))           ## only keys will be joined
# print(y)
# print(type(y))


## Check given char is present in str or not
s=input("enter str:")
d={}
for i in s:
    if i in d.keys():
        d[i]=d[i]+1
    else: d[i]=1

for k,v in d.items():
    print("{}={} TIMES".format(k,v))
