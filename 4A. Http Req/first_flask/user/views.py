from flask import  Blueprint , jsonify , request ,json

req = Blueprint('user',__name__)

#
# @req.route('/welcome')
# def welcome():
#     return 'welcome to flask '

# @req.route('/',methods=['GET'])
# def fetch_data():
#     return 'list of users'
#

data= json.load(open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json','r'))
print(data)

#
# @req.route('/user_id',methods=['GET'])
# def show(id):
#     response=[x for x in data if x['id']==int(id)]
#     return jsonify((response))
#
# @req.route('/fetch_user',methods=['GET'])
# def fetch_user():
#     user_id = request.args.get ('user_id')
#     user_detail= [x for x in data if x["id"] == int(user_id)]
#     user_detail=user_detail[0] if user_detail else {}
#     return jsonify(user_detail)
#

# @req.route('/create_user', methods=['POST'])
# def create_user():
#     request_data = request.get_json()
#     new_user_id = data [-1]['id'] + 1
#     response = request_data
#     response['id'] = new_user_id
#     data.append(response)
#     json.dump(data, open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json','w'))
#     return jsonify((response))`
#
# @req.route('/create_user_form' , methods = ['POST'])
# def creat_user2():
#     name = request.form.get('name')
#     password=request.form.get('password')
#     new_user_id = data[-1]['id'] + 1
#     response = {
#         'id':new_user_id,
#         'name':name,
#         'password':password
#     }
#     data.append(response)
#     json.dump(data, open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json', 'w'))
#     return jsonify((response))
#
# @req.route('/update_user/<user_id>', methods=['PUT'])
# def update_user(user_id):
#     user_data=request.get_json()
#     for d in data:
#         if d['id'] == int(user_id):
#             if 'name' in user_data:
#                 d['name'] = user_data['name']
#             if 'password' in user_data:
#                 d['password'] = user_data['password']
#
#     # json.dump(data,open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json', 'w'))
#     with open("santosh.json",'w') as f:
#         json.dump(data,f,indent=10)
#     return"data updated successfully"
# @req.route('/delete/<user_id>/',methods=['DELETE'])
# def delete_user(user_id):
#     user_data=request.get_json()
#     for d in data:
#         if d['id'] == int('user_id'):
#             if 'name' in user_data:
#                 d['name']=user_data['name']
#             if 'password' in user_data:
#                 d['password']=user_data['password']
#     json.dump(data,open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json', 'w'))
#
#


## Get methods

@req.route('/1',methods=['GET'])
def show_data():
    return jsonify(data)

@req.route('/2/<int:id>',methods=['GET'])
def fetch_data_by_userid(id):
    user=request.args.get(id)
    response=[x for x in data if x["id"] == int(id)]
    return jsonify(response)

@req.route('/3/<name>',methods=['GET'])
def fetch_data_by_name(name):
    user=request.args.get(name)
    response=[x for x in data if x["name"] == name]
    return jsonify(response)

@req.route('/4/<passw>',methods=['GET'])
def fetch_data_by_password(passw):
    user=request.args.get(passw)
    response=[x for x in data if x["pass"] == passw]
    return jsonify(response)

##post method(create)

@req.route('/5/<int:id>',methods=['POST'])
def create_user_id(id):
    req_data=request.get_json()
    new_user_id = data[-1]["id"] + 1
    response=req_data
    response["id"] = new_user_id
    data.append(response)

    json.dump(data,open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json', 'w'))
    return jsonify(response)

@req.route('/5.1/<int:id1>' ,methods=['POST'])
def create_user_id1(id1):
    rd1=request.get_json()

    data.append(rd1)

    json.dump(data,open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json', 'w'))
    return jsonify(rd1)

@req.route('/6/create_user_form',methods=['POST'])
def create_user_form():
    new_user_id=data[-1]["id"]+1
    name = request.form.get('name')
    password=request.form.get('password')
    response = {
        'id':new_user_id,
        'name':name,
        'pass':password
    }
    data.append(response)
    json.dump(data, open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json', 'w'))
    return jsonify((response))

@req.route('/6.1',methods=['POST'])
def create_uf():
    id=request.form.get("id")
    name=request.form.get("name")
    password=request.form.get("password")

    response = {
        'id': id,
        'name': name,
        'pass': password
    }
    data.append(response)
    json.dump(data, open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json', 'w'))
    return jsonify((response))


@req.route('/9/<int:id>',methods=['DELETE','GET'])
def delete(id):
    for index,d in enumerate(data):
        if d['id']== id:
            del data[index]

    with open('E:\\STUDY\\4A. Http Req\\first_flask\\Data.json','w') as f:
        json.dump(data,f,indent=2)
    return jsonify(data)

















