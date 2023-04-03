from flask import Flask,request,redirect,render_template,url_for,flash,session
from flask_mysqldb import MySQL
from flask_session import Session
import random
app=Flask(__name__)
app.secret_key='$hgeihe'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='spm'
Session(app)
mysql=MySQL(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration',methods=['GET,POST'])
def register():
    if request.method=='POST':
        rollno=request.form['rollno']
        name=request.form['name']
        group=request.form['group']
        password=request.form['password']
        code=request.form['code']
        #define college code
        code='sdmsmkpbsc$#23'
        if ccode==code:
            opt=genotp()
            return otp
        else:
            flash('Invalid college code')
            return render_template('register.html')
    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('login.html')
app.run(debug=True,use_reloader=True)
