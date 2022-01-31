from crypt import methods
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def hello():
    return render_template('register.html')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login_validation", methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    if email=='rehan@gmail.com'and password=='earth':
        return  render_template('home.html')
    else :
        return " INVALID USERNAME AND PASSWORD ."

    @app.route('/logout')
    def logout():
        return redirect('/login')
    
    
    # "The email is {} and password is {} ".format(email,password)



if __name__=='__main__':
    app.run(debug=True)   
  
   
       