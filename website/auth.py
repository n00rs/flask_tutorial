from flask import Blueprint,render_template,request,flash,redirect,url_for
# import password hasing and checking the password hashed is correct methods from werkzeug.security module
from werkzeug.security import generate_password_hash,check_password_hash
# import user model
from .models import User
from . import db
# import methods that needs to handle session
from flask_login import login_user,logout_user,current_user,login_required
 # 
auth = Blueprint("auth",__name__)




@auth.route("/login",methods = ["GET","POST"])
def login():
    str_login_template = "login.html"
    if request.method == 'POST':
        str_email = request.form.get('email')
        str_password = request.form.get('password')
        # querying database
        user = User.query.filter_by(email=str_email.strip()).first()
        # login template name
        if not user:
            flash("INVALID_CREDENTIALS",category="error")
            return render_template(str_login_template,boolean = True,user=current_user)
            
            
        if check_password_hash(user.password,str_password):
            flash("Logged in successfull",category="success")
            # save user data in session 
            login_user(user=user)
            return redirect(url_for('views.home'))
        else:
            flash("Incorrect password",category='error')
            return render_template(str_login_template,boolean = True,user=current_user)
    else:
            return render_template(str_login_template,boolean = True,user=current_user)
        
            

        



@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))




@auth.route("/sign_up",methods = ["GET","POST"])
def sign_up():
    if request.method == 'POST':
        
        str_email = request.form.get('email')
        str_firstname = request.form.get('firstName')
        str_password1 = request.form.get('password1')
        str_password2 = request.form.get('password2')
        print(str_email,str_firstname,str_password1,str_password2)
        
        user = User.query.filter_by(email=str_email).first()
        
        if user:
            flash("EMAIL_ALREADY_EXISTS",category='error')
        elif len(str_email) < 4 :
            flash("Email must be grater than 4 characters." ,category='error')
        elif len(str_firstname) < 5 :
            flash("First name must be grater than 5 characters." , category='error')
        elif len(str_password1.strip()) < 7 :
            flash("Password must be greater than 7 letters",category="error")
        elif str_password2.strip() != str_password1.strip():
            flash("password doesn't match",category="error")
        else :
            new_user = User(email = str_email,password = generate_password_hash(str_password1,method='pbkdf2'),first_name=str_firstname)
            # create new user in db
            db.session.add(new_user)
            db.session.commit()
            
            flash("SUCCESSFULLY_CREATED",category="success",user=current_user)
            # redirect the user to home page
            return redirect(url_for('views.home'))
    # else :
    return render_template("sign_up.html")
