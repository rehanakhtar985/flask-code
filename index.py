from crypt import methods
from flask import Flask, flash,render_template,request,redirect,url_for,session
import os 
import mysql.connector 

app = Flask(__name__)
app.secret_key=os.urandom(24)


connection=mysql.connector.connect(host="localhost",user="rehan",password="letmein1",database="login",port="3306",auth_plugin='mysql_native_password' )
mycursor=connection.cursor()

@app.route("/home")
def home():
    if 'user_id' in session:
        return render_template('uhome.html')
    else:
        return redirect('/')

    

@app.route("/register")
def register():
    return render_template('uregister.html')

@app.route("/")
def login():
    return render_template('ulogin.html')

@app.route("/login_validation", methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
     .format(email,password))
    fetchdata=mycursor.fetchall()
    if len(fetchdata)>0:
        session['user_id']=fetchdata[0][0]
        return redirect('/home')
    else:
            return redirect('/')

@app.route('/add_user',methods=['POSt'])
def add_user():
    rname=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    mycursor.execute("""INSERT INTO `users` (`user_id`,`email`,`password`) VALUES 
    (NULL,'{}','{}')""".format(email,password))
    connection.commit()
    mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser=mycursor.fetchall()
    session['user_id']=myuser[0][0]
    return redirect('/home')
    

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')
    
    
    # "The email is {} and password is {} ".format(email,password)



if __name__=='__main__':
    app.run(host="",port='5000',debug=True)   
  
   
       