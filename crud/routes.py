from flask import render_template,request,jsonify,make_response
from flask_bcrypt import Bcrypt
from crud import app
from .model import signUp
import jwt
import json
bcrypt = Bcrypt(app)

app.config['SECRET_KEY']="secret_key"

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/signup',methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        
        if("Fname" in data and "Lname" in data and "Mobile" in data and "Password" in data and "Username" in data and "PasswordAgain" in data):
            if(data["Fname"]!=None and data["Lname"]!=None and data["Username"]!=None and data["Mobile"]!=None and data["Password"]!=None and data["PasswordAgain"]!=None):
                if(data["Password"] != data["PasswordAgain"]):
                    return jsonify({"msg":"Password doesn't match"})
                else:
                    pw_hash = bcrypt.generate_password_hash(data['Password'])
                    obj = signUp(Fname = data['Fname'],Lname = data['Lname'],Mobile = data['Mobile'], Username = data['Username'],Password = pw_hash)
                    if request.method == 'POST':
                        check = signUp.objects.all()
                        if check:
                            for user in check:
                                if user.Username == data['Username']:
                                    return jsonify({"msg":"Username is already in use"})
                                else:
                                    obj.save()
                                    return jsonify(obj)
                        else:
                            obj.save()
                            return jsonify(obj)
                    else:
                        return jsonify({"msg":"Not a valid method"})     
            else:
                return jsonify({"msg":"All field are required"})
        else:
            return jsonify({"msg":"Missing field"})


@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        if("Username" in data and "Password" in data):
            if(data["Username"]!=None and data["Password"]!=None):
                check = signUp.objects.all()
                if check:
                    for user in check:
                        if user.Username ==data['Username']:
                            pw_hash = user.Password
                            res = bcrypt.check_password_hash(pw_hash,data["Password"])
                            if(res):
                                token=jwt.encode({'user':str(data['Username'])},app.config['SECRET_KEY'],algorithm="HS256")
                                user.Flag = True
                                user.save()
                                return make_response(token)
                            else:
                                return jsonify({"msg":"Password doesn't match"})
                else:
                    return jsonify({"msg":"No user found"})
            else:
                return jsonify({"msg":"All fields are required"})
        else:
            return jsonify({"msg":"Missing Fields"})

@app.route('/profile')
def profile():
    token = request.headers['token']
    try:
     decoded = jwt.decode(token,app.config['SECRET_KEY'], algorithms=["HS256"])
    except:
     return jsonify({"msg":"Bad token"})
    
    if(decoded):
        Details = signUp.objects(Username =decoded['user'] ).get_or_404()
        if Details.Flag:
            return jsonify(Details.Username)
        else:
            return jsonify({"msg":"user is not logged in"})
    else:
        return jsonify({"msg":"user is not logged in"})

@app.route('/logout/<user>')
def logout(user):
    Details = signUp.objects(Username =user ).get_or_404()
    Details.Flag = False
    Details.save()
    return make_response({"msg":"User Logout sucessfully"})

@app.route('/alluser')
def alluser():
    users=signUp.objects.all()
    return jsonify(users)
  
    

    
    

    


                








    

