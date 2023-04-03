from flask import Flask,request,render_template,url_for,redirect,session
from flask_session import Session
from flask_mysqldb import MySQL
app=Flask(_name_)
app.secret_key='monkey'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='emp'
Session(app)
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def emp():
    if request.method=='POST':
        eid=request.form['eid']
        ename=request.form['ename']
        erole=request.form['erole']
        mobile=request.form['mobile']
        dept=request.form['dept']
        salary=request.form['salary']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into emp values(%s,%s,%s,%s,%s,%s)',(eid,ename,erole,mobile,dept,salary));
        mysql.connection.commit();
        cursor.close();
    return render_template('emp.html')
app.run(debug=True,use_reloader=True)
