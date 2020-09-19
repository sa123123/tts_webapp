from flask import Flask, render_template, request,url_for,flash
from flaskweb import app,db,bcrypt
from flaskweb.models import User
from flaskweb.forms import SignupForm,LoginForm
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html')


@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)


@app.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(firstname=form.firstname.data,lastname=form.lastname.data,email=form.email.data,password=hashed_password,number=form.number.data)
        db.session.add(user)
        db.session.commit()
        flash('YOUR ACCOUNT IS CREATED ! YOU CAN LOGIN')
        return redirect(url_for('login'))
    return render_template('signup.html',title='SignUp',form=form)


@app.route('/contact')
def contact():
    return render_template('contact.html')