from serialization_pickling import *
import pickle

PO=pickle.loads(res)   ## To convert the binary to readable format we use loads
print(PO)

with open("myPickle.txt","rb") as RB:
    POP=pickle.load(RB)
print("Extract the saved data into the file",RB)