from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 가위바위보 random_number 생성
random_number = random.randint(1, 3) 


computer_RCP = "" 
if random_number == 1:           
    computer_RCP = "가위"
elif random_number == 2:
    computer_RCP = "바위"
else:                       
    computer_RCP = "보"


# DB 생성
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


# 유저 인풋(가위/바위/보) DB
class UserInput(db.Model):
    trial = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'내가 낸 것 : {self.user_input}'


#  인풋 결과값 승무패 DB
class RCPrecords(db.Model):
    trial = db.Column(db.Integer, primary_key=True)
    win = db.Column(db.Integer, nullable=False)
    lose = db.Column(db.Integer, nullable=False)
    draw = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'승: {self.win} 패: {self.lose} 무: {self.draw}'


with app.app_context():
    db.create_all()


# homepage
@app.route("/")
def home():
    return render_template("index.html")
    # RCP_records = RCPrecords.query.all()
    # return render_template("index.html", data=RCP_records)


# homepage의 유저인풋 가져오기
@app.route("/create/")
def RCP_create():
    user_input_receive = request.args.get("user_input")

    user_input_records = UserInput(user_input=user_input_receive)
    db.session.add(user_input_records)
    db.session.commit()
    return redirect(url_for('outcome'))


# @app.route("/create/")
# def RCP_create():
#     win_receive = request.args.get("win")
#     lose_receive = request.args.get("lose")
#     draw_receive = request.args.get("draw")

#     rcprecords = RCPrecords(win=win_receive, lose=lose_receive, draw=draw_receive)
#     db.session.add(rcprecords)
#     db.session.commit()


# 게임결과 페이지
@app.route("/outcome")
def outcome():
    user_inputs = UserInput.query.all()
    return render_template("outcome.html", data=user_inputs)
    

if __name__ == "__main__":
    app.run(debug=True)