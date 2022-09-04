from flask import Blueprint , request ,jsonify
from firsk_flask import db
from firsk_flask.usersql.models import User

mod=Blueprint('usersql',__name__)

@mod.route('/',methods=['GET'])
def fetch_user():
    users = User.query.all()        ##SELECT * FROM USER
    print(users)
    response=[x.__repr__() for x in users]
    return jsonify(response)



