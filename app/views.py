from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Tony' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Username="' + form.username.data + '", Password="' + form.password.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form)
@app.route('/panels', methods = ['GET', 'POST'])
def panels():
    return render_template('panels.html',
        title = 'My Panels',
        panels = [])
