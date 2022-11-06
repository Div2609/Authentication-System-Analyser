from flask import Flask ,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'

db=SQLAlchemy(app)
class user(db.Model):
    email_id = db.Column('email_id',db.String(100),primary_key = True)
    password = db.Column(db.String(10))

    def __init__(self, email_id,password):
        self.email_id =email_id
        self.password = password


@app.route('/')
def showall():
    l=[]
    for i in user.query.all():
        l.append({'email_id':i.email_id,'password':i.password})

    return {"users": l}


@app.route('/signup', methods=['POST'])
def signup():
    user1= user(request.json['email_id'], request.json['password'])
    db.session.add(user1)
    db.session.commit()
    json = request.json
    return json


@app.route('/login', methods=['POST'])
def login():
    user1= user.query.filter_by(email_id=request.json['email_id']).first()
    if user1.password==request.json['password']:
        # print(user1.email_id,user1.password)
        return {"message": "Authenticated"}
    else:
        return {"message": "Invalid User"}



if __name__ == '__main__':
    db.create_all()
    app.run('0.0.0.0', 5000, debug=True)
