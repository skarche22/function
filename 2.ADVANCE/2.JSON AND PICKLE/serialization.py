import json
empDict={
    "empList":["a","b","c"],
    "emptuple":("IT","Mech","Civil"),
    "empstring":"This is emp details",
    "empInt":243,
    "empfloat":23.2,
    "empTrue":True,
    "empFalse":False,
    "empNone":None
}
print(type(empDict))
res=json.dumps(empDict)
print(res)
print(type(res))

with open('empJSON.json','w') as WF:
    json.dump(empDict,WF,indent=5,separators=("," ,":",),sort_keys=True)
print("empjson,json file is created")
