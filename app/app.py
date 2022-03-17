from flask import Flask
from flask import render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_bootstrap import Bootstrap
import os
from flask_login import UserMixin,LoginManager,login_user,logout_user,login_required,current_user
import AI_analyse


app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)


class Younger(db.Model): # 若者テーブル
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(5),  nullable=False)
    job = db.Column(db.String(100), nullable=False)
    hobby = db.Column(db.String(100), nullable=False)

class User(UserMixin,db.Model): # ユーザテーブル
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(12))
    ai_survey = db.Column(db.String(5)) # 削除


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/',methods=["GET","POST"]) # トップページ
def top():
    return render_template('top.html')

@app.route('/index',methods=["GET","POST"]) # メイン画面
@login_required
def index():
    username = current_user.username
    if request.method == "GET":
        matchers = Younger.query.all()
        return render_template("/index.html",username=username,matchers = matchers)

@app.route('/signup',methods=["GET","POST"]) # 新規登録画面
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username,password=generate_password_hash(password,method="sha256"))
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    else:
        return render_template("signup.html")
        
@app.route('/login',methods=["GET","POST"]) # ログイン画面
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if check_password_hash(user.password,password):
            login_user(user)
            return redirect("/index")
    else:
        return render_template("login.html")

@app.route("/logout") # ログアウト処理
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/survey',methods=["GET","POST"]) # 調査画面
def survey():
    if request.method == "POST":
        if request.form.get('region') == '東京':
            regi = ['1','0','0','0']
        elif request.form.get('region') == '千葉':
            regi = ['0','1','0','0']
        elif request.form.get('region') == '埼玉':
            regi = ['0','0','1','0']
        else:
            regi = ['0','0','0','1']
        array = [[request.form.get('age'),request.form.get('sex'),request.form.get('sick'),request.form.get('family'),request.form.get('lonely'),request.form.get('exersise'),request.form.get('sleep'),*regi,request.form.get('money')]] # 調査から取得したAI判定に必要な特徴量
        
        flag = AI_analyse.analyze(array)
        value = AI_analyse.percent(array)

        if flag == [0]:
            return render_template("dn_need.html")
        elif flag == [1]:
            return render_template("n_help.html",value = value)
        else:
            return render_template("survey.html")
    else:
        return render_template("survey.html")

@app.route('/n_help',methods=["GET","POST"]) # 介護見込み有
def n_help():
    return render_template("n_help.html")

@app.route('/dn_need',methods=["GET","POST"]) # 介護見込み無
def dn_need():
    return render_template("dn_need.html")

@app.route('/admin',methods=["GET","POST"])
def admin(): # 管理者専用画面
    if request.method == "POST":
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')
        hobby = request.form.get('hobby')
        person = Younger(name=name,age=age,job=job,hobby=hobby)
        db.session.add(person)
        db.session.commit()
        return redirect("/index")
    else:
        return render_template("admin.html")

@app.route('/<int:id>/delete',methods=["GET"])
@login_required
def delete(id): # ごめんなさい...の処理
    person = Younger.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return redirect("/index")


if __name__ == "__main__": # ファイルの実行
    app.run(debug=True)