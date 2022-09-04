import json
# with open("empjson.json",'r') as RF:
#     print(json.load(RF))

empJsonString= """{
     "empFalse":false,
     "empInt":243,
     "empList":[
          "a",
          "b",
          "c"
     ],
     "empNone":null,
     "empTrue":true,
     "empfloat":23.2,
     "empstring":"This is emp details",
     "emptuple":[
          "IT",
          "Mech",
          "Civil"
     ]
}"""

mydata= json.loads(empJsonString)
print(mydata)
