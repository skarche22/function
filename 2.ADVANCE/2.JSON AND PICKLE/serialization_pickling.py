## Pickling is usually used for Binary only ///// serializtions output will gives binary stream

import pickle
dataPickle=("santosh","karche","Team Brainworks",['a','b','c','d'],{1:"Domestic",2:"Export",3:"Nylon"})
res=pickle.dumps(dataPickle)
print(res)            ## It will gives output in byte strem


mylist=["santosh",1992,2008,2010,2014,2022,("team brainworks ","python")]
byte=pickle.dumps(mylist)
print(byte)
print("file is created")


with open("myPickle.txt",'wb') as WB:
    print(pickle.dump(mylist,WB))
