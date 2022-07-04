from crud import db

class signUp(db.Document):
    Fname=db.StringField(required=True,max_length=15)
    Lname=db.StringField(required=True,max_length=15)
    Mobile=db.LongField(max_length=10,required=True)
    Username=db.StringField(max_length=50,required=True)
    Password=db.StringField(max_length=500,required=True)
    Flag = db.BooleanField(default = False)
